import unittest

from selenium import webdriver

from models.ShopTester import ShopTester


class Test_Search_Results(unittest.TestCase):
    def test_can_open_home_page(self):
        driver = webdriver.Chrome()
        shop = ShopTester(driver)

        home_page = shop.load_home_page()


if __name__ == "__main__":
    unittest.main()
