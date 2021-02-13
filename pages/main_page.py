from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Remote as RemoteWebDriver
import pytest
from .locators import ModelsPageLocators, ProjectsPageLocators, ClientsPageLocators,\
    ContactsPageLocators, DevelopmentPageLocators, QaPageLocators, DevopsPageLocators,\
    WhySibedgePageLocators, PressPageLocators, BlogPageLocators, MainPageLocators, \
    SubscribeToUsFormLocators, GetInTouchFormLocators, SitemapLocators, TeamExtensionLocators, SquadsProductLocators

#@pytest.mark.parametrize('language', ["en", "ru"])
link = "https://se.sibedge.com/"

class MainPage(BasePage):
    """This class contains methods for opening pages/elements + asserts"""

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
        assert self.is_element_present(*ModelsPageLocators.MODELS_HEADER), "Models header is not presented. Check test results."

    def open_projects_page(self):
        projects = self.driver.find_element(By.CSS_SELECTOR,
            ".header__nav.js--header-nav > .nav > li:nth-of-type(5) > .nav__item-link"
        )
        projects.click()
        assert self.is_element_present(
            *ProjectsPageLocators.PROJECTS_HEADER), "Projects header is not presented. Check test results."

    def open_clients_page(self):
        clients = self.driver.find_element(By.CSS_SELECTOR,
            ".header__nav.js--header-nav > .nav > li:nth-of-type(6) > .nav__item-link"
        )
        clients.click()
        assert self.is_element_present(
            *ClientsPageLocators.CLIENTS_HEADER), "Clients header is not presented. Check test results."
        assert self.is_element_present(
            *ClientsPageLocators.CLIENTS_TITLE), "Clients title is not presented. Check test result"

    def open_contacts_page(self):
        contacts = self.driver.find_element(By.CSS_SELECTOR,
            ".header__nav.js--header-nav > .nav > li:nth-of-type(7) > .nav__item-link"
        )
        contacts.click()
        assert self.is_element_present(
            *ContactsPageLocators.CONTACTS_HEADER), "Contacts page header is not presented. Check test results."
        assert self.is_element_present(
            *ContactsPageLocators.CONTACTS_ADRESSES_LIST), "Contacts Adresses List is not present. Check test results."

    def open_development_page(self):
        self.open_services_list()
        development_button = self.driver.find_element(By.CSS_SELECTOR,
            'li:nth-of-type(3) > .nav__sub-menu > li:nth-of-type(1) > .nav__sub-menu-link'
        )
        development_button.click()
        assert self.is_element_present(
            *DevelopmentPageLocators.DEVELOPMENT_HEADER), "Dev service page header is not presented. Check test results."

    def open_qa_page(self):
        self.open_services_list()
        qa_button = self.driver.find_element(By.CSS_SELECTOR,
        'li:nth-of-type(3) > .nav__sub-menu > li:nth-of-type(2) > .nav__sub-menu-link'
        )
        qa_button.click()
        assert self.is_element_present(
            *QaPageLocators.QA_HEADER), "QA Page header is not presented. Check test results."

    def open_devops_page(self):
        self.open_services_list()
        devops_button = self.driver.find_element(By.CSS_SELECTOR,
        'li:nth-of-type(3) > .nav__sub-menu > li:nth-of-type(3) > .nav__sub-menu-link'
        )
        devops_button.click()
        assert self.is_element_present(
            *DevopsPageLocators.DEVOPS_HEADER), "Devops page header is not presented. Check test results."

    #def open_r_d_page(self):
        #self.open_services_list()
        #rd_button = self.driver.find_element(By.CSS_SELECTOR,
        #'li:nth-of-type(3) > .nav__sub-menu > li:nth-of-type(4) > .nav__sub-menu-link'
        #)
        #rd_button.click()
        #assert self.is_element_present(
            #*RdPageLocators.RD_HEADER), "R&D header is not presented. Check test results."\

    def open_squads_product_page(self):
        self.open_services_list()
        squads_product_button = self.driver.find_element(By.CSS_SELECTOR,
        "li:nth-of-type(3) > .nav__sub-menu > li:nth-of-type(3) > .nav__sub-menu-link"
        )
        squads_product_button.click()
        assert self.is_element_present(
            *SquadsProductLocators.SQUADS_PRODUCT_HEADER), "Squads product page header is not present."

    def open_team_extension_page(self):
        self.open_services_list()
        team_extension_button = self.driver.find_element(By.CSS_SELECTOR,
        "li:nth-of-type(3) > .nav__sub-menu > li:nth-of-type(3) > .nav__sub-menu-link"
        )
        team_extension_button.click()
        assert self.is_element_present(
            *TeamExtensionLocators.TEAMEXTENSION_HEADER), "Team Extension page header is not presented. Check test results."

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
            *GetInTouchFormLocators.GETINTOUCH_HEADER), "Get in touch header is not presented!"

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
            *WhySibedgePageLocators.WHYSIBEDGE_HEADER), "Why sibedge header is not presented. Check test results."

    def open_press_page(self):
        self.open_about_us_list()
        press = self.driver.find_element(By.CSS_SELECTOR,
            'li:nth-of-type(2) > .nav__sub-menu > li:nth-of-type(2) > .nav__sub-menu-link'
        )
        press.click()
        assert self.is_element_present(
            *PressPageLocators.PRESS_HEADER), "Press header is not presented. Check test results."

    def open_blog_page(self):
        self.open_about_us_list()
        blog = self.driver.find_element(By.CSS_SELECTOR,
            'li:nth-of-type(2) > .nav__sub-menu > li:nth-of-type(3) > .nav__sub-menu-link'
        )
        blog.click()
        assert self.is_element_present(
            *BlogPageLocators.BLOG_HEADER), "Blog header is not presented. Check test results."

    def open_subscribe_to_us_form(self):
        self.open_about_us_list()
        subscribe_to_us = self.driver.find_element(By.CSS_SELECTOR,
            "li:nth-of-type(5) > .nav__sub-menu-link"
        )
        subscribe_to_us.click()
        assert self.is_element_present(
            *SubscribeToUsFormLocators.SUBSCRIBETOUS_HEADER), "Subscribe to us header is not presented. Check test results."

    def open_sitemap_page(self):
        sitemap_link = "https://dev.sibedge.com/sitemap/"
        self.driver.get(sitemap_link)
        assert self.is_element_present(*SitemapLocators.SITEMAP_HEADER), "Sitemap header is not presented."



















