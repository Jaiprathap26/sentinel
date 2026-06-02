import google.generativeai as genai
from app.core.config import settings

genai.configure(api_key=settings.gemini_api_key)

def get_gemini_model(model_name: str = "gemini-1.5-flash"):
    return genai.GenerativeModel(model_name)

async def analyze_code(prompt: str)-> str:
    model = get_gemini_model()
    response = await model.generate_content_async(prompt)
    return response.text