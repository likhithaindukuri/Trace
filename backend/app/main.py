from fastapi import FastAPI
from app.main import app
app = FastAPI(
    title="Trace - AI Engineering Work Documentation Assistant",
    description="Backend API for automated engineering work documentation generation.",
    version="0.1.0",
)


@app.get("/api/health")
def health_check():
    """Health check endpoint to verify that the API server is active and running."""
    return {
        "status": "ok",
        "message": "AI Engineering Work Documentation Assistant API is running",
    }
