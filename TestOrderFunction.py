import unittest
from selenium import webdriver
from locators import MainPageLocators
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

    def test_order_single_product(self):
        main_page = page.MainPage(self.driver)
        products = []
        main_page.click_add_to_cart(products)
        assert "Product successfully added" in self.driver.page_source

        #continue to process the step 1
        self.driver.implicitly_wait(10)
        main_page.click_proceed_to_checkout()
        assert "step_current  first" in self.driver.page_source
        elements = self.driver.find_elements(*MainPageLocators.QTY)
        total_qty = 0
        for element in elements:
            total_qty = total_qty + int(element.get_attribute("value"))
        assert total_qty == 1

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

    def test_order_multiple_products(self):
        main_page = page.MainPage(self.driver)
        products = []

        #add multiple products
        for x in xrange(0,3):
            main_page.click_add_to_cart(products)
            self.driver.implicitly_wait(10)
            if x==2:
                main_page.click_proceed_to_checkout()
            else:
                main_page.click_continue_shopping()
            self.driver.implicitly_wait(10)

        #continue to process the step 1
        assert "step_current  first" in self.driver.page_source
        elements = self.driver.find_elements(*MainPageLocators.QTY)
        total_qty = 0
        for element in elements:
            total_qty = total_qty + int(element.get_attribute("value"))
        assert total_qty == 3

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