from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import fastapi

from app.db.setup import get_db
from app.admin.auth import get_api_key
from app.crud.patient import get_patient_records

from app.admin.schemas import UserData
from app.models.api_schemas import PatientRequest
from app.models.db_schemas import Patient

router = fastapi.APIRouter()


@router.post("/", response_model=list[Patient], status_code=200)
async def read_records(request: PatientRequest, db: AsyncSession = Depends(get_db)):
    """Get a list of records by ids."""
    result = await get_patient_records(request, db)
    return result
