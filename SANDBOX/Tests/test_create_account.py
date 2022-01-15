from Tests.base_test import BaseTest
from Pages.RegistrationPage import RegistrationPage
from Pages.LoginPage import LoginPage
import time

class Test_CreateAccount(BaseTest):

    """ TEST DATA """
    REG_PAGE_TITLE = "[Sandbox] Gemini - Register"
    BUSINESS_REG_PAGE_URL = "https://exchange.sandbox.gemini.com/register/institution"    

    def test_reg_page_title(self):
        self.lp = LoginPage(self.driver)
        self.lp.click_create_new_account_link()
        self.rp = RegistrationPage(self.driver)
        title = self.rp.get_reg_page_title(self.REG_PAGE_TITLE)
        assert title == self.REG_PAGE_TITLE
        self.rp.goto_back_page()
        
    def test_goto_create_bus_account(self):
        self.lp = LoginPage(self.driver)
        self.lp.click_create_new_account_link()
        self.rp = RegistrationPage(self.driver)
        self.rp.click_cookies_ok()
        self.rp.click_create_business_account()
        bus_reg_url = self.rp.get_loaded_page_url()
        assert self.BUSINESS_REG_PAGE_URL == bus_reg_url
        print ("Expected URL: " + bus_reg_url)  

        


