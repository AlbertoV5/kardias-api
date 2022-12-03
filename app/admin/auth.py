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


async def get_api_key(
    api_key_header: str = Security(api_key_header), db: AsyncSession = Depends(get_db)
) -> UserData:
    """Check if API key is in database, return UserData if it is, either raise 403."""
    salt = os.environ["kardias_db_salt"]
    if api_key_header is not None:
        user = await find_user_key(
            db,
            blake2b(
                api_key_header.encode("utf-8"), salt=salt.encode("utf-8")
            ).hexdigest(),
        )
        if user is not None:
            return UserData(id=user.id, username=user.username, tier=user.tier)
    raise HTTPException(
        status_code=HTTP_403_FORBIDDEN, detail="Could not validate access token"
    )
