from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import fastapi

from app.db.setup import get_db
from app.crud.generic import upsert_all
from app.admin.auth import get_auth_tier_2
from app.crud.patient import get_patient_extra

from app.admin.models import User
from app.models.db_schemas import PatientOrigin
from app.models.db_models import PatientOriginDB, OriginDB
from app.models.api_schemas import PatientOriginResponse, PatientRequestByID

router = fastapi.APIRouter()


@router.post("/", response_model=list[PatientOriginResponse], status_code=200)
async def read_records(request: PatientRequestByID, db: AsyncSession = Depends(get_db)):
    """Get a list of records by ids."""
    result = await get_patient_extra(
        request,
        PatientOriginDB,
        OriginDB,
        [
            PatientOriginDB.patient_id,
            OriginDB.state,
            OriginDB.municipality,
            OriginDB.altitude,
        ],
        db,
    )
    if len(result) == 0:
        raise HTTPException(404, "No patients were found.")
    return result


@router.put("/", status_code=201)
async def create_or_update_records(
    clean_data: list[PatientOrigin],
    db: AsyncSession = Depends(get_db),
    user_data: User = Depends(get_auth_tier_2),
):
    """Update or Insert multiple records."""
    await upsert_all(db, PatientOriginDB, clean_data)
    return {"Upsert": "OK"}
