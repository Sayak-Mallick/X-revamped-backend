from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.core.config import settings

SQLALCHEMY_DATABASE_URL = settings.async_database_url

# Create the async engine
async_engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10,
    hide_parameters=True,
)

# Create the async session maker
AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
)


# Dependency to get the async session
@asynccontextmanager
async def db_session() -> AsyncIterator[AsyncSession]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise

# Utility functions to close the database and check the connection
async def close_db() -> None:
    await async_engine.dispose()

# Utility function to check the database connection 
async def check_db_connection() -> None:
    async with async_engine.connect() as conn:
        await conn.execute(text("SELECT 1"))

# Dependency to get the async session
async def get_async_db() -> AsyncIterator[AsyncSession]:
    async with db_session() as session:
        yield session
