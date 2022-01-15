from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class RegistrationPage(BasePage):

    """ TEST DATA"""
    PAGE_TEXT = "Create an account"
    
    """ By locators - Object Repository"""
    CREATE_BUSINESS_ACC = (By.XPATH, '//*[contains(text(), "Create a business account")]')
    COOKIES_OK_BUTTON = (By.CSS_SELECTOR, '[data-testid="cookiePolicyAgreement-close"]')

    """ constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)

    """ Page actions for RegistrationPage"""
    def get_reg_page_title(self, title):
        return self.get_title(title)

    # used to click "Create a business account" link
    def click_create_business_account(self):
        self.do_click(self.CREATE_BUSINESS_ACC)
        return RegistrationPage(self.driver)

    # used to click "OK" button for cookies popup
    def click_cookies_ok(self):
        if self.is_visible(self.COOKIES_OK_BUTTON):
            self.do_click(self.COOKIES_OK_BUTTON)
        else:
            pass

    # used to go back to previous page
    def goback_to_previous_page(self):
        self.driver.execute_script("window.history.go(-1)")
     

    
        
        


