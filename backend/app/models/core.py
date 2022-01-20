import uuid
from pydantic import BaseModel


class CoreModel(BaseModel):
    pass


class IdModelMixin(BaseModel):
    entity_id: uuid.UUID


class VersionMixin(BaseModel):
    version: int


class TimestampMixin(BaseModel):
    last_modified: float
    last_modified_by: str
