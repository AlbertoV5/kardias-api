from sqlalchemy.ext.asyncio import AsyncSession, AsyncScalarResult
from sqlalchemy.future import select
from sqlalchemy.sql import Select

from app.models.api_schemas import AppearanceRequest
from app.models.db_schemas import Appearance
from app.models.db_models import AppearanceDB


async def get_appearance_records(
    request: AppearanceRequest, db: AsyncSession
) -> list[Appearance]:
    """Get all records that match the request."""
    # Setup
    offset = request.amount * request.page
    limit = request.amount
    data = request.columns
    # Select
    sel: Select = select(AppearanceDB)
    sel = (
        sel.where(AppearanceDB.appearance.in_(data.appearance))
        if len(data.appearance) != 0
        else sel
    )
    # Query
    result: AsyncScalarResult = await db.scalars(sel.offset(offset).limit(limit))
    return result.all()
