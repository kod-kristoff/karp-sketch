from enum import Enum
from typing import Any, Dict, Optional
from uuid import UUID

from app.models.core import EntityOpMixin, IdModelMixin, CoreModel, TimestampMixin, VersionMixin


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
    is_published: Optional[bool]
    resource_type: Optional[str] = "resource"


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
    EntityOpMixin,
    ResourceBase
):
    history_id: int


class ResourcePublic(
    IdModelMixin,
    TimestampMixin,
    VersionMixin,
    EntityOpMixin,
    ResourceBase,
):
    pass
