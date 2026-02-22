import pytest
from urllib.parse import quote


def test_unregister_success(client):
    # use an existing participant from the seeded data
    email = "michael@mergington.edu"
    path = f"/activities/{quote('Chess Club')}/signup"
    resp = client.delete(path, params={"email": email})
    assert resp.status_code == 200
    assert "Unregistered" in resp.json().get("message", "")

    # verify removed
    resp2 = client.get("/activities")
    assert email not in resp2.json()["Chess Club"]["participants"]
