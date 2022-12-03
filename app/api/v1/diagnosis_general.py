from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import fastapi

from app.db.setup import get_db
from app.admin.auth import get_api_key
from app.crud.diagnosis_general import get_diagnosis_general_records

from app.admin.schemas import UserData
from app.models.api_schemas import DiagnosisGeneralRequest
from app.models.db_schemas import DiagnosisGeneral

router = fastapi.APIRouter()


@router.post("/", response_model=list[DiagnosisGeneral], status_code=200)
async def read_records(
    request: DiagnosisGeneralRequest, db: AsyncSession = Depends(get_db)
):
    """Get a list of records by ids."""
    result = await get_diagnosis_general_records(request, db)
    return result
