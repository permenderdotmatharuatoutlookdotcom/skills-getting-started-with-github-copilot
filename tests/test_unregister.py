import pytest
from urllib.parse import quote


def test_unregister_success(client):
    # Arrange: pick an existing participant from seeded data
    email = "michael@mergington.edu"
    path = f"/activities/{quote('Chess Club')}/signup"

    # Act: perform delete
    resp = client.delete(path, params={"email": email})

    # Assert
    assert resp.status_code == 200
    assert "Unregistered" in resp.json().get("message", "")

    # Act: get activities
    resp2 = client.get("/activities")
    # Assert removed from list
    assert email not in resp2.json()["Chess Club"]["participants"]
