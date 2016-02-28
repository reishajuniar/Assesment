from element import BasePageElementByName
from locators import MainPageLocators

class SearchTextElementByName(BasePageElementByName):
    locator = 'search_query'

class EmailLoginElementByName(BasePageElementByName):
    locator = 'email'

class PasswordLoginElementByName(BasePageElementByName):
    locator = 'passwd'

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    search_text_element = SearchTextElementByName()
    email_login_element = EmailLoginElementByName()
    password_login_element = PasswordLoginElementByName()

    def is_title_matches(self):
        return "My Store" in self.driver.title

    def click_go_button(self):
        """Triggers the search"""
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

    def click_add_to_cart(self):
        elements = self.driver.find_elements(*MainPageLocators.ADD_PRODUCT)
        for element in elements:
            if element.is_enabled():
                element.click()
                break

    def click_proceed_to_checkout(self):
        element = self.driver.find_element(*MainPageLocators.CHECKOUT_ORDER)
        element.click()

    def click_sign_in(self):
        element = self.driver.find_element(*MainPageLocators.GO_SIGNIN)
        element.click()

    def click_login_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_LOGIN)
        element.click()

    def click_process_address(self):
        element = self.driver.find_element(*MainPageLocators.PROCESS_ADDRESS)
        element.click()

    def click_term_of_service(self):
        element = self.driver.find_element(*MainPageLocators.TERM_OF_SERVICE_CBX)
        element.click()

    def click_process_delivery(self):
        element = self.driver.find_element(*MainPageLocators.DELIVER_GOODS)
        element.click()

    def click_bank_wire(self):
        element = self.driver.find_element(*MainPageLocators.BANK_WIRE)
        element.click()

    def click_confirm_order(self):
        element = self.driver.find_element(*MainPageLocators.CONFIRM_ORDER)
        element.click()
