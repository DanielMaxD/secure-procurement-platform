from fastapi import FastAPI

from app.database.database import Base, engine
from app.api.auth import router as auth_router

import app.models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Secure Procurement Platform",
    version="1.0.0"
)

app.include_router(auth_router)

@app.get("/")
async def root():
    return {"message": "API running"}


@app.get("/health")
async def health():
    return {"status": "healthy"}