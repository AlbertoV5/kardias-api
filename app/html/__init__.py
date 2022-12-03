from fastapi import APIRouter
from app.html import home


router = APIRouter()

router.include_router(home.router, tags=["HTML"])
