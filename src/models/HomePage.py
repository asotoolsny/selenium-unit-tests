from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .WebDriverContainer import WebDriverContainer


class HomePageModel(WebDriverContainer):
    __page_container_selector = (By.CLASS_NAME, "navigation")
    __link_selector = (By.CSS_SELECTOR, "li.level0.ui-menu-item > a")

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
