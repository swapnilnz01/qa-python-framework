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
        browser_type = ConfigReader.get_browser()
        headless = ConfigReader.is_headless()
        browser = getattr(p, browser_type).launch(headless=headless)
        yield browser
        browser.close()


@pytest.fixture()
def page(browser):
    context = browser.new_context(
        base_url=ConfigReader.get_ui_base_url()
    )
    page = context.new_page()
    page.set_default_timeout(ConfigReader.get_timeout())
    yield page
    page.close()
    context.close()