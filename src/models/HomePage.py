from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .WebDriverContainer import WebDriverContainer


class HomePageModel(WebDriverContainer):
    __page_container_selector = (By.CLASS_NAME, "navigation")
    # removed > a as it was not selecting all 7 navigation buttons. For some reason it was skipping men and women buttons
    __link_selector = (By.CSS_SELECTOR, "li.level0.ui-menu-item")

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def section_links(self):
        page_container = self.try_find_element(
            self.__page_container_selector, 20)

        links = self.try_find_elements_of(
            page_container, self.__link_selector, 20)

        return links


class HomePage(WebDriverContainer):
    def __init__(self, driver):
        super().__init__(driver)
        self.__page__ = HomePageModel(driver)

    @property
    def section_links(self):
        """will return link web elements of sections."""
        return self.__page__.section_links


class SearchResultsModel(WebDriverContainer):
    __side_bar_container_selector = (By.CSS_SELECTOR, "div.sidebar.sidebar-additional")

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def section_links_search_results(self):
        side_bar_container_locator = self.try_find_elements(
            self.__side_bar_container_selector, 20)

        return side_bar_container_locator

class SearchResults(WebDriverContainer):
    def __init__(self, driver):
        super().__init__(driver)
        self.__page__ = SearchResultsModel(driver)

    @property
    def section_links_search_results(self):
        """Will return web elements of search section"""
        return self.__page__.section_links_search_results
