# Visual AI Assistant

A modern web application that leverages Google's Gemini 1.5 Flash model to analyze images and answer questions about them. The application features a beautiful, responsive UI with a gradient design and glassmorphism effects.

## Features

- 🖼️ Image upload with preview
- 💬 Natural language questions about images
- 🤖 Powered by Google's Gemini 1.5 Flash model
- 🎨 Modern UI with gradient background and glassmorphism
- 📱 Fully responsive design

## Tech Stack

### Frontend
- React + Vite
- Tailwind CSS for styling
- Axios for API calls

### Backend
- FastAPI
- Google Generative AI (Gemini 1.5 Flash)
- Python Image Library (PIL)
- Python-dotenv for environment variables

## UI Screenshot

![Application Interface](Screenshot%202025-06-27%20170427.png)

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

4. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

## How to Use

1. Open the application in your browser
2. Upload an image using the drag-and-drop interface or file browser
3. Type your question about the image in the input field
4. Click "Ask AI" to get the response
5. View the AI's analysis in the response panel

## API Endpoint

The backend exposes a single endpoint:

- `POST /api/ask`
  - Accepts multipart form data with:
    - `file`: The image file
    - `question`: The question about the image
  - Returns JSON with either:
    - `{"answer": "AI response text"}` or
    - `{"error": "Error message"}`

## Note

Make sure to obtain a Gemini API key from Google AI Studio to use this application. The API key should be kept secure and not committed to version control.
