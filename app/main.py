from fastapi import FastAPI

from app.database.database import Base, engine

import app.models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Secure Procurement Platform",
    version="1.0.0"
)


@app.get("/")
async def root():
    return {"message": "API running"}


@app.get("/health")
async def health():
    return {"status": "healthy"}