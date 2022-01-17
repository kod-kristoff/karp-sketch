from fastapi import APIRouter

from app.api.routes import resources


router = APIRouter()

router.include_router(resources.router, prefix="/resources", tags=["resources"])
