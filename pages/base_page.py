from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Remote as RemoteWebDriver
import pytest
from selenium.common.exceptions import NoSuchElementException


class BasePage:

    def __init__(self, driver: RemoteWebDriver, link, timeout=10):
        self.driver = driver
        self.link = link
        self.driver.implicitly_wait(timeout)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def open(self):
        self.driver.get(self.link)
