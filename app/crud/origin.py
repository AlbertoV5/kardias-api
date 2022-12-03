from sqlalchemy.ext.asyncio import AsyncSession, AsyncScalarResult
from sqlalchemy.future import select
from sqlalchemy.sql import Select

from app.models.api_schemas import OriginRequest
from app.models.db_schemas import Origin
from app.models.db_models import OriginDB


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
