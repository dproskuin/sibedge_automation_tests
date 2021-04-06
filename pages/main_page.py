"""This module describes site's main page methods (Page object)."""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import settings
from .base_page import BasePage
from .locators import (
    ModelsPageLocators,
    ProjectsPageLocators,
    ClientsPageLocators,
    ContactsPageLocators,
    DevelopmentPageLocators,
    QaPageLocators,
    DevopsPageLocators,
    WhySibedgePageLocators,
    PressPageLocators,
    BlogPageLocators,
    MainPageLocators,
    GetInTouchFormLocators,
    SitemapLocators,
    TeamExtensionLocators,
    SquadsProductLocators,
)

LINK = "https://se.sibedge.com/en/"


class MainPage(BasePage):
    """This class contains methods for opening pages and asserts"""
    def open_about_us_list(self):
        about_us = self.driver.find_element(
            By.CSS_SELECTOR,
            ".nav__item:nth-of-type(2) .nav__item-link"
        )
        ActionChains(self.driver).move_to_element(about_us).perform()

    def open_services_list(self):
        services = self.driver.find_element(
            By.CSS_SELECTOR,
            ".nav__item:nth-of-type(3) .nav__item-link"
        )
        ActionChains(self.driver).move_to_element(services).perform()

    def open_models_page(self):
        self.driver.find_element(
            By.CSS_SELECTOR,
            ".header__nav.js--header-nav > .nav > li:nth-of-type(4) > .nav__item-link",
        ).click()

        assert self.is_element_present(
            *ModelsPageLocators.MODELS_HEADER
        ), "Models header is not presented."

    def open_projects_page(self):
        self.driver.find_element(
            By.CSS_SELECTOR,
            ".header__nav.js--header-nav > .nav > li:nth-of-type(5) > .nav__item-link",
        ).click()

        assert self.is_element_present(
            *ProjectsPageLocators.PROJECTS_HEADER),\
            "Projects header is not presented. Check test results."

    def open_clients_page(self):
        self.driver.find_element(
            By.CSS_SELECTOR,
            ".header__nav.js--header-nav > .nav > li:nth-of-type(6) > .nav__item-link",
        ).click()

        assert self.is_element_present(
            *ClientsPageLocators.CLIENTS_HEADER),\
            "Clients header is not presented. Check test results."
        assert self.is_element_present(
            *ClientsPageLocators.CLIENTS_TITLE),\
            "Clients title is not presented. Check test result"

    def open_contacts_page(self):
        self.driver.find_element(
            By.CSS_SELECTOR,
            ".header__nav.js--header-nav > .nav > li:nth-of-type(7) > .nav__item-link",
        ).click()
        assert self.is_element_present(
            *ContactsPageLocators.CONTACTS_HEADER),\
            "Contacts page header is not presented."
        assert self.is_element_present(
            *ContactsPageLocators.CONTACTS_ADRESSES_LIST),\
            "Contacts Adresses List is not present."

    def open_development_page(self):
        self.open_services_list()
        self.driver.find_element(
            By.CSS_SELECTOR,
            "li:nth-of-type(3) > .nav__sub-menu > li:nth-of-type(1) > .nav__sub-menu-link",
        ).click()

        assert self.is_element_present(
            *DevelopmentPageLocators.DEVELOPMENT_HEADER),\
            "Dev service page header is not presented."

    def open_qa_page(self):
        self.open_services_list()
        self.driver.find_element(
            By.CSS_SELECTOR,
            "li:nth-of-type(3) > .nav__sub-menu > li:nth-of-type(2) > .nav__sub-menu-link"
        ).click()

        assert self.is_element_present(
            *QaPageLocators.QA_HEADER),\
            "QA Page header is not presented. Check test results."

    def open_devops_page(self):
        self.open_services_list()
        self.driver.find_element(
            By.CSS_SELECTOR,
            "li:nth-of-type(3) > .nav__sub-menu > li:nth-of-type(3) > .nav__sub-menu-link",
        ).click()

        assert self.is_element_present(
            *DevopsPageLocators.DEVOPS_HEADER), "Devops header is not presented."

    def open_squads_product_page(self):
        self.open_services_list()
        self.driver.find_element(
            By.CSS_SELECTOR,
            "li:nth-of-type(3) > .nav__sub-menu > li:nth-of-type(3) > .nav__sub-menu-link",
        ).click()

        assert self.is_element_present(
            *SquadsProductLocators.SQUADS_PRODUCT_HEADER),\
            "Squads header is not present."

    def open_team_extension_page(self):
        self.open_services_list()
        self.driver.find_element(
            By.CSS_SELECTOR,
            "li:nth-of-type(3) > .nav__sub-menu > li:nth-of-type(3) > .nav__sub-menu-link",
        ).click()
        assert self.is_element_present(
            *TeamExtensionLocators.TEAMEXTENSION_HEADER),\
            "Team Extension header isn't presented"

    def accept_cookie(self):
        self.driver.find_element(
            By.CSS_SELECTOR,
            ".cookie-alert__button.cookie-alert__button--agree.js--cookie-alert-allow",
        ).click()

    def open_get_in_touch_form(self):
        self.driver.find_element(
            By.CSS_SELECTOR,
            ".header__mail-button",
        ).click()
        assert self.is_element_present(
            *GetInTouchFormLocators.GETINTOUCH_HEADER),\
            "Get in touch header is not presented!"

    def close_get_in_touch_form(self):
        self.driver.find_element(
            By.CLASS_NAME,
            "feedback-form__close js--form-close",
        ).click()

    def open_why_sibedge_page(self):
        self.open_about_us_list()
        self.driver.find_element(
            By.CSS_SELECTOR,
            "li:nth-of-type(2) > .nav__sub-menu > li:nth-of-type(1) > .nav__sub-menu-link",
            ).click()

        assert self.is_element_present(
            *WhySibedgePageLocators.WHYSIBEDGE_HEADER),\
            "'Why sibedge' header is not presented"

    def open_press_page(self):
        self.open_about_us_list()
        self.driver.find_element(
            By.CSS_SELECTOR,
            "li:nth-of-type(2) > .nav__sub-menu > li:nth-of-type(2) > .nav__sub-menu-link",
        ).click()
        assert self.is_element_present(
            *PressPageLocators.PRESS_HEADER),\
            "Press header is not presented. Check test results."

    def open_blog_page(self):
        self.open_about_us_list()
        self.driver.find_element(
            By.CSS_SELECTOR,
            "li:nth-of-type(2) > .nav__sub-menu > li:nth-of-type(3) > .nav__sub-menu-link"
        ).click()

        assert self.is_element_present(
            *BlogPageLocators.BLOG_HEADER),\
            "Blog header is not presented. Check test results."

    def open_sitemap_page(self):
        self.driver.get(settings.Const.SITEMAP_PAGE)

        assert self.is_element_present(
            *SitemapLocators.SITEMAP_HEADER
        ), "Sitemap header is not presented."
