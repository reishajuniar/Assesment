import unittest
from selenium import webdriver
import page

class TestOrderFunction(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://automationpractice.com")

    def test_login_with_valid_data(self):
        main_page = page.MainPage(self.driver)
        main_page.click_sign_in()
        self.driver.implicitly_wait(10)
        #fill in the login
        main_page.email_login_element = "reisha.juniar@gmail.com"
        main_page.password_login_element = "test123"
        main_page.click_login_button()
        self.driver.implicitly_wait(10)
        assert "Welcome to your account." in self.driver.page_source

    def test_login_with_invalid_data(self):
        main_page = page.MainPage(self.driver)
        main_page.click_sign_in()
        self.driver.implicitly_wait(10)
        #fill in the login
        main_page.email_login_element = "reisha.juniar@gmail.com"
        main_page.password_login_element = "test"
        main_page.click_login_button()
        self.driver.implicitly_wait(10)
        assert "Invalid password" in self.driver.page_source

    def test_order_product(self):
        main_page = page.MainPage(self.driver)

        main_page.click_add_to_cart()
        assert "Product successfully added" in self.driver.page_source

        #continue to process the step 1
        self.driver.implicitly_wait(10)
        main_page.click_proceed_to_checkout()
        assert "step_current  first" in self.driver.page_source

        #continue to process step 2
        self.driver.implicitly_wait(10)
        main_page.click_proceed_to_checkout()
        assert "step_current second" in self.driver.page_source

        #fill in the login
        main_page.email_login_element = "reisha.juniar@gmail.com"
        main_page.password_login_element = "test123"
        main_page.click_login_button()
        self.driver.implicitly_wait(10)
        assert "step_current third" in self.driver.page_source

        #continue to process step 3
        main_page.click_process_address()
        self.driver.implicitly_wait(10)
        assert "step_current four" in self.driver.page_source

        #continue to process step 4
        main_page.click_term_of_service()
        main_page.click_process_delivery()
        self.driver.implicitly_wait(10)
        assert "step_current last" in self.driver.page_source

        #continue to payment process
        main_page.click_bank_wire()
        self.driver.implicitly_wait(10)
        assert "You have chosen to pay by bank wire" in self.driver.page_source
        main_page.click_confirm_order()
        self.driver.implicitly_wait(10)
        assert "Your order on My Store is complete." in self.driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()