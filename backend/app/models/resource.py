from enum import Enum
from typing import Any, Dict
from uuid import UUID

from app.models.core import IdModelMixin, CoreModel, TimestampMixin, VersionMixin


class ResourceOp(str, Enum):
    ADDED = "ADDED"
    UPDATED = "UPDATED"
    DELETED = "DELETED"


class ResourceBase(CoreModel):
    resource_id: str
    name: str
    config: Dict[str, Any]
    message: str
    entry_repo_id: UUID
    op: ResourceOp = ResourceOp.ADDED,
    is_published: bool = False,


class ResourceCreate(
    IdModelMixin,
    TimestampMixin,
    ResourceBase
):
    version: int = 1


class ResourceInDB(
    IdModelMixin,
    TimestampMixin,
    VersionMixin,
    ResourceBase
):
    history_id: int

class ResourcePublic(
    IdModelMixin,
    TimestampMixin,
    VersionMixin,
    ResourceBase,
):
    pass
