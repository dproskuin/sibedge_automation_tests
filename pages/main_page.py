from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Remote as RemoteWebDriver
import pytest
from .locators import MainPageLocators

link = "https://sibedge.com/en/"

class MainPage(BasePage):

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
        assert self.is_element_present(*MainPageLocators.MODELS_HEADER), "Header is not presented. Check test results."

    def open_projects_page(self):
        projects = self.driver.find_element(By.CSS_SELECTOR,
            ".header__nav.js--header-nav > .nav > li:nth-of-type(5) > .nav__item-link"
        )
        projects.click()

    def open_clients_page(self):
        clients = self.driver.find_element(By.CSS_SELECTOR,
            ".header__nav.js--header-nav > .nav > li:nth-of-type(6) > .nav__item-link"
        )
        clients.click()

    def open_contacts_page(self):
        contacts = self.driver.find_element(By.CSS_SELECTOR,
            ".header__nav.js--header-nav > .nav > li:nth-of-type(7) > .nav__item-link"
        )
        contacts.click()

    def open_development_page(self):
        self.open_services_list()
        development_button = self.driver.find_element(By.CSS_SELECTOR,
            'li:nth-of-type(3) > .nav__sub-menu > li:nth-of-type(1) > .nav__sub-menu-link'
        )
        development_button.click()

    def open_qa_page(self):
        self.open_services_list()
        qa_button = self.driver.find_element(By.CSS_SELECTOR,
        'li:nth-of-type(3) > .nav__sub-menu > li:nth-of-type(2) > .nav__sub-menu-link'
        )
        qa_button.click()

    def open_devops_page(self):
        self.open_services_list()
        devops_button = self.driver.find_element(By.CSS_SELECTOR,
        'li:nth-of-type(3) > .nav__sub-menu > li:nth-of-type(3) > .nav__sub-menu-link'
        )
        devops_button.click()

    def open_r_d_page(self):
        self.open_services_list()
        rd_button = self.driver.find_element(By.CSS_SELECTOR,
        'li:nth-of-type(3) > .nav__sub-menu > li:nth-of-type(4) > .nav__sub-menu-link'
        )
        rd_button.click()

    def accept_cookie(self):
        cookies_accept = self.driver.find_element(By.CSS_SELECTOR,
            ".cookie-alert__button.cookie-alert__button--agree.js--cookie-alert-allow")
        cookies_accept.click()

    def open_main_page_by_click_to_logo(self):
        logo = self.driver.find_element(By.CSS_SELECTOR,
            ".header__logo > svg"
        )
        logo.click()

    def open_get_in_touch_form(self):
        get_in_touch_button = self.driver.find_element(By.CSS_SELECTOR,
            ".header__mail-button"
        )
        get_in_touch_button.click()

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

    def open_press_page(self):
        self.open_about_us_list()
        press = self.driver.find_element(By.CSS_SELECTOR,
            'li:nth-of-type(2) > .nav__sub-menu > li:nth-of-type(2) > .nav__sub-menu-link'
        )
        press.click()

    def open_blog_page(self):
        self.open_about_us_list()
        blog = self.driver.find_element(By.CSS_SELECTOR,
            'li:nth-of-type(2) > .nav__sub-menu > li:nth-of-type(3) > .nav__sub-menu-link'
        )
        blog.click()

    def open_subscribe_to_us_form(self):
        self.open_about_us_list()
        subscribe_to_us = self.driver.find_element(By.CSS_SELECTOR,
            "li:nth-of-type(5) > .nav__sub-menu-link"
        )
        subscribe_to_us.click()













