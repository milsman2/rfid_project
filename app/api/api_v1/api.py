from fastapi import APIRouter

from app.api.api_v1.routes import healthcheck, doodle

api_router = APIRouter()
api_router.include_router(healthcheck.router, prefix="/healthcheck", tags=["healthcheck"])
api_router.include_router(doodle.router, prefix="/doodle", tags=["doodle"])