import pytest
from game.server import app


@pytest.fixture
def client():
    return app.test_client()
