from sqlalchemy.ext.asyncio import AsyncSession, AsyncScalarResult, AsyncResult
from sqlalchemy.future import select
from sqlalchemy.sql.expression import label
from sqlalchemy.sql import Select, func, desc, alias, text
from sqlalchemy import Column

from app.models.api_schemas import SurgicalProcedureRequest, SurgicalProcedureCount
from app.models.db_schemas import SurgicalProcedure
from app.models.db_models import SurgicalProcedureDB, PatientSurgicalProcedureDB


async def get_surgical_procedure_records(
    request: SurgicalProcedureRequest, db: AsyncSession
) -> list[SurgicalProcedure]:
    """Get all records that match the request."""
    # Setup
    offset = request.amount * request.page
    limit = request.amount
    data = request.columns
    # Select
    sel: Select = select(SurgicalProcedureDB)
    sel = (
        sel.where(SurgicalProcedureDB.surgical_procedure.in_(data.diagnosis_main))
        if len(data.surgical_procedure) != 0
        else sel
    )
    # Query
    result: AsyncScalarResult = await db.scalars(sel.offset(offset).limit(limit))
    return result.all()
