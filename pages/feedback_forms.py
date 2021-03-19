"""This module describes methods for assertion and interaction with Feedback forms"""
import time
from imap_tools import MailBox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage
from .locators import (
    SubscribeFormLocators,
    MainPageLocators,
    WriteToUsFormLocators,
    BaseFeedbackFormLocators,
)

LINK = "https://dev.sibedge.com/clients/"

LINKS_DICT = {
    "main_page": "https://dev.sibedge.com/",
    "clients_page": "https://dev.sibedge.com/clients/",
    "models_page": "https://dev.sibedge.com/models/",
    "contacts_page": "https://dev.sibedge.com/contacts/",
    "blog_page": "https://dev.sibedge.com/blog/",
    "service_development_page": "https://dev.sibedge.com/services/development/",
    "service_extension_page": "https://dev.sibedge.com/services/team-extension/",
    "service_squads_page": "https://dev.sibedge.com/squads-product-development/",
    "service_devops_page": "https://dev.sibedge.com/devops/",
    "service_qa_page": "https://dev.sibedge.com/qa/",
    "about_us_page": "https:/dev.sibedge.com/about/",
    "agile_article": "https://dev.sibedge.com/article/agile-and-squad-services/",
    "pitfalls_article": "https://dev.sibedge.com/article/major-pitfalls/",
    "cto_article": "https://dev.sibedge.com/article/ctos-reshape-it-priorities-to-overcome-crisis-mode/",
}


def get_email(name_id: str) -> str or bool:
    """This function returns True, if email body contains correct "name_id" value
    Error string, if email body doesn't.
    """
    imap_user = "test4site@sibedge.com"
    imap_password = "Hup28813"

    with MailBox("outlook.office365.com").login(imap_user, imap_password) as mailbox:
        for message in mailbox.fetch(limit=1, reverse=True):
            email_body = message.text

            if name_id in email_body:
                return bool

            return "No 'name_id' value in email body"


