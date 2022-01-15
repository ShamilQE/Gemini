from Tests.base_test import BaseTest
from Pages.LoginPage import LoginPage
from Pages.RegistrationPage import RegistrationPage
from Pages.BusinessRegPage import BusinessRegPage
import time

class Test_CreateBusinessAccount_Positive(BaseTest):

    """ TEST DATA """
    BUSINESS_REG_PAGE_TITLE = '[Sandbox] Gemini - Institutional Client Registration'
    SUCCESSFUL_PAGE_TEXT = "Thanks for Registering!"

    def test_positive_create_business_account(self):
        self.lp = LoginPage(self.driver)
        self.lp.click_create_new_account_link()
        self.rp = RegistrationPage(self.driver)
        self.rp.click_cookies_ok()
        self.rp.click_create_business_account()
        self.brp = BusinessRegPage(self.driver)
        self.brp.complete_registration_form()
        self.brp.do_check_checkbox()
        time.sleep(2)
        self.brp.click_continue_button()
        successful_registration_text = self.brp.get_success_reg_text()
        print (successful_registration_text)
        assert self.SUCCESSFUL_PAGE_TEXT in successful_registration_text

    
        