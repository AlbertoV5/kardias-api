from fastapi import Depends, APIRouter
from app.admin.auth import get_api_key
from app.api.v1 import (
    appearance,
    clean,
    patient,
    origin,
    diagnosis_general,
    diagnosis_main,
    surgical_procedure,
)

router = APIRouter()

router.include_router(
    patient.router, 
    prefix="/patient",
    tags=["Read"]
)
router.include_router(
    origin.router, 
    prefix="/origin",
    tags=["Read"],
)
router.include_router(
    appearance.router, 
    prefix="/appearance",
    tags=["Read"],
)
router.include_router(
    diagnosis_general.router, 
    prefix="/diagnosis_general",
    tags=["Read"],
)
router.include_router(
    diagnosis_main.router, 
    prefix="/diagnosis_main",
    tags=["Read"],
)
router.include_router(
    surgical_procedure.router, 
    prefix="/surgical_procedure",
    tags=["Read"],
)
router.include_router(
    clean.router, 
    prefix="/clean",
    tags=["ETL"],
    dependencies=[Depends(get_api_key)],
)