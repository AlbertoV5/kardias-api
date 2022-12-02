from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from mangum import Mangum

from app.db.setup import async_engine


# SETUP
app = FastAPI(
    title="Kardias REST API",
    description="Read and process medical records.",
    version="0.1.0"
)
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
async_engine.begin()

@app.get("/")
async def main():
    return {"hello": "Kardias"}

handler = Mangum(app)
