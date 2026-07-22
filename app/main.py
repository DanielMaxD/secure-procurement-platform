from fastapi import FastAPI

app = FastAPI(
    title="Secure Procurement Platform",
    description="A secure sealed-bid procurement platform",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {
        "message": "Secure Procurement Platform API is running!"
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }