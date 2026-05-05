import pytest

import api.client
from utils.logger import get_logger

log = get_logger(__name__)

def test_get_all_posts(api_client):
    log.info("Testing GET /posts")
    response = api_client.get("/posts")
    log.debug(f"Status code: {response.status_code}")
    assert response.status_code == 200
    assert len(response.json()) == 100
    log.info("PASSED - got 100 posts")

def test_get_single_post(api_client):
    response = api_client.get("/posts/1")
    assert response.status_code == 200
    data = response.json()
    print(data)

    assert data["id"] == 1
    assert "title" in data
    assert "body" in data

def test_create_post(api_client):
    payload = {
        "tile": "my first post",
        "body": "my test body",
        "userid": 1
    }
    response = api_client.post("/posts", payload)
    data = response.json()
    print(data)

    assert response.status_code == 201
    assert data["tile"] == "my first post"
    assert "id" in data

@pytest.mark.parametrize("post_id, expected_status", [
    (1,   200),
    (50,  200),
    (100, 200),
    (999, 404),   # non-existent post
])
def test_get_post_by_id(api_client, post_id, expected_status):
    log.info(f"Testing GET /posts/{post_id}")
    response = api_client.get(f"/posts/{post_id}")

    log.debug(f"Status: {response.status_code}")
    assert response.status_code == expected_status