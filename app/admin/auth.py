"""
Authentication with API key dependency.
Storing the API keys in the database hashed with salt.
"""
from fastapi.security.api_key import APIKeyHeader
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Security, HTTPException, Depends
from starlette.status import HTTP_403_FORBIDDEN
from hashlib import blake2b
import os

from app.db.setup import get_db
from app.admin.methods import find_user_key

from app.admin.schemas import UserData


api_key_header = APIKeyHeader(name="access_token", auto_error=False)

USER_TIER_1 = 1
USER_TIER_2 = 2
SALT = os.environ["kardias_db_salt"]


async def get_auth_tier_1(
    api_key_header: str = Security(api_key_header), db: AsyncSession = Depends(get_db)
) -> UserData:
    """Check if API key is in database, return UserData if it is, either raise 403."""
    if api_key_header is not None:
        k = blake2b(api_key_header.encode("utf-8"), salt=SALT.encode("utf-8")).hexdigest()
        user = await find_user_key(db, k)
        if user is not None and user.tier == USER_TIER_1:
            return UserData(id=user.id, username=user.username, tier=user.tier)
    raise HTTPException(
        status_code=HTTP_403_FORBIDDEN, detail="Could not validate access token"
    )


async def get_auth_tier_2(
    api_key_header: str = Security(api_key_header), db: AsyncSession = Depends(get_db)
) -> UserData:
    """"""
    if api_key_header is not None:
        k = blake2b(api_key_header.encode("utf-8"), salt=SALT.encode("utf-8")).hexdigest()
        user = await find_user_key(db, k)
        if user is not None and user.tier == USER_TIER_2:
            return UserData(id=user.id, username=user.username, tier=user.tier)
    raise HTTPException(
        status_code=HTTP_403_FORBIDDEN, detail="Could not validate access token"
    )
