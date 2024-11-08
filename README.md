# A Learning Project based on Public information


# MCB Bank Products AI Agent

![MCB Bank Logo](https://www.mcb.com.pk/sites/default/files/mcb_logo.png)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Configuration](#configuration)
  - [Environment Variables](#environment-variables)
- [Running the Application](#running-the-application)
  - [Starting the Backend Server](#starting-the-backend-server)
  - [Starting the Frontend Server](#starting-the-frontend-server)
- [Usage](#usage)
- [Deployment](#deployment)
  - [Backend Deployment](#backend-deployment)
  - [Frontend Deployment](#frontend-deployment)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

The **MCB Bank Products AI Agent** is an interactive web application that leverages artificial intelligence to provide users with detailed information about specific MCB Bank products: **Roshan Digital Account** and **Cards**. Users can inquire about eligibility criteria, features, and other relevant details through a user-friendly interface, receiving instant AI-generated responses.

## Features

- **Product-Specific Information:** Tailored responses for Roshan Digital Account and Cards.
- **Interactive UI:** Clickable product cards that reveal query forms.
- **AI-Powered Responses:** Utilizes Langchain and Google Generative AI for accurate information retrieval.
- **Responsive Design:** Built with Next.js and Tailwind CSS for a professional and mobile-friendly interface.
- **Secure Backend:** FastAPI backend with CORS protection and environment variable management.

## Technologies Used

- **Frontend:**
  - [Next.js](https://nextjs.org/)
  - [TypeScript](https://www.typescriptlang.org/)
  - [Tailwind CSS](https://tailwindcss.com/)
- **Backend:**
  - [FastAPI](https://fastapi.tiangolo.com/)
  - [Langchain](https://github.com/hwchase17/langchain)
  - [Google Generative AI](https://cloud.google.com/ai)
  - [FAISS](https://github.com/facebookresearch/faiss)
- **Other Tools:**
  - [Uvicorn](https://www.uvicorn.org/)
  - [Dotenv](https://github.com/theskumar/python-dotenv)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Operating System:** Windows, macOS, or Linux.
- **Node.js:** Version 14 or higher. [Download Node.js](https://nodejs.org/)
- **Python:** Version 3.8 or higher. [Download Python](https://www.python.org/downloads/)
- **Git:** Installed and configured. [Download Git](https://git-scm.com/downloads)
- **API Keys:**
  - **Google API Key:** For Google Generative AI.
  - **Tavily API Key:** For Tavily Search Results.

## Installation

### Backend Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/mcb-bank-ai-agent.git
   cd mcb-bank-ai-agent/backend
   ```

2. **Create a Virtual Environment:**

   It's recommended to use a virtual environment to manage dependencies.

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment:**

   - **Windows:**

     ```bash
     venv\Scripts\activate
     ```

   - **macOS/Linux:**

     ```bash
     source venv/bin/activate
     ```

4. **Install Backend Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   > **Note:** If `requirements.txt` is not present, install dependencies manually:

   ```bash
   pip install fastapi uvicorn langchain langchain-google-genai langchain-community faiss-cpu langchain-text-splitters python-dotenv
   ```

### Frontend Setup

1. **Navigate to Frontend Directory:**

   ```bash
   cd ../frontend
   ```

2. **Install Frontend Dependencies:**

   ```bash
   npm install
   ```

   > **Note:** If Tailwind CSS is not set up, follow these steps:

   ```bash
   npm install -D tailwindcss postcss autoprefixer
   npx tailwindcss init -p
   ```

3. **Configure Tailwind CSS:**

   Ensure `tailwind.config.js` is properly set up:

   ```javascript
   /** @type {import('tailwindcss').Config} */
   module.exports = {
     content: [
       "./pages/**/*.{js,ts,jsx,tsx}",
       "./components/**/*.{js,ts,jsx,tsx}",
     ],
     theme: {
       extend: {},
     },
     plugins: [],
   }
   ```

4. **Add Tailwind Directives to CSS:**

   In `styles/globals.css`, add:

   ```css
   @tailwind base;
   @tailwind components;
   @tailwind utilities;
   ```

## Configuration

### Environment Variables

1. **Create a `.env` File in the Backend Directory:**

   ```bash
   touch .env
   ```

2. **Add the Following Variables to `.env`:**

   ```env
   GOOGLE_API_KEY=your_google_api_key
   TAVILY_API_KEY=your_tavily_api_key
   ```

   > **Replace** `your_google_api_key` and `your_tavily_api_key` with your actual API keys.

## Running the Application

### Starting the Backend Server

1. **Activate the Virtual Environment:**

   - **Windows:**

     ```bash
     venv\Scripts\activate
     ```

   - **macOS/Linux:**

     ```bash
     source venv/bin/activate
     ```

2. **Navigate to Backend Directory:**

   ```bash
   cd backend
   ```

3. **Start the FastAPI Server:**

   ```bash
   python main.py
   ```

   The backend server will start on [http://127.0.0.1:8000](http://127.0.0.1:8000).

### Starting the Frontend Server

1. **Navigate to Frontend Directory:**

   ```bash
   cd ../frontend
   ```

2. **Start the Next.js Development Server:**

   ```bash
   npm run dev
   ```

   The frontend application will be accessible at [http://localhost:3000](http://localhost:3000).

## Usage

1. **Access the Application:**

   Open your browser and navigate to [http://localhost:3000](http://localhost:3000).

2. **Interact with Product Cards:**

   - **Roshan Digital Account:**
     - Click on the "Roshan Digital Account" card to expand the query form.
     - Enter your query (e.g., "What is the eligibility criteria?") and click "Ask".
     - Receive AI-generated responses based on the provided information.
   
   - **Cards:**
     - Click on the "Cards" card to expand the query form.
     - Enter your query (e.g., "What types of cards do you offer?") and click "Ask".
     - Receive AI-generated responses based on the provided information.

## Deployment

### Backend Deployment

1. **Choose a Hosting Platform:**

   Consider platforms like **Heroku**, **AWS EC2**, **Google Cloud Run**, or **Azure App Service**.

2. **Set Up the Environment:**

   - Upload your backend code.
   - Install dependencies using the `requirements.txt`.
   - Configure environment variables on the hosting platform.

3. **Run the Server:**

   Ensure the server is set to run using a production-ready server like **Gunicorn** with **Uvicorn** workers.

   ```bash
   gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
   ```

4. **Update CORS Settings:**

   Modify the `allow_origins` in `main.py` to include your production frontend URL.

### Frontend Deployment

1. **Choose a Hosting Platform:**

   Consider platforms like **Vercel**, **Netlify**, or **AWS Amplify**.

2. **Deploy the Frontend:**

   - Connect your Git repository to the hosting platform.
   - Configure build settings if necessary.
   - Deploy the application.

3. **Update Backend API URL:**

   Ensure the frontend points to the deployed backend API instead of `http://127.0.0.1:8000`.

   ```tsx
   // Example: Update fetch URL in ProductCard.tsx
   const res = await fetch('https://your-backend-domain.com/query', {
     //...
   });
   ```

## Troubleshooting

### Common Issues

1. **CORS Errors:**

   - **Symptom:** Frontend unable to communicate with the backend due to CORS policy.
   - **Solution:** Ensure that the backend's CORS middleware includes the correct frontend URL.

2. **API Endpoint Not Accessible:**

   - **Symptom:** Unable to access backend API at `http://127.0.0.1:8000`.
   - **Solution:** Verify that the backend server is running. Check for any errors in the backend logs.

3. **Environment Variables Not Loaded:**

   - **Symptom:** Backend unable to access API keys.
   - **Solution:** Ensure that the `.env` file is correctly placed in the backend directory and contains the necessary keys.

4. **Image Not Displaying:**

   - **Symptom:** Product images do not appear on the frontend.
   - **Solution:** Verify that the image URLs are correct and accessible. If using local images, ensure they are placed in the `public` folder and the paths are correctly referenced.

5. **"Error processing the request" Messages:**

   - **Symptom:** Users receive error messages when submitting queries.
   - **Solution:** Check backend logs for detailed error messages. Ensure that tools are correctly defined and return single string outputs.

### Debugging Steps

1. **Check Backend Logs:**

   Monitor the terminal running the FastAPI server for any error messages or stack traces.

2. **Use API Documentation:**

   Navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to access FastAPI's interactive API documentation. Test the `/query` endpoint directly.

3. **Verify API Keys:**

   Ensure that `GOOGLE_API_KEY` and `TAVILY_API_KEY` are valid and have the necessary permissions.

4. **Network Configuration:**

   Ensure that no firewall or antivirus software is blocking the backend server's port (`8000`).

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. **Fork the Repository:**

   Click the "Fork" button at the top right of this page.

2. **Clone Your Fork:**

   ```bash
   git clone https://github.com/yourusername/mcb-bank-ai-agent.git
   cd mcb-bank-ai-agent
   ```

3. **Create a New Branch:**

   ```bash
   git checkout -b feature/YourFeatureName
   ```

4. **Make Changes and Commit:**

   ```bash
   git commit -m "Add your message"
   ```

5. **Push to Your Fork:**

   ```bash
   git push origin feature/YourFeatureName
   ```

6. **Create a Pull Request:**

   Navigate to the original repository and create a pull request from your fork.

## License

This project is licensed under the [MIT License](LICENSE).

---

© 2024 Naeem Goraya. All rights reserved.