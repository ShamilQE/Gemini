from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage
from Pages.RegistrationPage import RegistrationPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class BusinessRegPage(BasePage):

    """ TEST DATA"""
    VALID_BUSINESS_NAME = "Sandbox"
    VALID_FIRST_NAME = "Michael"
    VALID_MIDDLE_NAME = "J"
    VALID_LAST_NAME = "Johnson"
    VALID_EMAIL = "michael.johnson@test.com"
    SUCCESSFULL_TEXT = "Thanks for Registering!"
    INVALID_EMAIL = "invalid email"
    
    """ By locators - Object Repository"""
    BUSINESS_NAME = (By.NAME, "company.legalName")
    COMPANY_TYPE = (By.XPATH, '//input[@id="companyTypeDropdown"]')
    COMPANY_OPTION = (By.XPATH, "//*[text()='Broker-Dealer']")
    COUNTRY_DROPDOWN = (By.XPATH, "//input[@id='countryDropdown']")
    COUNTRY_OPTION = (By.XPATH, ".//*[text()='United States']")
    STATE_DROPDOWN = (By.ID, "stateDropdown")
    STATE_OPTION = (By.XPATH, "//*[text()='UT']")
    FIRST_NAME = (By.NAME, "personal.legalName.firstName")
    MIDDLE_NAME = (By.NAME, "personal.legalName.middleName")
    LAST_NAME = (By.NAME, "personal.legalName.lastName")
    EMAIL = (By.NAME, "personal.email")
    CHECKBOX = (By.XPATH, '//*[contains(text(),"By submitting")]')
    CONTINUE_BUTON = (By.CSS_SELECTOR, '[data-testid="InstitutionSubmit"]')   
    SUCCESSFUL_TEXT = (By.XPATH, '//*[contains(text(),"Thanks for Registering!")]')
    SUCCESS_REGISTRATION = (By.CSS_SELECTOR, '[class="page-body SuccessPage"]')
    REQUIRED_ALERTS = (By.CSS_SELECTOR, '[class="AlertBody"]')

    """ constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)

    """ Page actions for Business Registration Page"""
    ### used to fill out all field with VALID data
    def complete_registration_form(self):
        self.do_send_keys(self.BUSINESS_NAME, self.VALID_BUSINESS_NAME)
        self.do_click(self.COMPANY_TYPE)
        self.do_click(self.COMPANY_OPTION)
        if self.is_visible(self.COUNTRY_OPTION):
            pass
        else:
            self.do_click(self.COUNTRY_DROPDOWN)
            self.do_click(self.COUNTRY_OPTION)            
        self.do_click(self.STATE_DROPDOWN)
        self.do_click(self.STATE_OPTION)       
        self.do_send_keys(self.FIRST_NAME, self.VALID_FIRST_NAME)
        self.do_send_keys(self.MIDDLE_NAME, self.VALID_MIDDLE_NAME)
        self.do_send_keys(self.LAST_NAME, self.VALID_LAST_NAME)
        self.do_send_keys(self.EMAIL, self.VALID_EMAIL)
    
    # used to click checkbox
    def do_check_checkbox(self):
        self.do_click(self.CHECKBOX)        

    # used to click "Continue" button
    def click_continue_button(self):    
        self.do_click(self.CONTINUE_BUTON)

    # used to get successful registration text
    def get_success_reg_text(self):
        text = self.get_element_text(self.SUCCESS_REGISTRATION)
        return text

    # used to get Alerts text
    def get_alerts_text(self):
        alerts = self.get_element_text(self.REQUIRED_ALERTS)
        return alerts

    # used to go back to Registration Page
    def goback_to_reg_page(self):
        self.driver.execute_script("window.history.go(-1)")
        
    # used to delete entire text in "Legal Business Name" field
    def delete_business_text(self):
        self.clear_entire_text(self.BUSINESS_NAME)

    # used to delete entire text in "Legal First Name" field
    def delete_first_name_text(self):
        self.clear_entire_text(self.FIRST_NAME)

    # used to delete entire text in "Legal Last Name" field
    def delete_last_name_text(self):
        self.clear_entire_text(self.LAST_NAME)

    # used to delete entire text in "Your Email Address" field
    def delete_email_text(self):
        self.clear_entire_text(self.EMAIL)

    # used to uncheck the checkbox
    def uncheck_checkbox(self):
        self.do_click(self.CHECKBOX)

    # used to enter invalid in "Your Email Address" field
    def enter_invalid_email(self):
        self.do_send_keys(self.EMAIL, self.INVALID_EMAIL)