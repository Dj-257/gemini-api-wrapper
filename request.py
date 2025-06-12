import requests
from dotenv import load_dotenv
import os

load_dotenv()

base_url = os.getenv("BASE_URL")

query=input("Enter your query: ")
try:
    response = requests.get(f"{base_url}/gemini", params={"item": query})
    response.raise_for_status()
    print(f"\nResponse from /gemini for '{query}':")
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f"Error making request to /gemini: {e}")