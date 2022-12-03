from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import fastapi

from app.db.setup import get_db
from app.admin.auth import get_api_key
from app.crud.appearance import get_appearance_records

from app.admin.schemas import UserData
from app.models.api_schemas import AppearanceRequest
from app.models.db_schemas import Appearance

router = fastapi.APIRouter()


@router.post("/", response_model=list[Appearance], status_code=200)
async def read_records(request: AppearanceRequest, db: AsyncSession = Depends(get_db)):
    """Get a list of records by ids."""
    result = await get_appearance_records(request, db)
    return result
