import unittest

from selenium import webdriver

from models.ShopTester import ShopTester


class Test_HomePage(unittest.TestCase):
    def test_can_open_home_page(self):
        driver = webdriver.Chrome()
        shop = ShopTester(driver)

        home_page = shop.load_home_page()

    def test_can_find_header_menus_on_home_page(self):
        driver = webdriver.Chrome()
        shop = ShopTester(driver)

        home_page = shop.load_home_page()
        section_links = home_page.section_links

        self.assertIsNotNone(section_links)


if __name__ == "__main__":
    unittest.main()
