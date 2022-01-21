
from enum import Enum
import uuid

from pydantic import BaseModel


class CoreModel(BaseModel):
    pass

class EntityOp(str, Enum):
    ADDED = "ADDED"
    UPDATED = "UPDATED"
    DELETED = "DELETED"
class EntityOpMixin(BaseModel):
    op: EntityOp


class IdModelMixin(BaseModel):
    entity_id: uuid.UUID


class VersionMixin(BaseModel):
    version: int


class TimestampMixin(BaseModel):
    last_modified: float
    last_modified_by: str
