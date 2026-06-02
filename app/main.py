from fastapi import FastAPI
from pydantic import BaseModel 
from app.core.gemini import analyze_code 

app = FastAPI(
    title="SENTINEL",
    description="AI-powered software engineering intelligence platform",
    version="0.1.0"
)
class AnalyzeRequest(BaseModel):
    prompt: str


@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/analyze")
async def analyze(request: AnalyzeRequest):
    result = await analyze_code(request.prompt)
    return {"result": result}
