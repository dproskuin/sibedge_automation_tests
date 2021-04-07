"""This module contains methods for opening and
interacting with feedback forms."""
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import settings
from .base_form import BaseForm
from .locators import (
    SubscribeFormLocators,
    MainPageLocators,
    WriteToUsFormLocators,
    BaseFeedbackFormLocators,
)


class FeedBackForms(BaseForm):
    """Contains methods for interaction with feedback forms on RU website."""
    def open_about_us_and_form(self) -> None:
        """This method will open About us dropdown and click on element."""
        BaseForm.open(settings.Const.CLIENTS_PAGE)
        about_us = self.driver.find_element(
            By.CSS_SELECTOR,
            MainPageLocators.ABOUT_US_BUTTON,
        )
        ActionChains(self.driver).move_to_element(about_us).perform()
        self.driver.find_element(
            By.CSS_SELECTOR,
            MainPageLocators.SUBSCRIBE_TO_US_BUTTON,
        ).click()

    def open_and_send_write_to_us_form(self):
        """Opens given page, than send feedback form
        and perform 2 assertions consistently.
        """
        name_id = "TestWriteToUs"
        self.driver.get(settings.Const.CLIENTS_PAGE)
        self.driver.find_element(
            By.CSS_SELECTOR,
            MainPageLocators.HEADER_FORM_BUTTON,
        ).click()
        self.driver.find_element(
            By.ID,
            WriteToUsFormLocators.NAME_FIELD,
        ).send_keys(name_id)
        self.driver.find_element(
            By.ID,
            WriteToUsFormLocators.EMAIL_FIELD,
        ).send_keys(settings.Const.EMAIL)
        self.driver.find_element(
            By.ID,
            WriteToUsFormLocators.PHONE_FIELD,
        ).send_keys(settings.Const.PHONE)
        self.driver.find_element(
            By.ID,
            WriteToUsFormLocators.MESSAGE_FIELD,
        ).send_keys(settings.Const.MESSAGE)
        self.driver.find_element(
            By.NAME,
            WriteToUsFormLocators.SEND_BUTTON,
        ).click()
        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(2)
        assert bool(BaseForm.get_email(self, name_id)) is not False, \
            f"Email have no correct id - {name_id} in body"

    def open_and_send_subscribe_to_us_form(self):
        """Opens given page, send feedback form
        and perform 2 assertions consistently.
        """
        name_id = "TestSubscribeToUs"
        self.driver.find_element(
            By.ID,
            SubscribeFormLocators.NAME_FIELD,
        ).send_keys(name_id)
        self.driver.find_element(
            By.ID,
            SubscribeFormLocators.EMAIL_FIELD,
        ).send_keys(settings.Const.EMAIL)
        self.driver.find_element(
            By.ID,
            SubscribeFormLocators.MESSAGE_FIELD,
        ).send_keys(settings.Const.MESSAGE)
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR,
            SubscribeFormLocators.SEND_BUTTON,
        ).click()
        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(2)
        assert bool(BaseForm.get_email(self, name_id)) is not False, \
            f"Email have no correct id - {name_id} in body"

    def open_and_send_main_page_form(self):
        """Opens given page, send feedback form
        and perform 2 assertions consistently.
        """
        name_id = "TestMainPage"
        self.driver.get(settings.Const.MAIN_PAGE)
        BaseForm.accept_cookie(self)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.NAME_FIELD,
        ).send_keys(name_id)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.LAST_NAME_FIELD,
        ).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.EMAIL_FIELD,
        ).send_keys(settings.Const.EMAIL)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.PHONE_FIELD,
        ).send_keys(settings.Const.PHONE)
        time.sleep(1)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.SEND_BUTTON,
        ).click()
        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(2)
        assert bool(BaseForm.get_email(self, name_id)) is not False, \
            f"Email have no correct id - {name_id} in body"

    def open_and_send_models_page_form(self):
        """Opens given page, send feedback form
        and perform 2 assertions consistently.
        """
        name_id = "TestModelsPage"
        self.driver.get(settings.Const.MODELS_PAGE)
        BaseForm.accept_cookie(self)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.NAME_FIELD,
        ).send_keys(name_id)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.LAST_NAME_FIELD,
        ).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.EMAIL_FIELD,
        ).send_keys(settings.Const.EMAIL)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.PHONE_FIELD,
        ).send_keys(settings.Const.PHONE)
        time.sleep(1)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.SEND_BUTTON,
        ).click()
        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(2)
        assert bool(BaseForm.get_email(self, name_id)) is not False, \
            f"Email have no correct id - {name_id} in body"

    def open_and_send_about_us_page_form(self):
        """Opens given page, send feedback form
        and perform 2 assertions consistently.
        """
        name_id = "TestAboutUs"
        self.driver.get(settings.Const.ABOUT_US_PAGE)
        BaseForm.accept_cookie(self)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.NAME_FIELD,
        ).send_keys(name_id)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.LAST_NAME_FIELD,
        ).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.EMAIL_FIELD,
        ).send_keys(settings.Const.EMAIL)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.PHONE_FIELD,
        ).send_keys(settings.Const.PHONE)
        time.sleep(1)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.SEND_BUTTON) \
            .click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(2)
        assert bool(BaseForm.get_email(self, name_id)) is not False, \
            f"Email have no correct id - {name_id} in body"

    def open_and_send_contacts_page_form(self):
        """Opens given page, send feedback form
        and perform 2 assertions consistently.
        """
        name_id = "TestContacts"
        self.driver.get(settings.Const.CONTACTS_PAGE)
        BaseForm.accept_cookie(self)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.NAME_FIELD,
        ).send_keys(name_id)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.LAST_NAME_FIELD,
        ).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.EMAIL_FIELD,
        ).send_keys(settings.Const.EMAIL)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.PHONE_FIELD,
        ).send_keys(settings.Const.PHONE)
        time.sleep(1)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.SEND_BUTTON,
        ).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(2)
        assert bool(BaseForm.get_email(self, name_id)) is not False, \
            f"Email have no correct id - {name_id} in body"

    def open_and_send_blog_page_form(self):
        """Opens given page, send feedback form
        and perform 2 assertions consistently.
        """
        email_id = "blog@test.com"
        self.driver.get(settings.Const.BLOG_PAGE)
        BaseForm.accept_cookie(self)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.LAST_NAME_FIELD,
        ).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.EMAIL_FIELD,
        ).send_keys(email_id)
        time.sleep(1)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.SEND_BUTTON,
        ).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(2)
        assert bool(BaseForm.get_email(self, email_id)) is not False, \
            f"Email have no correct id - {email_id} in body"

    def open_and_send_development_service_form(self):
        """Opens given page, send feedback form
        and perform 2 assertions consistently.
        """
        name_id = "TestDevelopmentService"
        self.driver.get(settings.Const.SERVICE_DEVELOPMENT_PAGE)
        BaseForm.accept_cookie(self)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.NAME_FIELD,
        ).send_keys(name_id)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.EMAIL_FIELD,
        ).send_keys(settings.Const.EMAIL)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.LAST_NAME_FIELD,
        ).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.COMPANY_FIELD,
        ).send_keys(settings.Const.COMPANY)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.PHONE_FIELD,
        ).send_keys(settings.Const.PHONE)
        time.sleep(1)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.SEND_BUTTON,
        ).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(2)
        assert bool(BaseForm.get_email(self, name_id)) is not False, \
            f"Email have no correct id - {name_id} in body"

    def open_and_send_extension_service_form(self):
        """Opens given page, send feedback form
        and perform 2 assertions consistently.
        """
        name_id = "TestExtensionService"
        self.driver.get(settings.Const.SERVICE_EXTENSION_PAGE)
        BaseForm.accept_cookie(self)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.NAME_FIELD,
        ).send_keys(name_id)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.LAST_NAME_FIELD,
        ).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.EMAIL_FIELD,
        ).send_keys(settings.Const.EMAIL)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.COMPANY_FIELD,
        ).send_keys(settings.Const.COMPANY)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.PHONE_FIELD,
        ).send_keys(settings.Const.PHONE)
        time.sleep(0.5)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.SEND_BUTTON,
        ).click()
        time.sleep(1)

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(2)
        assert bool(BaseForm.get_email(self, name_id)) is not False, \
            f"Email have no correct id - {name_id} in body"

    def open_and_send_squads_service_form(self):
        """Opens given page, send feedback form
        and perform 2 assertions consistently.
        """
        name_id = "TestSquadsService"
        self.driver.get(settings.Const.SERVICE_SQUADS_PAGE)
        BaseForm.accept_cookie(self)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.NAME_FIELD,
        ).send_keys(name_id)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.EMAIL_FIELD,
        ).send_keys(settings.Const.EMAIL)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.LAST_NAME_FIELD,
        ).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.COMPANY_FIELD,
        ).send_keys(settings.Const.COMPANY)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.PHONE_FIELD,
        ).send_keys(settings.Const.PHONE)
        time.sleep(1)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.SEND_BUTTON,
        ).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(2)
        assert bool(BaseForm.get_email(self, name_id)) is not False, \
            f"Email have no correct id - {name_id} in body"

    def open_and_send_devops_service_form(self):
        """Opens given page, send feedback form
        and perform 2 assertions consistently.
        """
        name_id = "TestDevopsService"
        self.driver.get(settings.Const.SERVICE_DEVOPS_PAGE)
        BaseForm.accept_cookie(self)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.NAME_FIELD,
        ).send_keys(name_id)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.LAST_NAME_FIELD,
        ).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.EMAIL_FIELD,
        ).send_keys(settings.Const.EMAIL)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.COMPANY_FIELD,
        ).send_keys(settings.Const.COMPANY)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.PHONE_FIELD,
        ).send_keys(settings.Const.PHONE)
        time.sleep(1)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.SEND_BUTTON,
        ).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(2)
        assert bool(BaseForm.get_email(self, name_id)) is not False, \
            f"Email have no correct id - {name_id} in body"

    def open_and_send_qa_service_form(self):
        """Opens given page, send feedback form
        and perform 2 assertions consistently.
        """
        name_id = "TestQaService"
        self.driver.get(settings.Const.SERVICE_QA_PAGE)
        BaseForm.accept_cookie(self)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.NAME_FIELD,
        ).send_keys(name_id)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.LAST_NAME_FIELD,
        ).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.EMAIL_FIELD,
        ).send_keys(settings.Const.EMAIL)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.COMPANY_FIELD,
        ).send_keys(settings.Const.COMPANY)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.PHONE_FIELD,
        ).send_keys(settings.Const.PHONE)
        time.sleep(1)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.SEND_BUTTON,
        ).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(2)
        assert bool(BaseForm.get_email(self, name_id)) is not False, \
            f"Email have no correct id - {name_id} in body"

    def open_and_send_agile_article_form(self):
        """Opens given page, send feedback form
        and perform 2 assertions consistently.
        """
        name_id = "TestAgileArticle"
        self.driver.get(settings.Const.AGILE_ARTICLE)
        BaseForm.accept_cookie(self)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.NAME_FIELD,
        ).send_keys(name_id)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.LAST_NAME_FIELD,
        ).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.EMAIL_FIELD,
        ).send_keys(settings.Const.EMAIL)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.PHONE_FIELD,
        ).send_keys(settings.Const.PHONE)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.COMPANY_FIELD,
        ).send_keys(settings.Const.COMPANY)
        time.sleep(1)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.SEND_BUTTON,
        ).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(2)
        assert bool(BaseForm.get_email(self, name_id)) is not False, \
            f"Email have no correct id - {name_id} in body"

    def open_and_send_pitfalls_article_form(self):
        """Opens given page, send feedback form
        and perform 2 assertions consistently.
        """
        message = settings.Const.PITFALLS_MESSAGE
        self.driver.get(settings.Const.PITFALLS_ARTICLE)
        BaseForm.accept_cookie(self)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.NAME_FIELD,
        ).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.LAST_NAME_FIELD,
        ).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.EMAIL_FIELD,
        ).send_keys(settings.Const.IMAP_USER)
        time.sleep(1)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.SEND_BUTTON,
        ).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(5)
        assert bool(BaseForm.get_email(self, message)) is not False, \
            f"Email have no correct id - '{message}' in body"

    def open_and_send_cto_article_form(self):
        """Opens given page, send feedback form
        and perform 2 assertions consistently.
        """
        name_id = "TestCtoArticle"
        self.driver.get(settings.Const.CTO_ARTICLE)
        BaseForm.accept_cookie(self)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.NAME_FIELD,
        ).send_keys(name_id)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.LAST_NAME_FIELD,
        ).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.EMAIL_FIELD,
        ).send_keys(settings.Const.EMAIL)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.PHONE_FIELD,
        ).send_keys(settings.Const.PHONE)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.COMPANY_FIELD,
        ).send_keys(settings.Const.COMPANY)
        time.sleep(3)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.SEND_BUTTON,
        ).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(2)
        assert bool(BaseForm.get_email(self, name_id)) is not False, \
            f"Email have no correct id - {name_id} in body"

    def open_and_send_deferit_case_form(self):
        """Opens given page, send feedback form
        and perform 2 assertions consistently.
        """
        self.driver.get(settings.Const.DEFERIT_CASE)
        BaseForm.accept_cookie(self)
        self.driver.execute_script("window.scrollTo(0, 1000)")
        self.driver.find_element_by_css_selector(
            ".redesign-content-case__sliding [data-form]",
        ).click()
        name_id = "TestKoronaCase"
        self.driver.find_element(By.NAME, "user_name").send_keys(name_id)
        self.driver.find_element(
            By.NAME, BaseFeedbackFormLocators.EMAIL_FIELD
        ).send_keys(settings.Const.EMAIL)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.PHONE_FIELD,
        ).send_keys(settings.Const.PHONE)
        time.sleep(1)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.SEND_BUTTON,
        ).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(2)
        assert bool(BaseForm.get_email(self, name_id)) is not False, \
            f"Email have no correct id - {name_id} in body"


