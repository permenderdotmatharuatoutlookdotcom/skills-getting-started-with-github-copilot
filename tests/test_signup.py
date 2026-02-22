import pytest
from urllib.parse import quote


def test_signup_success(client):
    email = "testuser@example.com"
    path = f"/activities/{quote('Chess Club')}/signup"
    resp = client.post(path, params={"email": email})
    assert resp.status_code == 200
    assert "Signed up" in resp.json().get("message", "")

    # verify participant appears in activity
    resp2 = client.get("/activities")
    assert email in resp2.json()["Chess Club"]["participants"]


def test_signup_duplicate_error(client):
    email = "dup@example.com"
    path = f"/activities/{quote('Chess Club')}/signup"
    r1 = client.post(path, params={"email": email})
    assert r1.status_code == 200

    r2 = client.post(path, params={"email": email})
    assert r2.status_code == 400
    assert r2.json().get("detail") == "Student already signed up"
