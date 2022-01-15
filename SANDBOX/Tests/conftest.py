import pytest
from selenium import webdriver
from Config.config import ConfigSetUp
from Pages.LoginPage import LoginPage
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

"""
Pytest fixture to initialize driver and run tests in different browsers.
* Add to params=["chrome", "firefox", "edge"] to run tests in desired browser
"""

@pytest.fixture(params=["chrome"], scope="class")
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    if request.param == "edge":
        web_driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    request.cls.driver = web_driver
    try:
        web_driver.maximize_window()
        web_driver.get(ConfigSetUp.TEST_URL)
                
        yield
    finally:
        web_driver.quit()
