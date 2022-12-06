from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import fastapi

from app.db.setup import get_db
from app.crud.appearance import get_appearance_records
from app.crud.generic import get_count_list
from app.crud.generic import upsert_all


from app.models.api_schemas import AppearanceRequest, AppearanceCount
from app.models.db_schemas import Appearance
from app.models.db_models import AppearanceDB, PatientAppearanceDB

router = fastapi.APIRouter()


@router.post("/", response_model=list[Appearance], status_code=200)
async def read_records(request: AppearanceRequest, db: AsyncSession = Depends(get_db)):
    """Get a list of records by ids."""
    result = await get_appearance_records(request, db)
    return result


@router.get("/list", response_model=list[AppearanceCount], status_code=200)
async def read_value_counts(
    offset: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)
):
    """Get a list of records with count"""
    result = await get_count_list(
        offset,
        limit,
        PatientAppearanceDB,
        AppearanceDB,
        [AppearanceDB.appearance],
        db,
    )
    return result


@router.put("/", status_code=201)
async def create_or_update_records(
    clean_data: list[Appearance],
    db: AsyncSession = Depends(get_db),
):
    """Update or Insert multiple records."""
    await upsert_all(db, AppearanceDB, clean_data)
    return {"Upsert": "OK"}