class FeedBackForms(BasePage):

    def open_about_us_and_form(self):
        about_us = self.driver.find_element(
            By.CSS_SELECTOR,
            ".nav__item:nth-of-type(2) .nav__item-link",
        )
        ActionChains(self.driver).move_to_element(about_us).perform()
        self.driver.find_element(By.CSS_SELECTOR, MainPageLocators.SUBSCRIBE_TO_US_BUTTON).click()

    def accept_cookie(self):
        self.driver.find_element(
            By.CSS_SELECTOR,
            ".cookie-alert__button.cookie-alert__button--agree.js--cookie-alert-allow"
        ).click()

    def open_and_send_write_to_us_form(self):
        name_id = "TestWriteToUs"
        self.driver.find_element(By.CSS_SELECTOR, MainPageLocators.HEADER_FORM_BUTTON).click()
        self.driver.find_element(By.ID, WriteToUsFormLocators.NAME_FIELD).send_keys(name_id)
        self.driver.find_element(By.ID, WriteToUsFormLocators.EMAIL_FIELD).send_keys("testemail@email.com")
        self.driver.find_element(By.ID, WriteToUsFormLocators.PHONE_FIELD).send_keys("+79513454323")
        self.driver.find_element(By.ID, WriteToUsFormLocators.MESSAGE_FIELD).send_keys("Hello. Have a good day!")
        self.driver.find_element(By.NAME, WriteToUsFormLocators.SEND_BUTTON).click()

        thank_you_notice = self.driver.find_element(
            By.CLASS_NAME,
            WriteToUsFormLocators.THANK_YOU_NOTICE_MESSAGE,
        )

        assert thank_you_notice != 0
        time.sleep(3)
        assert bool(get_email(name_id)) is not False, f"Email have no correct id -  {name_id} in body"

    def open_and_send_subscribe_to_us_form(self):
        name_id = "TestSubscribeToUs"
        self.driver.find_element(By.ID, SubscribeFormLocators.NAME_FIELD).send_keys(name_id)
        self.driver.find_element(By.ID, SubscribeFormLocators.EMAIL_FIELD).send_keys("testemail@email.com")
        self.driver.find_element(By.ID, SubscribeFormLocators.MESSAGE_FIELD).send_keys("Hello. Have a good day!")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, SubscribeFormLocators.SEND_BUTTON).click()

        thank_you_notice = self.driver.find_element(
            By.CLASS_NAME,
            SubscribeFormLocators.THANK_YOU_NOTICE_MESSAGE,
        )

        assert thank_you_notice != 0
        time.sleep(3)
        assert bool(get_email(name_id)) is not False, f"Email have no correct id -  {name_id} in body"

    def open_and_send_main_page_form(self):
        name_id = "TestMainPage"
        self.driver.get(LINKS_DICT["main_page"])
        self.accept_cookie()
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.NAME_FIELD).send_keys(name_id)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.LAST_NAME_FIELD).send_keys("Testlastname")
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.EMAIL_FIELD).send_keys("test@email.com")
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.PHONE_FIELD).send_keys("+79994512345")
        time.sleep(1)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.SEND_BUTTON).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(3)
        assert bool(get_email(name_id)) is not False, f"Email have no correct id -  {name_id} in body"

    def open_and_send_models_page_form(self):
        name_id = "TestModelsPage"
        self.driver.get(LINKS_DICT["models_page"])
        self.accept_cookie()
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.NAME_FIELD).send_keys(name_id)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.LAST_NAME_FIELD).send_keys("Testlastname")
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.EMAIL_FIELD).send_keys("test@email.com")
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.PHONE_FIELD).send_keys("+79994512345")
        time.sleep(1)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.SEND_BUTTON).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(3)
        assert bool(get_email(name_id)) is not False, f"Email have no correct id -  {name_id} in body"

    def open_and_send_about_us_page_form(self):
        name_id = "TestAboutUs"
        self.driver.get(LINKS_DICT["about_us_page"])
        self.accept_cookie()
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.NAME_FIELD).send_keys(name_id)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.LAST_NAME_FIELD).send_keys("Testlastname")
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.EMAIL_FIELD).send_keys("test@email.com")
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.PHONE_FIELD).send_keys("+79994512345")
        time.sleep(1)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.SEND_BUTTON).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(3)
        assert bool(get_email(name_id)) is not False, f"Email have no correct id -  {name_id} in body"

    def open_and_send_contacts_page_form(self):
        name_id = "TestContacts"
        self.driver.get(LINKS_DICT["contacts_page"])
        self.accept_cookie()
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.NAME_FIELD).send_keys(name_id)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.LAST_NAME_FIELD).send_keys("Testlastname")
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.EMAIL_FIELD).send_keys("test@email.com")
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.PHONE_FIELD).send_keys("+79994512345")
        time.sleep(1)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.SEND_BUTTON).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(3)
        assert bool(get_email(name_id)) is not False, f"Email have no correct id -  {name_id} in body"

    def open_and_send_blog_page_form(self):
        name_id = "TestBlog"
        self.driver.get(LINKS_DICT["blog_page"])
        self.accept_cookie()
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.LAST_NAME_FIELD).send_keys(name_id)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.EMAIL_FIELD).send_keys("test@email.com")
        time.sleep(1)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.SEND_BUTTON).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(3)
        assert bool(get_email(name_id)) is not False, f"Email have no correct id -  {name_id} in body"

    def open_and_send_development_service_form(self):
        name_id = "TestDevelopmentService"
        self.driver.get(LINKS_DICT["service_development_page"])
        self.accept_cookie()
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.NAME_FIELD).send_keys(name_id)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.EMAIL_FIELD).send_keys("test@email.com")
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.LAST_NAME_FIELD).send_keys("Testlastname")
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.COMPANY_FIELD).send_keys("Test-Company")
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.PHONE_FIELD).send_keys("+79994512345")
        time.sleep(1)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.SEND_BUTTON).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(3)
        assert bool(get_email(name_id)) is not False, f"Email have no correct id -  {name_id} in body"

    def open_and_send_extension_service_form(self):
        name_id = "TestExtensionService"
        self.driver.get(LINKS_DICT["service_extension_page"])
        self.accept_cookie()
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.NAME_FIELD).send_keys(name_id)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.LAST_NAME_FIELD).send_keys("Testlastname")
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.EMAIL_FIELD).send_keys("test@email.com")
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.COMPANY_FIELD).send_keys("Test-Company")
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.PHONE_FIELD).send_keys("+79994512345")
        time.sleep(0.5)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.SEND_BUTTON).click()
        time.sleep(1)

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(3)
        assert bool(get_email(name_id)) is not False, f"Email have no correct id -  {name_id} in body"

    def open_and_send_squads_service_form(self):
        name_id = "TestSquadsService"
        self.driver.get(LINKS_DICT["service_squads_page"])
        self.accept_cookie()
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.NAME_FIELD).send_keys(name_id)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.EMAIL_FIELD).send_keys("test@email.com")
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.LAST_NAME_FIELD).send_keys("Testlastname")
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.COMPANY_FIELD).send_keys("Test-Company")
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.PHONE_FIELD).send_keys("+79994512345")
        time.sleep(1)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.SEND_BUTTON).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(3)
        assert bool(get_email(name_id)) is not False, f"Email have no correct id -  {name_id} in body"

    def open_and_send_devops_service_form(self):
        name_id = "TestDevopsService"
        self.driver.get(LINKS_DICT["service_devops_page"])
        self.accept_cookie()
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.NAME_FIELD).send_keys(name_id)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.LAST_NAME_FIELD).send_keys("Testlastname")
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.EMAIL_FIELD).send_keys("test@email.com")
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.COMPANY_FIELD).send_keys("Test-Company")
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.PHONE_FIELD).send_keys("+79994512345")
        time.sleep(1)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.SEND_BUTTON).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(3)
        assert bool(get_email(name_id)) is not False, f"Email have no correct id -  {name_id} in body"

    def open_and_send_qa_service_form(self):
        name_id = "TestQaService"
        self.driver.get(LINKS_DICT["service_qa_page"])
        self.accept_cookie()
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.NAME_FIELD).send_keys(name_id)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.LAST_NAME_FIELD).send_keys("Testlastname")
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.EMAIL_FIELD).send_keys("test@email.com")
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.COMPANY_FIELD).send_keys("Test-Company")
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.PHONE_FIELD).send_keys("+79994512345")
        time.sleep(1)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.SEND_BUTTON).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(3)
        assert bool(get_email(name_id)) is not False, f"Email have no correct id -  {name_id} in body"

    def open_and_send_agile_article_form(self):
        name_id = "TestAgileArticle"
        self.driver.get(LINKS_DICT["agile_article"])
        self.accept_cookie()
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.NAME_FIELD).send_keys(name_id)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.LAST_NAME_FIELD).send_keys("Testlastname")
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.EMAIL_FIELD).send_keys("test@email.com")
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.PHONE_FIELD).send_keys("+79994512345")
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.COMPANY_FIELD).send_keys("Test-Company")
        time.sleep(1)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.SEND_BUTTON).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(3)
        assert bool(get_email(name_id)) is not False, f"Email have no correct id -  {name_id} in body"

    def open_and_send_pitfalls_article_form(self):
        name_id = "TestPitfallsArticle"
        self.driver.get(LINKS_DICT["pitfalls_article"])
        self.accept_cookie()
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.NAME_FIELD).send_keys(name_id)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.LAST_NAME_FIELD).send_keys("Testlastname")
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.EMAIL_FIELD).send_keys("test@email.com")
        time.sleep(1)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.SEND_BUTTON).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(3)
        assert bool(get_email(name_id)) is not False, f"Email have no correct id -  {name_id} in body"

    def open_and_send_cto_article_form(self):
        name_id = "TestCtoArticle"
        self.driver.get(LINKS_DICT["cto_article"])
        self.accept_cookie()
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.NAME_FIELD).send_keys(name_id)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.LAST_NAME_FIELD).send_keys("Testlastname")
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.EMAIL_FIELD).send_keys("test@email.com")
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.PHONE_FIELD).send_keys("+79994512345")
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.COMPANY_FIELD).send_keys("Test-Company")
        time.sleep(1)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.SEND_BUTTON).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(3)
        assert bool(get_email(name_id)) is not False, f"Email have no correct id -  {name_id} in body"
