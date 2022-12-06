from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import fastapi

from app.db.setup import get_db
from app.crud.generic import upsert_all
from app.crud.patient import get_patient_extra
from app.admin.auth import get_api_key

from app.admin.models import User
from app.models.db_schemas import PatientAppearance
from app.models.db_models import PatientAppearanceDB, AppearanceDB
from app.models.api_schemas import PatientRequestByID, PatientAppearanceResponse

router = fastapi.APIRouter()


@router.post("/", response_model=list[PatientAppearanceResponse], status_code=200)
async def read_records(request: PatientRequestByID, db: AsyncSession = Depends(get_db)):
    """Get a list of records by ids."""
    result = await get_patient_extra(
        request, 
        PatientAppearanceDB,
        AppearanceDB,
        [PatientAppearanceDB.patient_id, AppearanceDB.appearance],
        db
    )
    if len(result) == 0:
        raise HTTPException(404, "No patients were found.")
    return result


@router.put("/", status_code=201)
async def create_or_update_records(
    clean_data: list[PatientAppearance],
    db: AsyncSession = Depends(get_db),
    user_data: User = Depends(get_api_key),
):
    """Update or Insert multiple records."""
    await upsert_all(db, PatientAppearanceDB, clean_data)
    return {"Upsert": "OK"}