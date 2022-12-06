from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import fastapi

from app.db.setup import get_db
from app.crud.diagnosis_general import get_diagnosis_general_records
from app.crud.generic import get_count_list
from app.crud.generic import upsert_all
from app.admin.auth import get_api_key

from app.admin.models import User
from app.models.api_schemas import DiagnosisGeneralRequest, DiagnosisGeneralCount
from app.models.db_schemas import DiagnosisGeneral
from app.models.db_models import DiagnosisGeneralDB, PatientDiagnosisGeneralDB

router = fastapi.APIRouter()


@router.post("/", response_model=list[DiagnosisGeneral], status_code=200)
async def read_records(
    request: DiagnosisGeneralRequest, db: AsyncSession = Depends(get_db)
):
    """Get a list of records by ids."""
    result = await get_diagnosis_general_records(request, db)
    return result


@router.get("/list", response_model=list[DiagnosisGeneralCount], status_code=200)
async def read_value_counts(
    offset: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)
):
    """Get a list of records with count"""
    result = await get_count_list(
        offset,
        limit,
        PatientDiagnosisGeneralDB,
        DiagnosisGeneralDB,
        [DiagnosisGeneralDB.diagnosis_general],
        db,
    )
    return result


@router.put("/", status_code=201)
async def create_or_update_records(
    clean_data: list[DiagnosisGeneral],
    db: AsyncSession = Depends(get_db),
    user_data: User = Depends(get_api_key),
):
    """Update or Insert multiple records."""
    await upsert_all(db, DiagnosisGeneralDB, clean_data)
    return {"Upsert": "OK"}
