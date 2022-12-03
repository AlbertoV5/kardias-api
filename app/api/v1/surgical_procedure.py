from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import fastapi

from app.db.setup import get_db
from app.admin.auth import get_api_key
from app.crud.surgical_procedure import get_surgical_procedure_records

from app.admin.schemas import UserData
from app.models.api_schemas import SurgicalProcedureRequest
from app.models.db_schemas import SurgicalProcedure

router = fastapi.APIRouter()


@router.post("/", response_model=list[SurgicalProcedure], status_code=200)
async def read_records(
    request: SurgicalProcedureRequest, db: AsyncSession = Depends(get_db)
):
    """Get a list of records by ids."""
    result = await get_surgical_procedure_records(request, db)
    return result
