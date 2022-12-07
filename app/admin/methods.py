"""
Logic for querying the api keys table.
"""
from typing import Optional
from sqlalchemy.sql import func
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession, AsyncScalarResult

from app.admin.models import User


async def find_user_key(db: AsyncSession, key: str, tier: int) -> Optional[User]:
    """Get key from database if any."""
    count: AsyncScalarResult = await db.scalar(
        select(func.count(User.id)).where(User.key == key).where(User.tier >= tier)
    )
    if count == 0:
        return None
    return await db.scalar(select(User).where(User.key == key))
