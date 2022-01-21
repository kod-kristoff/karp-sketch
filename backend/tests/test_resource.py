import pytest

from httpx import AsyncClient
from fastapi import FastAPI

from starlette import status


class TestResourcesRoutes:
    @pytest.mark.asyncio
    async def test_routes_exist(self, app: FastAPI, client: AsyncClient) -> None:
        res = await client.post(app.url_path_for("resources:create-resource"), json={})
        assert res.status_code != status.HTTP_404_NOT_FOUND

    @pytest.mark.asyncio
    async def test_invalid_input_raises_error(self, app: FastAPI, client: AsyncClient) -> None:
        res = await client.post(app.url_path_for("resources:create-resource"), json={})
        assert res.status_code != status.HTTP_422_UNPROCESSABLE_ENTITY

