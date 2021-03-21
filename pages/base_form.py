from selenium.webdriver import Remote as RemoteWebDriver
from selenium.common.exceptions import NoSuchElementException

class BaseForm:
    """This class describes Basic feedback forms methods (Page object)"""

    def __init__(self, driver: RemoteWebDriver, timeout=10):
        self.driver = driver
        self.driver.implicitly_wait(timeout)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
