from Tests.base_test import BaseTest
from Pages.LoginPage import LoginPage
from Pages.RegistrationPage import RegistrationPage


class Test_LoginPage(BaseTest):
    
    """ TEST DATA"""
    LOGIN_PAGE_TITLE = '[Sandbox] Gemini - Sign In'
    REG_PAGE_URL = 'https://exchange.sandbox.gemini.com/register'
    
    def test_login_page_title(self):
        self.lp = LoginPage(self.driver)
        title = self.lp.get_login_page_title(self.LOGIN_PAGE_TITLE)
        assert title == self.LOGIN_PAGE_TITLE

    def test_goto_create_new_account(self):
        self.lp = LoginPage(self.driver)
        self.lp.click_create_new_account_link()
        reg_url = self.lp.get_loaded_page_url()
        assert reg_url == self.REG_PAGE_URL
        print ("Expected URL: " + reg_url)
        

        



        



        


    