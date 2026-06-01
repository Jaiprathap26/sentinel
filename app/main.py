from fastapi import FastAPI

app = FastAPI(
    title="SENTINEL",
    description="AI-powered software engineering intelligence platform",
    version="0.1.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "SENTINEL"}
