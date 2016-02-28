import unittest
from selenium import webdriver
import page

class TestSearchFunction(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://automationpractice.com")

    def test_search_with_invalid_data(self):
        """
        Tests search function with invalid data.
        Confirm that the page source will contain 'No Results were found'.
        """
        main_page = page.MainPage(self.driver)
        main_page.search_text_element = "test invalid data"
        main_page.click_go_button()
        assert "No results were found" in self.driver.page_source

    def test_search_with_valid_data(self):
        """
        Tests search function with valid data.
        Confirm that the page source will NOT contain 'No Results were found'.
        """
        main_page = page.MainPage(self.driver)
        main_page.search_text_element = "t-shirt"
        main_page.click_go_button()
        assert "No results were found" not in self.driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()