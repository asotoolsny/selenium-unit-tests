from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .HomePage import HomePage, SearchResults
from .WebDriverContainer import WebDriverContainer


class ShopTester(WebDriverContainer):
    _home_page_url = "http://demo-acm-2.bird.eu/"
    _search_textbox_selector = (By.NAME, "q")

    def __init__(self, driver):
        super().__init__(driver)

    def load_home_page(self):
        self.load_url(self._home_page_url)
        return HomePage(self._driver)

    def search_and_submit(self, query):
        """Loads home page, finds search box, types a query and hits enter"""
        self.load_url(self._home_page_url)
        self.keyboard_type_submit(self._search_textbox_selector, query)
        return SearchResults(self._driver)

