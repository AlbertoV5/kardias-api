from fastapi import Depends, HTTPException, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
import fastapi

from app.db.setup import get_db
from app.models.db_models import CleanDB
from app.models.db_schemas import Clean
from app.models.api_schemas import CleanRequestID
from app.crud.generic import (
    upsert_all,
    delete_all,
    get_ordered,
    get_by_ids,
)


router = fastapi.APIRouter()


@router.get("/", response_model=list[Clean], status_code=200)
async def read_records_by_page(
    amount: int = 20,
    page: int = 0,
    db: AsyncSession = Depends(get_db),
):
    """Get a list of records by page."""
    result = await get_ordered(db, CleanDB, page * amount, amount)
    return result.all()


@router.post("/", response_model=list[Clean], status_code=200)
async def read_records_by_id(
    request: CleanRequestID,
    db: AsyncSession = Depends(get_db),
):
    """Get a list of records by ids."""
    result = await get_by_ids(db, CleanDB, set(request.patient_id))
    if result is None:
        raise HTTPException(404, "No Records were found.")
    return result.all()


@router.put("/", status_code=201)
async def create_or_update_records(
    clean_data: list[Clean],
    db: AsyncSession = Depends(get_db),
):
    """Update or Insert multiple records."""
    await upsert_all(db, CleanDB, clean_data)
    return {"Upsert": "OK"}


@router.delete("/", status_code=204)
async def delete_records(
    request: CleanRequestID,
    db: AsyncSession = Depends(get_db),
):
    """Delete multiple records."""
    await delete_all(db, CleanDB, set(request.patient_id))