class FeedBackFormsEn(BaseForm):
    """Contains methods for interaction with feedback forms on RU website."""

    def open_about_us_and_form_en(self) -> None:
        """This method will open About us dropdown and click on element."""
        self.driver.get(settings.Const.CLIENTS_PAGE_EN)
        about_us = self.driver.find_element(
            By.CSS_SELECTOR,
            MainPageLocators.ABOUT_US_BUTTON,
        )
        ActionChains(self.driver).move_to_element(about_us).perform()
        self.driver.find_element(
            By.CSS_SELECTOR,
            MainPageLocators.SUBSCRIBE_TO_US_BUTTON,
        ).click()

    def open_and_send_write_to_us_form_en(self):
        """Opens given page, than send feedback form
        and perform 2 assertions consistently.
        """
        name_id = "TestWriteToUs"
        self.driver.get(settings.Const.CLIENTS_PAGE_EN)
        self.driver.find_element(
            By.CSS_SELECTOR,
            MainPageLocators.HEADER_FORM_BUTTON,
        ).click()
        self.driver.find_element(
            By.ID,
            WriteToUsFormLocators.NAME_FIELD,
        ).send_keys(name_id)
        self.driver.find_element(
            By.ID,
            WriteToUsFormLocators.EMAIL_FIELD,
        ).send_keys(settings.Const.EMAIL)
        self.driver.find_element(
            By.ID,
            WriteToUsFormLocators.PHONE_FIELD,
        ).send_keys(settings.Const.PHONE)
        self.driver.find_element(
            By.ID,
            WriteToUsFormLocators.MESSAGE_FIELD,
        ).send_keys(settings.Const.MESSAGE)
        self.driver.find_element(
            By.NAME,
            WriteToUsFormLocators.SEND_BUTTON,
        ).click()
        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(2)
        assert bool(BaseForm.get_email(self, name_id)) is not False, \
            f"Email have no correct id - {name_id} in body"

    def open_and_send_subscribe_to_us_form_en(self):
        """Opens given page, send feedback form
        and perform 2 assertions consistently.
        """
        name_id = "TestSubscribeToUs"
        self.driver.find_element(
            By.ID,
            SubscribeFormLocators.NAME_FIELD,
        ).send_keys(name_id)
        self.driver.find_element(
            By.ID,
            SubscribeFormLocators.EMAIL_FIELD,
        ).send_keys(settings.Const.EMAIL)
        self.driver.find_element(
            By.ID,
            SubscribeFormLocators.MESSAGE_FIELD,
        ).send_keys(settings.Const.MESSAGE)
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR,
            SubscribeFormLocators.SEND_BUTTON,
        ).click()
        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(2)
        assert bool(BaseForm.get_email(self, name_id)) is not False, \
            f"Email have no correct id - {name_id} in body"

    def open_and_send_main_page_form_en(self):
        """Opens given page, send feedback form
        and perform 2 assertions consistently.
        """
        name_id = "TestMainPage"
        self.driver.get(settings.Const.MAIN_PAGE_EN)
        BaseForm.accept_cookie(self)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.NAME_FIELD,
        ).send_keys(name_id)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.LAST_NAME_FIELD,
        ).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.EMAIL_FIELD,
        ).send_keys(settings.Const.EMAIL)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.PHONE_FIELD,
        ).send_keys(settings.Const.PHONE)
        time.sleep(1)
        self.driver.find_element(
            By.NAME, BaseFeedbackFormLocators.SEND_BUTTON,
        ).click()
        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(2)
        assert bool(BaseForm.get_email(self, name_id)) is not False, \
            f"Email have no correct id - {name_id} in body"

    def open_and_send_models_page_form_en(self):
        """Opens given page, send feedback form
        and perform 2 assertions consistently.
        """
        name_id = "TestModelsPage"
        self.driver.get(settings.Const.MODELS_PAGE_EN)
        BaseForm.accept_cookie(self)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.NAME_FIELD,
        ).send_keys(name_id)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.LAST_NAME_FIELD,
        ).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(
            By.NAME, BaseFeedbackFormLocators.EMAIL_FIELD,
        ).send_keys(settings.Const.EMAIL)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.PHONE_FIELD,
        ).send_keys(settings.Const.PHONE)
        time.sleep(1)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.SEND_BUTTON,
        ).click()
        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(2)
        assert bool(BaseForm.get_email(self, name_id)) is not False, \
            f"Email have no correct id - {name_id} in body"

    def open_and_send_about_us_page_form_en(self):
        """Opens given page, send feedback form
        and perform 2 assertions consistently.
        """
        name_id = "TestAboutUs"
        self.driver.get(settings.Const.ABOUT_US_PAGE_EN)
        BaseForm.accept_cookie(self)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.NAME_FIELD,
        ).send_keys(name_id)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.LAST_NAME_FIELD,
        ).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.EMAIL_FIELD,
        ).send_keys(settings.Const.EMAIL)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.PHONE_FIELD,
        ).send_keys(settings.Const.PHONE)
        time.sleep(1)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.SEND_BUTTON) \
            .click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(2)
        assert bool(BaseForm.get_email(self, name_id)) is not False, \
            f"Email have no correct id - {name_id} in body"

    def open_and_send_contacts_page_form_en(self):
        """Opens given page, send feedback form
        and perform 2 assertions consistently.
        """
        name_id = "TestContacts"
        self.driver.get(settings.Const.CONTACTS_PAGE_EN)
        BaseForm.accept_cookie(self)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.NAME_FIELD,
        ).send_keys(name_id)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.LAST_NAME_FIELD,
        ).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.EMAIL_FIELD,
        ).send_keys(settings.Const.EMAIL)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.PHONE_FIELD,
        ).send_keys(settings.Const.PHONE)
        time.sleep(1)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.SEND_BUTTON,
        ).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(2)
        assert bool(BaseForm.get_email(self, name_id)) is not False, \
            f"Email have no correct id - {name_id} in body"

    def open_and_send_blog_page_form_en(self):
        """Opens given page, send feedback form
        and perform 2 assertions consistently.
        """
        email_id = "blog@test.com"
        self.driver.get(settings.Const.BLOG_PAGE_EN)
        BaseForm.accept_cookie(self)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.LAST_NAME_FIELD,
        ).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.EMAIL_FIELD,
        ).send_keys(email_id)
        time.sleep(1)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.SEND_BUTTON,
        ).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(2)
        assert bool(BaseForm.get_email(self, email_id)) is not False, \
            f"Email have no correct id - {email_id} in body"

    def open_and_send_development_service_form_en(self):
        """Opens given page, send feedback form
        and perform 2 assertions consistently.
        """
        name_id = "TestDevelopmentService"
        self.driver.get(settings.Const.SERVICE_DEVELOPMENT_PAGE_EN)
        BaseForm.accept_cookie(self)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.NAME_FIELD,
        ).send_keys(name_id)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.EMAIL_FIELD,
        ).send_keys(settings.Const.EMAIL)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.LAST_NAME_FIELD,
        ).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.COMPANY_FIELD,
        ).send_keys(settings.Const.COMPANY)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.PHONE_FIELD,
        ).send_keys(settings.Const.PHONE)
        time.sleep(1)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.SEND_BUTTON,
        ).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(2)
        assert bool(BaseForm.get_email(self, name_id)) is not False, \
            f"Email have no correct id - {name_id} in body"

    def open_and_send_extension_service_form_en(self):
        """Opens given page, send feedback form
        and perform 2 assertions consistently.
        """
        name_id = "TestExtensionService"
        self.driver.get(settings.Const.SERVICE_EXTENSION_PAGE_EN)
        BaseForm.accept_cookie(self)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.NAME_FIELD,
        ).send_keys(name_id)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.LAST_NAME_FIELD,
        ).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.EMAIL_FIELD,
        ).send_keys(settings.Const.EMAIL)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.COMPANY_FIELD,
        ).send_keys(settings.Const.COMPANY)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.PHONE_FIELD,
        ).send_keys(settings.Const.PHONE)
        time.sleep(0.5)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.SEND_BUTTON,
        ).click()
        time.sleep(1)

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(2)
        assert bool(BaseForm.get_email(self, name_id)) is not False, \
            f"Email have no correct id - {name_id} in body"

    def open_and_send_squads_service_form_en(self):
        """Opens given page, send feedback form
        and perform 2 assertions consistently.
        """
        name_id = "TestSquadsService"
        self.driver.get(settings.Const.SERVICE_SQUADS_PAGE_EN)
        BaseForm.accept_cookie(self)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.NAME_FIELD,
        ).send_keys(name_id)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.EMAIL_FIELD,
        ).send_keys(settings.Const.EMAIL)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.LAST_NAME_FIELD,
        ).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.COMPANY_FIELD,
        ).send_keys(settings.Const.COMPANY)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.PHONE_FIELD,
        ).send_keys(settings.Const.PHONE)
        time.sleep(1)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.SEND_BUTTON,
        ).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(2)
        assert bool(BaseForm.get_email(self, name_id)) is not False, \
            f"Email have no correct id - {name_id} in body"

    def open_and_send_devops_service_form_en(self):
        """Opens given page, send feedback form
        and perform 2 assertions consistently.
        """
        name_id = "TestDevopsService"
        self.driver.get(settings.Const.SERVICE_DEVOPS_PAGE_EN)
        BaseForm.accept_cookie(self)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.NAME_FIELD,
        ).send_keys(name_id)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.LAST_NAME_FIELD,
        ).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.EMAIL_FIELD,
        ).send_keys(settings.Const.EMAIL)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.COMPANY_FIELD,
        ).send_keys(settings.Const.COMPANY)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.PHONE_FIELD,
        ).send_keys(settings.Const.PHONE)
        time.sleep(1)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.SEND_BUTTON,
        ).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(2)
        assert bool(BaseForm.get_email(self, name_id)) is not False, \
            f"Email have no correct id - {name_id} in body"

    def open_and_send_qa_service_form_en(self):
        """Opens given page, send feedback form
        and perform 2 assertions consistently.
        """
        name_id = "TestQaService"
        self.driver.get(settings.Const.SERVICE_QA_PAGE_EN)
        BaseForm.accept_cookie(self)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.NAME_FIELD,
        ).send_keys(name_id)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.LAST_NAME_FIELD,
        ).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.EMAIL_FIELD,
        ).send_keys(settings.Const.EMAIL)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.COMPANY_FIELD,
        ).send_keys(settings.Const.COMPANY)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.PHONE_FIELD,
        ).send_keys(settings.Const.PHONE)
        time.sleep(1)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.SEND_BUTTON,
        ).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(2)
        assert bool(BaseForm.get_email(self, name_id)) is not False, \
            f"Email have no correct id - {name_id} in body"

    def open_and_send_agile_article_form_en(self):
        """Opens given page, send feedback form
        and perform 2 assertions consistently.
        """
        name_id = "TestAgileArticle"
        self.driver.get(settings.Const.AGILE_ARTICLE_EN)
        BaseForm.accept_cookie(self)
        self.driver.find_element(
            By.NAME, BaseFeedbackFormLocators.NAME_FIELD,
        ).send_keys(name_id)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.LAST_NAME_FIELD,
        ).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.EMAIL_FIELD,
        ).send_keys(settings.Const.EMAIL)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.PHONE_FIELD,
        ).send_keys(settings.Const.PHONE)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.COMPANY_FIELD,
        ).send_keys(settings.Const.COMPANY)
        time.sleep(1)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.SEND_BUTTON,
        ).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(2)
        assert bool(BaseForm.get_email(self, name_id)) is not False, \
            f"Email have no correct id - {name_id} in body"

    def open_and_send_pitfalls_article_form_en(self):
        """Opens given page, send feedback form
        and perform 2 assertions consistently.
        """
        message = settings.Const.PITFALLS_MESSAGE
        self.driver.get(settings.Const.PITFALLS_ARTICLE_EN)
        BaseForm.accept_cookie(self)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.NAME_FIELD,
        ).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.LAST_NAME_FIELD,
        ).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.EMAIL_FIELD,
        ).send_keys(settings.Const.IMAP_USER)
        time.sleep(1)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.SEND_BUTTON,
        ).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(5)
        assert bool(BaseForm.get_email(self, message)) is not False, \
            f"Email have no correct id - '{message}' in body"

    def open_and_send_cto_article_form_en(self):
        """Opens given page, send feedback form
        and perform 2 assertions consistently.
        """
        name_id = "TestCtoArticle"
        self.driver.get(settings.Const.CTO_ARTICLE_EN)
        BaseForm.accept_cookie(self)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.NAME_FIELD,
        ).send_keys(name_id)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.LAST_NAME_FIELD,
        ).send_keys(settings.Const.LAST_NAME)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.EMAIL_FIELD,
        ).send_keys(settings.Const.EMAIL)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.PHONE_FIELD,
        ).send_keys(settings.Const.PHONE)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.COMPANY_FIELD,
        ).send_keys(settings.Const.COMPANY)
        time.sleep(3)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.SEND_BUTTON,
        ).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(2)
        assert bool(BaseForm.get_email(self, name_id)) is not False, \
            f"Email have no correct id - {name_id} in body"

    def open_and_send_deferit_case_form_en(self):
        """Opens given page, send feedback form
        and perform 2 assertions consistently.
        """
        self.driver.get(settings.Const.DEFERIT_CASE_EN)
        BaseForm.accept_cookie(self)
        self.driver.execute_script("window.scrollTo(0, 1000)")
        self.driver.find_element_by_css_selector(
            ".redesign-content-case__sliding [data-form]",
        ).click()
        name_id = "TestDeferitCase"
        self.driver.find_element(By.NAME, "user_name").send_keys(name_id)
        self.driver.find_element(
            By.NAME, BaseFeedbackFormLocators.EMAIL_FIELD
        ).send_keys(settings.Const.EMAIL)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.PHONE_FIELD,
        ).send_keys(settings.Const.PHONE)
        time.sleep(1)
        self.driver.find_element(
            By.NAME,
            BaseFeedbackFormLocators.SEND_BUTTON,
        ).click()

        assert "success" in self.driver.current_url, "No 'success' in URL"
        time.sleep(2)
        assert bool(BaseForm.get_email(self, name_id)) is not False, \
            f"Email have no correct id - {name_id} in body"
