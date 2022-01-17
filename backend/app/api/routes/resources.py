from typing import Dict, List

from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def get_all_resources() -> List[Dict]:
    resources = [
        {"id": "uuid-5-8", "resource_id": "saldo"},
    ]

    return resources
