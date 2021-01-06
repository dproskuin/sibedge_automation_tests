from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Remote as RemoteWebDriver
import pytest

class BasePage:

    def __init__(self, driver: RemoteWebDriver, link):
        self.driver = driver
        self.link = link

    def open(self):
        self.driver.get(self.link)
