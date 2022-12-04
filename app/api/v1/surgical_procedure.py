from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import fastapi

from app.db.setup import get_db
from app.crud.surgical_procedure import get_surgical_procedure_records
from app.crud.generic import get_count_list

from app.models.api_schemas import SurgicalProcedureRequest, SurgicalProcedureCount
from app.models.db_schemas import SurgicalProcedure
from app.models.db_models import SurgicalProcedureDB, PatientSurgicalProcedureDB


router = fastapi.APIRouter()


@router.post("/", response_model=list[SurgicalProcedure], status_code=200)
async def read_records(
    request: SurgicalProcedureRequest, db: AsyncSession = Depends(get_db)
):
    """Get a list of records by ids."""
    result = await get_surgical_procedure_records(request, db)
    return result


@router.get("/", response_model=list[SurgicalProcedureCount], status_code=200)
async def read_counts(
    offset: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)
):
    """Get a list of records with count"""
    result = await get_count_list(
        offset,
        limit,
        PatientSurgicalProcedureDB,
        SurgicalProcedureDB,
        [SurgicalProcedureDB.surgical_procedure],
        db,
    )
    return result
