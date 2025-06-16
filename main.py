from fastapi import FastAPI
from dotenv import load_dotenv
from google import genai
from google.genai import types
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

@app.get("/gemini-image")
def read_root_image(item: str, image: str):

    with open(f'./{image}.jpg', 'rb') as f:
      image_bytes = f.read()

    response = client.models.generate_content(
    model="gemini-2.5-flash-preview-04-17",
    contents=[
      types.Part.from_bytes(
        data=image_bytes,
        mime_type='image/jpeg',
      ),
      item
    ]
  )
    return response.text