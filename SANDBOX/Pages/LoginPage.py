from selenium import webdriver
from Pages.BasePage import BasePage
from Pages.RegistrationPage import RegistrationPage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    """ TEST DATA"""
    

    """ By locators - Object Repository"""
    CREATE_NEW_ACC = (By.XPATH, "//*[contains(text(), 'Create new account')]")


    """ constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)

    """ Page actions for LoginPage"""
    # used to get LoginPage title
    def get_login_page_title(self, title):
        return self.get_title(title)

    # used to click on "Creat new account" link
    def click_create_new_account_link(self):
        self.do_click(self.CREATE_NEW_ACC)
        return RegistrationPage(self.driver)

    

