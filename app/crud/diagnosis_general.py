from sqlalchemy.ext.asyncio import AsyncSession, AsyncScalarResult
from sqlalchemy.future import select
from sqlalchemy.sql import Select

from app.models.api_schemas import DiagnosisGeneralRequest
from app.models.db_schemas import DiagnosisGeneral
from app.models.db_models import DiagnosisGeneralDB


async def get_diagnosis_general_records(
    request: DiagnosisGeneralRequest, db: AsyncSession
) -> list[DiagnosisGeneral]:
    """Get all records that match the request."""
    # Setup
    offset = request.amount * request.page
    limit = request.amount
    data = request.columns
    # Select
    sel: Select = select(DiagnosisGeneralDB)
    sel = (
        sel.where(DiagnosisGeneralDB.diagnosis_general.in_(data.diagnosis_general))
        if len(data.diagnosis_general) != 0
        else sel
    )
    # Query
    result: AsyncScalarResult = await db.scalars(sel.offset(offset).limit(limit))
    return result.all()
