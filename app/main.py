from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.router import app_router
from app.core.config import settings
from app.db.database import check_db_connection, close_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await check_db_connection()
        yield
    finally:
        try:
            await close_db()
        except Exception as e:
            print(e)


app = FastAPI(
    title=settings.app_name,
    version="1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi",
    lifespan=lifespan,
)


@app.get("/", include_in_schema=False)
def read_root():
    return {"message": "X-revamped-backend", "version": "1.0.0", "status": "running"}


app.include_router(app_router)
