import pytest
from ui.pages.home_page import HomePage
from utils.logger import get_logger

log = get_logger(__name__)

@pytest.fixture()
def home(page):
    home = HomePage(page)
    home.navigate()
    return home

def test_page_title(home):
    log.info("Testing page title")
    title = home.get_title()
    assert "Books to Scrape" in title
    log.info(f"Title verified: {title}")

def test_books_displayed(home):
    log.info("Testing books are displayed on home page")
    count = home.get_book_count()
    assert count == 20
    log.info(f"Found {count} books on home page")

def test_book_titles_not_empty(home):
    log.info("Testing book titles are not empty")
    titles = home.get_book_titles()
    assert len(titles) > 0
    for title in titles:
        assert title.strip() != ""
    log.info(f"Verified {len(titles)} book titles")

def test_next_page_exists(home):
    log.info("Testing next page button exists")
    next_btn = home.get_next_page_button()
    assert next_btn.is_visible()
    log.info("Next page button found")

def test_navigate_to_category(home):
    log.info("Testing category navigation")
    home.search_category("Mystery")
    title = home.page.title()
    assert "Mystery" in title
    log.info("Category navigation passed")