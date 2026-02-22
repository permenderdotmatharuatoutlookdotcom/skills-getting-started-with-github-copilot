import pytest


def test_get_activities(client):
    # Arrange: nothing to prepare beyond the fixture

    # Act
    resp = client.get("/activities")

    # Assert
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    # ensure a known activity is present
    assert "Chess Club" in data
