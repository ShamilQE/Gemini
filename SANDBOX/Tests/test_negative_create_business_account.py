from selenium import webdriver
from Tests.base_test import BaseTest
from Pages.LoginPage import LoginPage
from Pages.RegistrationPage import RegistrationPage
from Pages.BusinessRegPage import BusinessRegPage
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Test_CreateBusinessAccount_Negative(BaseTest):

    """ TEST DATA """
    BUSINESS_REG_PAGE_TITLE = '[Sandbox] Gemini - Institutional Client Registration'
    SUCCESSFUL_PAGE_TEXT = "Thanks for Registering!"
    BUSINESS_FIELD_ALERT = "Legal Business Name is required."
    COMPANY_FIELD_ALERT = "Company type is required."
    FIRST_NAME_ALERT = "First name is required."
    LAST_NAME_ALERT = "Last name is required."
    EMAIL_ALERT = "Please enter a valid email address."
    EMAIL_DOMAIN_ALERT = "Please specify a valid email domain."
    STATE_ALERT = "Company state is required."
    CHECKBOX_ALERT = "User Agreement is required."
    BUSINESS_NAME = (By.NAME, "company.legalName")
  
    def test_negative_missing_all_fields(self):
        self.lp = LoginPage(self.driver)
        self.lp.click_create_new_account_link()
        self.rp = RegistrationPage(self.driver)
        self.rp.click_cookies_ok()
        self.rp.click_create_business_account()
        self.brp = BusinessRegPage(self.driver)
        self.brp.click_continue_button()
        alerts = self.brp.get_alerts_text()
        print (alerts)
        assert self.brp.is_visible(self.brp.REQUIRED_ALERTS)
        
    def test_negative_missing_business_name(self):
        self.driver.refresh()
        self.brp = BusinessRegPage(self.driver)
        self.brp.complete_registration_form()
        self.brp.do_check_checkbox()
        self.brp.delete_business_text()
        self.brp.click_continue_button()
        business_alert = self.brp.get_alerts_text()
        assert self.BUSINESS_FIELD_ALERT == business_alert
    
    def test_negative_missing_first_name(self):
        self.driver.refresh()
        self.brp = BusinessRegPage(self.driver)
        self.brp.complete_registration_form()
        self.brp.do_check_checkbox()
        self.brp.delete_first_name_text()
        self.brp.click_continue_button()
        first_name_alert = self.brp.get_alerts_text()
        assert self.FIRST_NAME_ALERT == first_name_alert
        
    def test_negative_missing_last_name_name(self):
        self.driver.refresh()
        self.brp = BusinessRegPage(self.driver)
        self.brp.complete_registration_form()
        self.brp.do_check_checkbox()
        self.brp.delete_last_name_text()
        self.brp.click_continue_button()
        last_name_alert = self.brp.get_alerts_text()
        assert self.LAST_NAME_ALERT == last_name_alert

    def test_negative_missing_email(self):
        self.driver.refresh()
        self.brp = BusinessRegPage(self.driver)
        self.brp.complete_registration_form()
        self.brp.do_check_checkbox()
        self.brp.delete_email_text()
        self.brp.click_continue_button()
        email_alert = self.brp.get_alerts_text()
        assert self.EMAIL_ALERT == email_alert
        self.driver.refresh()

    def test_negative_invalid_email(self):
        self.driver.refresh()
        self.brp = BusinessRegPage(self.driver)
        self.brp.complete_registration_form()
        self.brp.do_check_checkbox()
        self.brp.delete_email_text()
        self.brp.enter_invalid_email()
        self.brp.click_continue_button()
        email_alert = self.brp.get_alerts_text()
        assert self.EMAIL_DOMAIN_ALERT == email_alert
        self.driver.refresh()

    def test_negative_unchecked_checkbox(self):
        self.driver.refresh()
        self.brp = BusinessRegPage(self.driver)
        self.brp.complete_registration_form()
        self.brp.do_check_checkbox()
        self.brp.uncheck_checkbox()
        self.brp.click_continue_button()
        checkbox_alert = self.brp.get_alerts_text()
        assert self.CHECKBOX_ALERT == checkbox_alert
        self.driver.refresh()