from app.db.repositories.base import BaseRepository
from app.models.resource import ResourceCreate, ResourceInDB


CREATE_RESOURCE_QUERY = """
    INSERT INTO resources (
        history_id,
        entity_id,
        resource_id,
        resource_type,
        entry_repo_id,
        version,
        name,
        config,
        is_published,
        last_modified,
        last_modified_by,
        message,
        op,
        discarded)
    VALUES (
        :history_id,
        :entity_id,
        :resource_id,
        :resource_type,
        :entry_repo_id,
        :version,
        :name,
        :config,
        :is_published,
        :last_modified,
        :last_modified_by,
        :message,
        :op,
        :discarded)
    RETURNING
        history_id,
        entity_id,
        resource_id,
        resource_type,
        entry_repo_id,
        version,
        name,
        config,
        is_published,
        last_modified,
        last_modified_by,
        message,
        op,
        discarded;

"""


class ResourceRepository(BaseRepository):
    async def create_resource(self, *, new_resource: ResourceCreate) -> ResourceInDB:
        query_values = new_resource.dict()
        resource = await self.db.fetch_one(query=CREATE_RESOURCE_QUERY, values=query_values)
        return ResourceInDB(**resource)
