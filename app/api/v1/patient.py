from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import fastapi

from app.db.setup import get_db
from app.crud.patient import get_patient_records
from app.crud.generic import upsert_all
from app.admin.auth import get_api_key

from app.admin.models import User
from app.models.api_schemas import PatientRequest
from app.models.db_schemas import Patient
from app.models.db_models import PatientDB

router = fastapi.APIRouter()


@router.post("/", response_model=list[Patient], status_code=200)
async def read_records(request: PatientRequest, db: AsyncSession = Depends(get_db)):
    """Get a list of records by ids."""
    result = await get_patient_records(request, db)
    return result


@router.put("/", status_code=201)
async def create_or_update_records(
    clean_data: list[Patient],
    db: AsyncSession = Depends(get_db),
    user_data: User = Depends(get_api_key),
):
    """Update or Insert multiple records."""
    await upsert_all(db, PatientDB, clean_data)
    return {"Upsert": "OK"}
