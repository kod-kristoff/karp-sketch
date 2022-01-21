from typing import Dict, List

from fastapi import APIRouter, Body, Depends
from starlette import status

from app.models.resource import ResourceCreate, ResourcePublic
from app.db.repositories.resources import ResourceRepository
from app.api.dependencies.database import get_repository


router = APIRouter()


@router.get("/")
async def get_all_resources() -> List[Dict]:
    resources = [
        {"id": "uuid-5-8", "resource_id": "saldo"},
    ]

    return resources


@router.post(
    "/",
    response_model=ResourcePublic,
    name="resources:create-resource",
    status_code=status.HTTP_201_CREATED,
)
async def create_new_resource(
    new_resource: ResourceCreate = Body(...),
    resource_repo: ResourceRepository = Depends(get_repository(ResourceRepository)),
)-> ResourcePublic:
    created_resource = await resource_repo.create_resource(new_resource=new_resource)

    return created_resource
