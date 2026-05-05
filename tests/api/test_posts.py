from utils.config_reader import ConfigReader
from utils.logger import get_logger

log = get_logger(__name__)
POSTS = ConfigReader.get("posts_endpoint")

def test_get_all_posts(api_client):
    log.info("Testing GET /posts")
    response = api_client.get(POSTS)
    assert response.status_code == 200
    assert len(response.json()) == 100

def test_get_single_post(api_client):
    log.info("Testing GET /posts/1")
    response = api_client.get(f"{POSTS}/1")
    data = response.json()
    assert response.status_code == 200
    assert data["id"] == 1

def test_create_post(api_client):
    payload = {
        "title": "My Test Post",
        "body": "This is a test",
        "userId": 1
    }
    response = api_client.post(POSTS, payload)
    assert response.status_code == 201
    assert response.json()["title"] == "My Test Post"