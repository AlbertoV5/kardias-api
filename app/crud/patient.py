from sqlalchemy.ext.asyncio import AsyncSession, AsyncScalarResult
from sqlalchemy.future import select
from sqlalchemy.sql import Select

from app.models.api_schemas import PatientRequest
from app.models.db_schemas import Patient
from app.models.db_models import PatientDB


async def get_patient_records(
    request: PatientRequest, db: AsyncSession
) -> list[Patient]:
    """Get all patient records that match the request."""
    # Setup
    offset = request.amount * request.page
    limit = request.amount
    data = request.columns
    # Select
    sel: Select = select(PatientDB)
    for key, value in data.dict().items():
        sel = sel.where(PatientDB.__table__.c[key].between(value["min"], value["max"]))
    # Query
    result: AsyncScalarResult = await db.scalars(sel.offset(offset).limit(limit))
    return result.all()
