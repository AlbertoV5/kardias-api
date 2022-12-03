from fastapi import FastAPI
from mangum import Mangum

from starlette.middleware.cors import CORSMiddleware

from app.db.setup import async_engine
from app import html
from app import api

import uvicorn


app = FastAPI(
    title="Kardias REST API",
    description="Medical Records Database Access",
    version="0.1.0",
)
async_engine.begin()
app.include_router(html.router)
app.include_router(api.v1.router, prefix="/api/v1")

handler = Mangum(app)

# if __name__ == '__main__':
#     uvicorn.run(app)