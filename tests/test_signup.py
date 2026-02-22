import pytest
from urllib.parse import quote


def test_signup_success(client):
    # Arrange
    email = "testuser@example.com"
    path = f"/activities/{quote('Chess Club')}/signup"

    # Act
    resp = client.post(path, params={"email": email})

    # Assert
    assert resp.status_code == 200
    assert "Signed up" in resp.json().get("message", "")

    # Arrange/Act: fetch activities to verify state
    resp2 = client.get("/activities")
    # Assert
    assert email in resp2.json()["Chess Club"]["participants"]


def test_signup_duplicate_error(client):
    # Arrange
    email = "dup@example.com"
    path = f"/activities/{quote('Chess Club')}/signup"

    # Act: first signup
    r1 = client.post(path, params={"email": email})
    # Assert first succeeded
    assert r1.status_code == 200

    # Act: duplicate signup
    r2 = client.post(path, params={"email": email})

    # Assert: duplicate returns 400 with message
    assert r2.status_code == 400
    assert r2.json().get("detail") == "Student already signed up"
