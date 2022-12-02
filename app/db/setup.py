"""
This file creates a database engine and will yield an async session
everytime the asyc_get_db function is called from FastAPI as a Dependency.

We will use the environment variables to load the path to the database.
"""
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

# NullPool: https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html#using-multiple-asyncio-event-loops

from config import DB_PATH


ASYNC_SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{DB_PATH}"
async_engine = create_async_engine(
    ASYNC_SQLALCHEMY_DATABASE_URL,
    # poolclass=NullPool,
    pool_size=10,
    max_overflow=20,
)
AsyncSessionLocal = sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
Base = declarative_base()
"""Declarative Base. Include metadata schema."""
Base.metadata.schema = "public"


async def get_db() -> AsyncSession:
    """Yields a database session."""
    async with AsyncSessionLocal() as db:
        yield db
        await db.commit()
