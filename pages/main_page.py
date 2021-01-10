from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Remote as RemoteWebDriver
import pytest
from .locators import ModelsPageLocators, ProjectsPageLocators, ClientsPageLocators,\
    ContactsPageLocators, DevelopmentPageLocators, QaPageLocators, DevopsPageLocators,\
    RdPageLocators, WhySibedgePageLocators, PressPageLocators, BlogPageLocators, MainPageLocators, \
    SubscribeToUsFormLocators, GetInTouchFormLocators

link = "https://se.sibedge.com/en/"

class MainPage(BasePage):
    """Methods with open_page steps and asserts"""

    def open_about_us_list(self):
        about_us = self.driver.find_element(By.CSS_SELECTOR, ".nav__item:nth-of-type(2) .nav__item-link")
        hover = ActionChains(self.driver).move_to_element(about_us)
        hover.perform()

    def open_services_list(self):
        services = self.driver.find_element(By.CSS_SELECTOR, ".nav__item:nth-of-type(3) .nav__item-link")
        hover = ActionChains(self.driver).move_to_element(services)
        hover.perform()

    def open_models_page(self):
        models = self.driver.find_element(By.CSS_SELECTOR,
            ".header__nav.js--header-nav > .nav > li:nth-of-type(4) > .nav__item-link"
        )
        models.click()
        assert self.is_element_present(*ModelsPageLocators.MODELS_HEADER), "Header is not presented. Check test results."

    def open_projects_page(self):
        projects = self.driver.find_element(By.CSS_SELECTOR,
            ".header__nav.js--header-nav > .nav > li:nth-of-type(5) > .nav__item-link"
        )
        projects.click()
        assert self.is_element_present(
            *ProjectsPageLocators.PROJECTS_HEADER), "Header is not presented. Check test results."

    def open_clients_page(self):
        clients = self.driver.find_element(By.CSS_SELECTOR,
            ".header__nav.js--header-nav > .nav > li:nth-of-type(6) > .nav__item-link"
        )
        clients.click()
        assert self.is_element_present(
            *ClientsPageLocators.CLIENTS_HEADER), "Header is not presented. Check test results."

    def open_contacts_page(self):
        contacts = self.driver.find_element(By.CSS_SELECTOR,
            ".header__nav.js--header-nav > .nav > li:nth-of-type(7) > .nav__item-link"
        )
        contacts.click()
        assert self.is_element_present(
            *ContactsPageLocators.CONTACTS_HEADER), "Header is not presented. Check test results."

    def open_development_page(self):
        self.open_services_list()
        development_button = self.driver.find_element(By.CSS_SELECTOR,
            'li:nth-of-type(3) > .nav__sub-menu > li:nth-of-type(1) > .nav__sub-menu-link'
        )
        development_button.click()
        assert self.is_element_present(
            *DevelopmentPageLocators.DEVELOPMENT_HEADER), "Header is not presented. Check test results."

    def open_qa_page(self):
        self.open_services_list()
        qa_button = self.driver.find_element(By.CSS_SELECTOR,
        'li:nth-of-type(3) > .nav__sub-menu > li:nth-of-type(2) > .nav__sub-menu-link'
        )
        qa_button.click()
        assert self.is_element_present(
            *QaPageLocators.QA_HEADER), "Header is not presented. Check test results."

    def open_devops_page(self):
        self.open_services_list()
        devops_button = self.driver.find_element(By.CSS_SELECTOR,
        'li:nth-of-type(3) > .nav__sub-menu > li:nth-of-type(3) > .nav__sub-menu-link'
        )
        devops_button.click()
        assert self.is_element_present(
            *DevopsPageLocators.DEVOPS_HEADER), "Header is not presented. Check test results."

    def open_r_d_page(self):
        self.open_services_list()
        rd_button = self.driver.find_element(By.CSS_SELECTOR,
        'li:nth-of-type(3) > .nav__sub-menu > li:nth-of-type(4) > .nav__sub-menu-link'
        )
        rd_button.click()
        assert self.is_element_present(
            *RdPageLocators.RD_HEADER), "Header is not presented. Check test results."

    def accept_cookie(self):
        cookies_accept = self.driver.find_element(By.CSS_SELECTOR,
            ".cookie-alert__button.cookie-alert__button--agree.js--cookie-alert-allow")
        cookies_accept.click()

    def open_main_page_by_click_to_logo(self):
        logo = self.driver.find_element(By.CSS_SELECTOR,
            ".header__logo > svg"
        )
        logo.click()
        url = "https://se.sibedge.com/en/"
        assert url == MainPageLocators.MAIN_URL

    def open_get_in_touch_form(self):
        get_in_touch_button = self.driver.find_element(By.CSS_SELECTOR,
            ".header__mail-button"
        )
        get_in_touch_button.click()
        assert self.is_element_present(
            *GetInTouchFormLocators.GETINTOUCH_HEADER), "Header is not presented!"

    def close_get_in_touch_form(self):
        form_close_button = self.driver.find_element(By.CSS_SELECTOR,
            ".feedback-form.js--feedback-form.js--form.visible > form[method='post']  .feedback-form__close.js--form-close > svg"
        )
        form_close_button.click()

    def open_why_sibedge_page(self):
        self.open_about_us_list()
        why_sibedge = self.driver.find_element(By.CSS_SELECTOR,
            "li:nth-of-type(2) > .nav__sub-menu > li:nth-of-type(1) > .nav__sub-menu-link"
        )
        why_sibedge.click()
        assert self.is_element_present(
            *WhySibedgePageLocators.WHYSIBEDGE_HEADER), "Header is not presented. Check test results."

    def open_press_page(self):
        self.open_about_us_list()
        press = self.driver.find_element(By.CSS_SELECTOR,
            'li:nth-of-type(2) > .nav__sub-menu > li:nth-of-type(2) > .nav__sub-menu-link'
        )
        press.click()
        assert self.is_element_present(
            *PressPageLocators.PRESS_HEADER), "Header is not presented. Check test results."

    def open_blog_page(self):
        self.open_about_us_list()
        blog = self.driver.find_element(By.CSS_SELECTOR,
            'li:nth-of-type(2) > .nav__sub-menu > li:nth-of-type(3) > .nav__sub-menu-link'
        )
        blog.click()
        assert self.is_element_present(
            *BlogPageLocators.BLOG_HEADER), "Header is not presented. Check test results."

    def open_subscribe_to_us_form(self):
        self.open_about_us_list()
        subscribe_to_us = self.driver.find_element(By.CSS_SELECTOR,
            "li:nth-of-type(5) > .nav__sub-menu-link"
        )
        subscribe_to_us.click()
        assert self.is_element_present(
            *SubscribeToUsFormLocators.SUBSCRIBETOUS_HEADER), "Header is not presented. Check test results."













