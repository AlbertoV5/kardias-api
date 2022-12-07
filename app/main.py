from fastapi import FastAPI
from mangum import Mangum
from starlette.middleware.cors import CORSMiddleware
import uvicorn

from app.db.setup import async_engine
from app import api

with open("app/README.md", "r") as readme:
    description = readme.read()

app = FastAPI(
    title="Kardias REST API",
    description=description,
    version="0.2.0",
    root_path="/dev",
    docs_url="/docs",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async_engine.begin()
app.include_router(api.v1.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"Hello": "Kardias"}

handler = Mangum(app)

if __name__ == "__main__":
    uvicorn.run(app)
