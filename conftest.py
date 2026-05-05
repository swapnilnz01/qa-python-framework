import pytest
from playwright.sync_api import sync_playwright
from utils.config_reader import ConfigReader

from api.client import APIClient

# --- API fixture ---
@pytest.fixture()
def api_client():
    return APIClient()



@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser_type = ConfigReader.get("BROWSER")
        headless = ConfigReader.get("headless", "true").lower() == "true"
        browser = getattr(p, browser_type).launch(headless=headless)
        yield browser
        browser.close()


@pytest.fixture()
def page(browser):
    context = browser.new_context(
        base_url=ConfigReader.get("UI_BASE_URL")
    )
    page = context.new_page()
    page.set_default_timeout(int(ConfigReader.get("timeout", "30000")))
    yield page
    page.close()
    context.close()