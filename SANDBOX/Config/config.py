import os
from dotenv import load_dotenv
from selenium import webdriver

class ConfigSetUp:

    load_dotenv() # take environment variables from .env file

    TEST_URL = str(os.getenv('URL'))
    USERNAME = str(os.getenv('EMAIL_ADDRESS'))
    PASSWORD = str(os.getenv('PASSWORD'))
