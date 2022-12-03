from fastapi import APIRouter
from app.api.html import test


html_router = APIRouter()

html_router.include_router(
    test.router, 
    prefix="/test",
    tags=["HTML"]
)
