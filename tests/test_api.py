from httpx import AsyncClient
import pytest
import logging

from app.models.db_schemas import Clean
from pydantic import BaseModel
import os

from app import app


log = logging.getLogger(__name__)
KEY = os.environ["kardias_api_key"]


class RecordsList(BaseModel):
    records: list[Clean]


@pytest.mark.asyncio
async def test_read_records():
    async with AsyncClient(app=app, base_url="http://test_1") as ac:

        URL = "/api/v1"
        headers = {"access_token": KEY}
        # Perform GET
        AMOUNT = 5
        PAGE = 0
        response = await ac.get(
            f"{URL}/clean/?amount={AMOUNT}&page={PAGE}", headers=headers
        )
        assert response.status_code == 200
        response_a = RecordsList(records=response.json())

        # Perform POST
        POST_DATA = {"patient_id": [record.patient_id for record in response_a.records]}
        response = await ac.post(f"{URL}/clean/", json=POST_DATA, headers=headers)
        assert response.status_code == 200
        response_b = RecordsList(records=response.json())

        # Compare Responses using Pydantic's __eq__
        assert response_a == response_b
