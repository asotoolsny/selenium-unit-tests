import unittest
import time
from selenium import webdriver

from models.ShopTester import ShopTester


class Test_Search_Results(unittest.TestCase):
    # this code is working but actions are lightning fast.
    # you can enter a debug mode to see slow motion how it happens
    def test_can_search(self):
        driver = webdriver.Chrome()
        shop = ShopTester(driver)
        shop.search_and_submit("pants")
        time.sleep(5)

    def test_can_find_sidebar_in_search_results_page(self):
        driver = webdriver.Chrome()
        shop = ShopTester(driver)

        search_page = shop.search_and_submit("pants")
        section_links = search_page.section_links_search_results

        self.assertIsNotNone(section_links)


if __name__ == "__main__":
    unittest.main()
