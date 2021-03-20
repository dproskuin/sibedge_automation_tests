"""This module describes methods for assertion and interaction with Feedback forms"""
import time
import settings
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


def get_email(name_id: str) -> str or bool:
    """This function returns True, if email body contains correct "name_id" value
    Error string, if email body doesn't.
    """
    with MailBox("outlook.office365.com").login(settings.Const.IMAP_USER, settings.Const.IMAP_PASSWORD) as mailbox:
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

    def accept_cookie(self) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR,
            ".cookie-alert__button.cookie-alert__button--agree.js--cookie-alert-allow"
        ).click()

    def open_and_send_write_to_us_form(self):
        name_id = "TestWriteToUs"
        self.driver.get(settings.Const.CLIENTS_PAGE)
        self.driver.find_element(By.CSS_SELECTOR, MainPageLocators.HEADER_FORM_BUTTON).click()
        self.driver.find_element(By.ID, WriteToUsFormLocators.NAME_FIELD).send_keys(name_id)
        self.driver.find_element(By.ID, WriteToUsFormLocators.EMAIL_FIELD).send_keys(settings.Const.EMAIL)
        self.driver.find_element(By.ID, WriteToUsFormLocators.PHONE_FIELD).send_keys(settings.Const.PHONE)
        self.driver.find_element(By.ID, WriteToUsFormLocators.MESSAGE_FIELD).send_keys(settings.Const.MESSAGE)
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
        self.driver.get(settings.Const.CLIENTS_PAGE)
        self.driver.find_element(By.ID, SubscribeFormLocators.NAME_FIELD).send_keys(name_id)
        self.driver.find_element(By.ID, SubscribeFormLocators.EMAIL_FIELD).send_keys(settings.Const.EMAIL)
        self.driver.find_element(By.ID, SubscribeFormLocators.MESSAGE_FIELD).send_keys(settings.Const.MESSAGE)
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
        self.driver.get(settings.Const.MAIN_PAGE)
        self.accept_cookie()
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.NAME_FIELD).send_keys(name_id)
        self.driver.find_element(
            By.NAME, BaseFeedbackFormLocators.LAST_NAME_FIELD
        ).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.EMAIL_FIELD).send_keys(settings.Const.EMAIL)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.PHONE_FIELD).send_keys(settings.Const.PHONE)
        time.sleep(1)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.SEND_BUTTON).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(3)
        assert bool(get_email(name_id)) is not False, f"Email have no correct id -  {name_id} in body"

    def open_and_send_models_page_form(self):
        name_id = "TestModelsPage"
        self.driver.get(settings.Const.MODELS_PAGE)
        self.accept_cookie()
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.NAME_FIELD).send_keys(name_id)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.LAST_NAME_FIELD).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.EMAIL_FIELD).send_keys(settings.Const.EMAIL)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.PHONE_FIELD).send_keys(settings.Const.PHONE)
        time.sleep(1)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.SEND_BUTTON).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(3)
        assert bool(get_email(name_id)) is not False, f"Email have no correct id -  {name_id} in body"

    def open_and_send_about_us_page_form(self):
        name_id = "TestAboutUs"
        self.driver.get(settings.Const.ABOUT_US_PAGE)
        self.accept_cookie()
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.NAME_FIELD).send_keys(name_id)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.LAST_NAME_FIELD).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.EMAIL_FIELD).send_keys(settings.Const.EMAIL)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.PHONE_FIELD).send_keys(settings.Const.PHONE)
        time.sleep(1)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.SEND_BUTTON).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(3)
        assert bool(get_email(name_id)) is not False, f"Email have no correct id -  {name_id} in body"

    def open_and_send_contacts_page_form(self):
        name_id = "TestContacts"
        self.driver.get(settings.Const.CONTACTS_PAGE)
        self.accept_cookie()
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.NAME_FIELD).send_keys(name_id)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.LAST_NAME_FIELD).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.EMAIL_FIELD).send_keys(settings.Const.EMAIL)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.PHONE_FIELD).send_keys(settings.Const.PHONE)
        time.sleep(1)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.SEND_BUTTON).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(3)
        assert bool(get_email(name_id)) is not False, f"Email have no correct id -  {name_id} in body"

    def open_and_send_blog_page_form(self):
        name_id = "TestBlog"
        self.driver.get(settings.Const.BLOG_PAGE)
        self.accept_cookie()
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.LAST_NAME_FIELD).send_keys(name_id)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.EMAIL_FIELD).send_keys(settings.Const.EMAIL)
        time.sleep(1)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.SEND_BUTTON).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(3)
        assert bool(get_email(name_id)) is not False, f"Email have no correct id -  {name_id} in body"

    def open_and_send_development_service_form(self):
        name_id = "TestDevelopmentService"
        self.driver.get(settings.Const.SERVICE_DEVELOPMENT_PAGE)
        self.accept_cookie()
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.NAME_FIELD).send_keys(name_id)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.EMAIL_FIELD).send_keys(settings.Const.EMAIL)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.LAST_NAME_FIELD).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.COMPANY_FIELD).send_keys(settings.Const.COMPANY)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.PHONE_FIELD).send_keys(settings.Const.PHONE)
        time.sleep(1)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.SEND_BUTTON).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(3)
        assert bool(get_email(name_id)) is not False, f"Email have no correct id -  {name_id} in body"

    def open_and_send_extension_service_form(self):
        name_id = "TestExtensionService"
        self.driver.get(settings.Const.SERVICE_EXTENSION_PAGE)
        self.accept_cookie()
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.NAME_FIELD).send_keys(name_id)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.LAST_NAME_FIELD).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.EMAIL_FIELD).send_keys(settings.Const.EMAIL)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.COMPANY_FIELD).send_keys(settings.Const.COMPANY)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.PHONE_FIELD).send_keys(settings.Const.PHONE)
        time.sleep(0.5)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.SEND_BUTTON).click()
        time.sleep(1)

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(3)
        assert bool(get_email(name_id)) is not False, f"Email have no correct id -  {name_id} in body"

    def open_and_send_squads_service_form(self):
        name_id = "TestSquadsService"
        self.driver.get(settings.Const.SERVICE_SQUADS_PAGE)
        self.accept_cookie()
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.NAME_FIELD).send_keys(name_id)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.EMAIL_FIELD).send_keys(settings.Const.EMAIL)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.LAST_NAME_FIELD).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.COMPANY_FIELD).send_keys(settings.Const.COMPANY)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.PHONE_FIELD).send_keys(settings.Const.PHONE)
        time.sleep(1)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.SEND_BUTTON).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(3)
        assert bool(get_email(name_id)) is not False, f"Email have no correct id -  {name_id} in body"

    def open_and_send_devops_service_form(self):
        name_id = "TestDevopsService"
        self.driver.get(settings.Const.SERVICE_DEVOPS_PAGE)
        self.accept_cookie()
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.NAME_FIELD).send_keys(name_id)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.LAST_NAME_FIELD).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.EMAIL_FIELD).send_keys(settings.Const.EMAIL)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.COMPANY_FIELD).send_keys(settings.Const.COMPANY)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.PHONE_FIELD).send_keys(settings.Const.PHONE)
        time.sleep(1)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.SEND_BUTTON).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(3)
        assert bool(get_email(name_id)) is not False, f"Email have no correct id -  {name_id} in body"

    def open_and_send_qa_service_form(self):
        name_id = "TestQaService"
        self.driver.get(settings.Const.SERVICE_QA_PAGE)
        self.accept_cookie()
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.NAME_FIELD).send_keys(name_id)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.LAST_NAME_FIELD).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.EMAIL_FIELD).send_keys(settings.Const.EMAIL)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.COMPANY_FIELD).send_keys(settings.Const.COMPANY)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.PHONE_FIELD).send_keys(settings.Const.PHONE)
        time.sleep(1)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.SEND_BUTTON).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(3)
        assert bool(get_email(name_id)) is not False, f"Email have no correct id -  {name_id} in body"

    def open_and_send_agile_article_form(self):
        name_id = "TestAgileArticle"
        self.driver.get(settings.Const.AGILE_ARTICLE)
        self.accept_cookie()
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.NAME_FIELD).send_keys(name_id)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.LAST_NAME_FIELD).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.EMAIL_FIELD).send_keys(settings.Const.EMAIL)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.PHONE_FIELD).send_keys(settings.Const.PHONE)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.COMPANY_FIELD).send_keys(settings.Const.COMPANY)
        time.sleep(1)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.SEND_BUTTON).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(3)
        assert bool(get_email(name_id)) is not False, f"Email have no correct id -  {name_id} in body"

    def open_and_send_pitfalls_article_form(self):
        name_id = "TestPitfallsArticle"
        self.driver.get(settings.Const.PITFALLS_ARTICLE)
        self.accept_cookie()
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.NAME_FIELD).send_keys(name_id)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.LAST_NAME_FIELD).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.EMAIL_FIELD).send_keys(settings.Const.EMAIL)
        time.sleep(1)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.SEND_BUTTON).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(3)
        assert bool(get_email(name_id)) is not False, f"Email have no correct id -  {name_id} in body"

    def open_and_send_cto_article_form(self):
        name_id = "TestCtoArticle"
        self.driver.get(settings.Const.CTO_ARTICLE)
        self.accept_cookie()
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.NAME_FIELD).send_keys(name_id)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.LAST_NAME_FIELD).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.EMAIL_FIELD).send_keys(settings.Const.EMAIL)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.PHONE_FIELD).send_keys(settings.Const.PHONE)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.COMPANY_FIELD).send_keys(settings.Const.COMPANY)
        time.sleep(1)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.SEND_BUTTON).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(3)
        assert bool(get_email(name_id)) is not False, f"Email have no correct id -  {name_id} in body"

    def open_and_send_anchorfree_case_form(self):
        self.driver.get(settings.Const.ANCHORFREE_CASE)
        self.accept_cookie()
        self.driver.execute_script("window.scrollTo(0, 1000)")
        self.driver.find_element_by_css_selector(
            ".redesign-content-case__sliding [data-form]",
        ).click()
        name_id = "TestAnchorfreeCase"
        self.driver.find_element(By.NAME, "user_name").send_keys(name_id)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.EMAIL_FIELD).send_keys(settings.Const.EMAIL)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.PHONE_FIELD).send_keys(settings.Const.PHONE)
        time.sleep(1)
        self.driver.find_element(By.NAME, BaseFeedbackFormLocators.SEND_BUTTON).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(3)
        assert bool(get_email(name_id)) is not False, f"Email have no correct id -  {name_id} in body"



