# main.py

from langchain.agents import initialize_agent, AgentType, Tool
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Load environment variables
load_dotenv()

app = FastAPI()

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Update with your frontend URL if different
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the LLM with GoogleGenerativeAI
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Define URLs for specific products
product_urls = {
    "Roshan Digital Account": "https://www.mcb.com.pk/personal/roshan-digital-account",
    "Cards": "https://www.mcb.com.pk/personal/cards"
}

# Load and process documents for each product
vector_stores = {}

for product, url in product_urls.items():
    loader = WebBaseLoader(url)
    docs = loader.load()
    split_docs = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200).split_documents(docs)
    vector_stores[product] = FAISS.from_documents(
        split_docs,
        GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    )

# Create retriever tools for each product
retriever_tools = {}

for product, vector_store in vector_stores.items():
    retriever = vector_store.as_retriever()
    retriever_tools[product] = retriever

# Define Tool functions manually to ensure single string output
def retrieve_roshan_digital_account(query: str) -> str:
    results = retriever_tools["Roshan Digital Account"].get_relevant_documents(query)
    if not results:
        return "No information found for your query."
    # Combine the content from all relevant documents
    combined_content = "\n".join([doc.page_content for doc in results])
    return combined_content

def retrieve_cards(query: str) -> str:
    results = retriever_tools["Cards"].get_relevant_documents(query)
    if not results:
        return "No information found for your query."
    # Combine the content from all relevant documents
    combined_content = "\n".join([doc.page_content for doc in results])
    return combined_content

# Define Tools with single output
tools = [
    Tool(
        name="Roshan Digital Account",
        description="Use this tool to get information about Roshan Digital Account of MCB Bank Limited.",
        func=retrieve_roshan_digital_account
    ),
    Tool(
        name="Cards",
        description="Use this tool to get information about Cards of MCB Bank Limited.",
        func=retrieve_cards
    )
]

# Initialize the agent with the defined tools
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

@app.post("/query")
async def query(request: Request):
    data = await request.json()
    product = data.get("product")
    user_input = data.get("query")
    
    if not product or not user_input:
        return {"error": "Product and query must be provided."}
    
    if product not in product_urls:
        return {"error": "Invalid product specified."}
    
    try:
        # Execute the agent with the user input
        response = agent.run(user_input)
    except Exception as e:
        return {"error": f"Error processing the request: {str(e)}"}
    
    return {"response": response}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
