from fastapi import APIRouter
from sqlalchemy import text

from app.db.database import async_engine

router = APIRouter()


@router.get("/")
async def health_check():
    return {"status": "ok"}


@router.get("/db")
async def db_health_check():
    async with async_engine.connect() as conn:
        await conn.execute(text("SELECT 1"))
        return {"status": "ok", "database": "PostgreSQL Connection OK"}
