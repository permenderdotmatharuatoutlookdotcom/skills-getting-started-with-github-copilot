import pytest
from copy import deepcopy
from src import app as app_module
from fastapi.testclient import TestClient


# Snapshot the initial activities once so tests can restore state
INITIAL_ACTIVITIES = deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities():
    """Restore the in-memory activities before each test."""
    app_module.activities = deepcopy(INITIAL_ACTIVITIES)
    yield


@pytest.fixture
def client():
    """Synchronous TestClient bound to the FastAPI app."""
    with TestClient(app_module.app) as c:
        yield c
