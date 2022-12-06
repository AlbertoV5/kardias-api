from fastapi import FastAPI
from mangum import Mangum
from starlette.middleware.cors import CORSMiddleware
import uvicorn

from app.db.setup import async_engine
from app import api


app = FastAPI(
    title="Kardias REST API",
    description="Medical Records Data Analytics",
    version="0.1.0",
    # openapi_prefix="/dev"
)

async_engine.begin()
app.include_router(api.v1.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Kardias"}

handler = Mangum(app)

if __name__ == "__main__":
    uvicorn.run(app)
