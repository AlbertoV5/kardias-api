from fastapi import Depends, APIRouter
from app.admin.auth import get_auth_tier_1, get_auth_tier_2
from app.api.v1 import (
    appearance,
    clean,
    patient,
    origin,
    diagnosis_general,
    diagnosis_main,
    storage,
    surgical_procedure,
    patient_appearance,
    patient_diagnosis_general,
    patient_diagnosis_main,
    patient_origin,
    patient_surgical_procedure
)

router = APIRouter()

# PATIENT DATA ROUTERS
router.include_router(
    patient.router, 
    prefix="/patient",
    tags=["Patient"],
    dependencies=[Depends(get_auth_tier_1)],
)
router.include_router(
    patient_appearance.router,
    prefix="/patient_appearance",
    tags=["Patient"],
    dependencies=[Depends(get_auth_tier_1)],
)
router.include_router(
    patient_origin.router,
    prefix="/patient_origin",
    tags=["Patient"],
    dependencies=[Depends(get_auth_tier_1)],
)
router.include_router(
    patient_diagnosis_main.router,
    prefix="/patient_diagnosis_main",
    tags=["Patient"],
    dependencies=[Depends(get_auth_tier_1)],
)
router.include_router(
    patient_diagnosis_general.router,
    prefix="/patient_diagnosis_general",
    tags=["Patient"],
    dependencies=[Depends(get_auth_tier_1)],

)
router.include_router(
    patient_surgical_procedure.router,
    prefix="/patient_surgical_procedure",
    tags=["Patient"],
    dependencies=[Depends(get_auth_tier_1)],
)
# MEDICAL DATA ROUTES
router.include_router(
    origin.router,
    prefix="/origin",
    tags=["Origin"],
    dependencies=[Depends(get_auth_tier_1)],
)
router.include_router(
    appearance.router,
    prefix="/appearance",
    tags=["Appearance"],
    dependencies=[Depends(get_auth_tier_1)],
)
router.include_router(
    diagnosis_main.router,
    prefix="/diagnosis_main",
    tags=["Diagnosis Main"],
    dependencies=[Depends(get_auth_tier_1)],
)
router.include_router(
    diagnosis_general.router,
    prefix="/diagnosis_general",
    tags=["Diagnosis General"],
    dependencies=[Depends(get_auth_tier_1)],
)
router.include_router(
    surgical_procedure.router,
    prefix="/surgical_procedure",
    tags=["Surgical Procedure"],
    dependencies=[Depends(get_auth_tier_1)],
)
router.include_router(
    clean.router,
    prefix="/clean",
    tags=["ETL"],
    dependencies=[Depends(get_auth_tier_2)],
)
router.include_router(
    storage.router,
    prefix="/storage",
    tags=["ETL"],
    dependencies=[Depends(get_auth_tier_2)],
)
