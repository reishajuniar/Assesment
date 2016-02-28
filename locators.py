from selenium.webdriver.common.by import By

class MainPageLocators(object):
    GO_BUTTON = (By.NAME , 'submit_search')
    ADD_PRODUCT = (By.LINK_TEXT ,'Add to cart')
    CHECKOUT_ORDER = (By.LINK_TEXT,'Proceed to checkout')
    GO_SIGNIN = (By.LINK_TEXT, 'Sign in')
    GO_LOGIN = (By.NAME ,'SubmitLogin')
    PROCESS_ADDRESS = (By.NAME,'processAddress')
    TERM_OF_SERVICE_CBX = (By.NAME,'cgv')
    DELIVER_GOODS = (By.NAME,'processCarrier')
    BANK_WIRE = (By.CLASS_NAME,'bankwire')
    CONFIRM_ORDER = (By.XPATH,'//p[@id="cart_navigation"]/button')
