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

# origins = [
#     "http://localhost",
#     "http://localhost:8080",
#     "http://localhost:3000",
#     "http://127.0.0.1:5500",
# ]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

async_engine.begin()
app.include_router(api.v1.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"Hello": "Kardias"}

handler = Mangum(app)

if __name__ == "__main__":
    uvicorn.run(app)
