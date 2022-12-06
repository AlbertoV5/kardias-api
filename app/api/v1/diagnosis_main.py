from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import fastapi

from app.db.setup import get_db
from app.crud.diagnosis_main import get_diagnosis_main_records
from app.crud.generic import get_count_list
from app.crud.generic import upsert_all


from app.models.api_schemas import DiagnosisMainRequest, DiagnosisMainCount
from app.models.db_schemas import DiagnosisMain
from app.models.db_models import DiagnosisMainDB, PatientDiagnosisMainDB

router = fastapi.APIRouter()


@router.post("/", response_model=list[DiagnosisMain], status_code=200)
async def read_records(
    request: DiagnosisMainRequest, db: AsyncSession = Depends(get_db)
):
    """Get a list of records by ids."""
    result = await get_diagnosis_main_records(request, db)
    return result


@router.get("/list", response_model=list[DiagnosisMainCount], status_code=200)
async def read_value_counts(
    offset: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)
):
    """Get a list of records with count"""
    result = await get_count_list(
        offset,
        limit,
        PatientDiagnosisMainDB,
        DiagnosisMainDB,
        [DiagnosisMainDB.diagnosis_main],
        db,
    )
    return result


@router.put("/", status_code=201)
async def create_or_update_records(
    clean_data: list[DiagnosisMain],
    db: AsyncSession = Depends(get_db),
):
    """Update or Insert multiple records."""
    await upsert_all(db, DiagnosisMainDB, clean_data)
    return {"Upsert": "OK"}
