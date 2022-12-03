from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from mangum import Mangum

from app.db.setup import async_engine
from app import html


app = FastAPI(
    title="Kardias REST API",
    description="Read and process medical records.",
    version="0.1.0"
)
async_engine.begin()
app.include_router(html.router)

handler = Mangum(app)
