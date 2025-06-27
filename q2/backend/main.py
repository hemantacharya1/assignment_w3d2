from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image
import os
import io

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/ask")
async def ask_question(file: UploadFile = File(...), question: str = Form(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes))

    try:
        response = model.generate_content([question, image])
        return {"answer": response.text}
    except Exception as e:
        return {"error": str(e)}
