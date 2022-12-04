from sqlalchemy.ext.asyncio import AsyncSession, AsyncScalarResult, AsyncResult
from sqlalchemy.future import select
from sqlalchemy.sql import Select, label, text, func, desc

from app.models.api_schemas import OriginRequest, StateCount
from app.models.db_schemas import Origin
from app.models.db_models import OriginDB, PatientOriginDB


async def get_origin_records(request: OriginRequest, db: AsyncSession) -> list[Origin]:
    """Get all records that match the request."""
    # Setup
    offset = request.amount * request.page
    limit = request.amount
    data = request.columns
    # Select
    sel: Select = select(OriginDB)
    sel = sel.where(OriginDB.altitude.between(data.altitude.min, data.altitude.max))
    sel = (
        sel.where(OriginDB.municipality.in_(data.municipality))
        if len(data.municipality) != 0
        else sel
    )
    sel = sel.where(OriginDB.state.in_(data.state)) if len(data.state) != 0 else sel
    # Query
    result: AsyncScalarResult = await db.scalars(sel.offset(offset).limit(limit))
    return result.all()


async def get_state_count(
    offset: int, limit: int, db: AsyncSession
) -> list[StateCount]:
    """Get a list of surgical procedures and their count."""
    sel = (
        select(OriginDB.state, label("count", func.count(PatientOriginDB.patient_id)))
        .join(PatientOriginDB, PatientOriginDB.token == OriginDB.token)
        .group_by(OriginDB.state)
        .order_by(desc(text("count")))
    )
    result: AsyncResult = await db.execute(sel.offset(offset).limit(limit))
    return result.all()
