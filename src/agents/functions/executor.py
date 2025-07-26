import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # Load your Gemini API key from .env

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def execute(prompt):
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(prompt)
    return response.text
