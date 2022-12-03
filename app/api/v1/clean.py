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

from app.s3.setup import upload_csv_to_bucket
from app.config import MAX_CSV_FILE_SIZE_BYTES


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


@router.put("/uploadfile/")
async def create_upload_csv_file(file: UploadFile,):
    """Upload a CSV file to S3 bucket."""
    result = await upload_csv_to_bucket(file, MAX_CSV_FILE_SIZE_BYTES)
    if result is None:
        raise HTTPException(status_code=413, detail=f"File exceeds max size: {MAX_CSV_FILE_SIZE_BYTES} bytes.")
    return {"Upload": "OK"}


@router.delete("/", status_code=204)
async def delete_records(
    request: CleanRequestID,
    db: AsyncSession = Depends(get_db),
):
    """Delete multiple records."""
    await delete_all(db, CleanDB, set(request.patient_id))
