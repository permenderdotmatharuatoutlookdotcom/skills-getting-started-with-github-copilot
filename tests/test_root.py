import pytest


def test_root_redirect(client):
    # Arrange: TestClient fixture is provided by `client` fixture

    # Act
    resp = client.get("/", follow_redirects=False)

    # Assert
    assert resp.status_code == 307
    assert resp.headers.get("location") == "/static/index.html"
