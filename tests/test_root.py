import pytest


def test_root_redirect(client):
    resp = client.get("/", follow_redirects=False)
    assert resp.status_code == 307
    assert resp.headers.get("location") == "/static/index.html"
