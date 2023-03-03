from unittest.mock import AsyncMock, patch

import pytest
from fastapi.testclient import TestClient
from main import app

from api import (
    SERVICE_STATUS_PATH
)


def test_get_status_api():
    with TestClient(app) as client:
        response = client.get(SERVICE_STATUS_PATH)
    assert response.status_code == 200
    assert response.json() == {"message": "Backend service is available"}
