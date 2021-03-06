"""This module describes Basic feedback form methods."""
from selenium.webdriver import Remote as RemoteWebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from imap_tools import MailBox
import settings
from .locators import MainPageLocators

class BaseForm:
    """This class describes Basic feedback forms methods (Page object)"""
    def __init__(self, link, driver: RemoteWebDriver, timeout=10):
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

    def accept_cookie(self) -> None:
        """Finds "allow" button on cookie alert and click on it."""
        self.driver.find_element(
            By.CSS_SELECTOR,
            MainPageLocators.COOKIE_ALLOW_BUTTON,
        ).click()

    def get_email(self, name_id: str) -> bool:
        """Returns True, if email body contains correct
        "name_id" value. Error string, if email body doesn't.
        """
        with MailBox("outlook.office365.com").login(
                settings.Const.IMAP_USER, settings.Const.IMAP_PASSWORD
        ) as mailbox:

            for message in mailbox.fetch(limit=1, reverse=True):

                email_body = message.text

                if name_id not in email_body:

                    return False

                return True

    def open(self):
        self.driver.get(self.link)

    @staticmethod
    def clean_email_folder() -> None:
        """Delete all email messages in outlook folder (clean up)."""
        with MailBox("outlook.office365.com").login(
                settings.Const.IMAP_USER, settings.Const.IMAP_PASSWORD
        ) as mailbox:
            mailbox.delete([msg.uid for msg in mailbox.fetch()])