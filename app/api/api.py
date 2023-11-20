from fastapi import APIRouter

from app.api.endpoints import links

api_router = APIRouter()
api_router.include_router(links.router, prefix="/api")
