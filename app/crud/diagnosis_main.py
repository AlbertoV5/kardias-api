from sqlalchemy.ext.asyncio import AsyncSession, AsyncScalarResult
from sqlalchemy.future import select
from sqlalchemy.sql import Select

from app.models.api_schemas import DiagnosisMainRequest
from app.models.db_schemas import DiagnosisMain
from app.models.db_models import DiagnosisMainDB


async def get_diagnosis_main_records(
    request: DiagnosisMainRequest, db: AsyncSession
) -> list[DiagnosisMain]:
    """Get all records that match the request."""
    # Setup
    offset = request.amount * request.page
    limit = request.amount
    data = request.columns
    # Select
    sel: Select = select(DiagnosisMainDB)
    sel = (
        sel.where(DiagnosisMainDB.diagnosis_main.in_(data.diagnosis_main))
        if len(data.diagnosis_main) != 0
        else sel
    )
    # Query
    result: AsyncScalarResult = await db.scalars(sel.offset(offset).limit(limit))
    return result.all()
