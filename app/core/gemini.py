import google.generativeai as genai
from app.core.config import Settings

genai.configure(api_key=Settings().gemini_api_key)

def get_gemini_model(model_name: str = "gemini-1.5-flash"):
    return genai.GenerativeModel(model_name)

def analyze_code(prompt: str)-> str:
    model = get_gemini_model()
    response = model.generate_content(prompt)
    return response.text