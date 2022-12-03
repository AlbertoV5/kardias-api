"""
Logic for querying the api keys table.
"""
from typing import Optional
from sqlalchemy.sql import func
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession, AsyncScalarResult

from app.admin.models import ApiKeys


async def find_api_key(db: AsyncSession, key: str) -> Optional[ApiKeys]:
    """Get key from database if any."""
    count: AsyncScalarResult = await db.scalar(
        select(func.count(ApiKeys.id)).where(ApiKeys.key == key)
    )
    if count == 0:
        return None
    return await db.scalar(select(ApiKeys).where(ApiKeys.key == key))
