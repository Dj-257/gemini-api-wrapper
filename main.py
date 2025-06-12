from fastapi import FastAPI
from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

gemini_api_key=os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=gemini_api_key)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Just another Gemini API wrapper"}

@app.get("/gemini")
def read_root(item: str):
    response = client.models.generate_content(
    model="gemini-2.5-flash-preview-04-17",
    contents=item,
)
    return response.text
