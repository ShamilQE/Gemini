from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

"""
# This class is the parent of all pages.
# It contains all the generic methods and utilities for all pages.
"""

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        
    def do_click(self, by_locator):
        self.wait.until(EC.presence_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, value):
        self.wait.until(EC.visibility_of_element_located(by_locator)).send_keys(value)

    def get_element_text(self, by_locator):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        return element.get_attribute("innerText")

    def find_element(self, by_locator):
        element = self.driver.find_element(by_locator)
        return element

    def is_visible(self, by_locator):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def is_present(self, by_locator):
        element = self.wait.until(EC.presence_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        self.wait.until(EC.title_is(title))
        return self.driver.title

    def clear_field(self, by_locator):
        field = self.wait.until(EC.visibility_of_element_located(by_locator))
        field.clear()

    def clear_entire_text(self, by_locator):
        field = self.get_element_by_visibility(by_locator)
        field.send_keys(Keys.COMMAND + "a")
        field.send_keys(Keys.BACKSPACE)

    def get_loaded_page_url(self):
        url = self.driver.current_url
        return url

    def goto_back_page(self):
        self.driver.back()

    def get_element_by_visibility(self, by_locator):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        return element

    def select_dropdown(self, by_locator):
        dropdown = Select(self.get_element_by_visibility(by_locator))
        return dropdown

        