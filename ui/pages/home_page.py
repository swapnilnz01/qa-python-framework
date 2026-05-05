from utils.config_reader import ConfigReader


class HomePage:

    def __init__(self, page):
        self.page = page
        self.url = ConfigReader.get_ui_base_url()

    def navigate(self):
        self.page.goto(self.url)

    def get_title(self):
        return self.page.title()

    def get_all_books(self):
        return self.page.locator("article.product_pod").all()

    def get_book_titles(self):
        books = self.page.locator("article.product_pod h3 a")
        return books.all_inner_texts()

    def get_book_count(self):
        return self.page.locator("article.product_pod").count()

    def search_category(self, category):
        self.page.locator(f"a:has-text('{category}')").first.click()
        self.page.wait_for_load_state("networkidle")

    def get_next_page_button(self):
        return self.page.locator("li.next a")

    def go_to_next_page(self):
        self.get_next_page_button().click()
        self.page.wait_for_load_state("networkidle")