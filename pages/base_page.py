"""This module describes Basic page methods (Page object)."""
from selenium.webdriver import Remote as RemoteWebDriver
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    """Contains Basic page methods for pages (Page object)"""
    def __init__(self, driver: RemoteWebDriver, link, timeout=10):
        self.driver = driver
        self.link = link
        self.driver.implicitly_wait(timeout)

    def is_element_present(self, how, what) -> bool:
        """Return True, if element is presented on the screen. Otherwise - False"""
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def open(self):
        self.driver.get(self.link)
