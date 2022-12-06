from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import fastapi

from app.db.setup import get_db
from app.crud.origin import get_origin_records, get_state_count
from app.crud.generic import get_count_list
from app.crud.generic import upsert_all
from app.admin.auth import get_api_key

from app.admin.models import User
from app.models.api_schemas import OriginRequest, OriginCount, StateCount
from app.models.db_schemas import Origin
from app.models.db_models import PatientOriginDB, OriginDB

router = fastapi.APIRouter()


@router.post("/", response_model=list[Origin], status_code=200)
async def read_records(request: OriginRequest, db: AsyncSession = Depends(get_db)):
    """Get a list of records by ids."""
    result = await get_origin_records(request, db)
    return result


@router.get("/list", response_model=list[OriginCount], status_code=200)
async def read_value_counts(
    offset: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)
):
    """Get a list of records with count"""
    result = await get_count_list(
        offset,
        limit,
        PatientOriginDB,
        OriginDB,
        [OriginDB.state, OriginDB.municipality, OriginDB.altitude],
        db,
    )
    return result


@router.get("/state/list", response_model=list[StateCount], status_code=200)
async def read_value_counts_state(
    offset: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)
):
    """Get a list of records with count"""
    result = await get_state_count(offset, limit, db)
    return result


@router.put("/", status_code=201)
async def create_or_update_records(
    clean_data: list[Origin],
    db: AsyncSession = Depends(get_db),
    user_data: User = Depends(get_api_key),
):
    """Update or Insert multiple records."""
    await upsert_all(db, OriginDB, clean_data)
    return {"Upsert": "OK"}
