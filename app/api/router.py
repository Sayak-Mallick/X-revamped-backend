from fastapi import APIRouter

from app.api.endpoints.health_routes import router as health_router

app_router = APIRouter()

app_router.include_router(health_router, prefix="/health", tags=["health"])
