from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pytest


link = "https://sibedge.com/en/"

def test_accept_cookie(driver):
    driver.get(link)
    cookies_accept = driver.find_element_by_css_selector(
        ".cookie-alert__button.cookie-alert__button--agree.js--cookie-alert-allow")
    cookies_accept.click()


def test_about_us_1(driver):
    driver.get(link)
    about_us = driver.find_element_by_css_selector(".nav__item:nth-of-type(2) .nav__item-link")
    hover = ActionChains(driver).move_to_element(about_us)
    hover.perform()
    why_sibedge = driver.find_element_by_css_selector(
        "li:nth-of-type(2) > .nav__sub-menu > li:nth-of-type(1) > .nav__sub-menu-link").click()
    url = "https://sibedge.com/en/why-sibedge/"
    assert driver.current_url == url, "URL /why-sibedge не совпадает!"


def test_about_us_2(driver):
    driver.get(link)
    about_us = driver.find_element_by_css_selector(".nav__item:nth-of-type(2) .nav__item-link")
    hover = ActionChains(driver).move_to_element(about_us)
    hover.perform()
    press = driver.find_element_by_css_selector(
        'li:nth-of-type(2) > .nav__sub-menu > li:nth-of-type(2) > .nav__sub-menu-link'
    ).click()
    url = "https://sibedge.com/en/press/"
    assert driver.current_url == url, "URL /press не совпадет"


def test_about_us_3(driver):
    driver.get(link)
    about_us = driver.find_element_by_css_selector(".nav__item:nth-of-type(2) .nav__item-link")
    hover = ActionChains(driver).move_to_element(about_us)
    hover.perform()
    blog = driver.find_element_by_css_selector(
        'li:nth-of-type(2) > .nav__sub-menu > li:nth-of-type(3) > .nav__sub-menu-link'
    ).click()
    url = "https://sibedge.com/en/blog/"
    assert driver.current_url == url, "URL /blog не совпадает"


def test_about_us_4(driver):
    driver.get(link)
    about_us = driver.find_element_by_css_selector(".nav__item:nth-of-type(2) .nav__item-link")
    hover = ActionChains(driver).move_to_element(about_us)
    hover.perform()
    subscribe_to_us = driver.find_element_by_css_selector(
        "li:nth-of-type(5) > .nav__sub-menu-link"
    ).click()
    assert len(driver.find_element_by_css_selector(
        ".feedback-form.js--email-subscribe-form.js--form.visible > form[method='post'] > .feedback-form__title"
    ).text) != 0
    close_button = driver.find_element_by_css_selector(
        ".feedback-form.js--email-subscribe-form.js--form.visible > form[method='post']  .feedback-form__close.js--form-close > svg"
    ).click()


def test_services_1(driver):
    driver.get(link)
    services = driver.find_element_by_css_selector(".nav__item:nth-of-type(3) .nav__item-link")
    hover = ActionChains(driver).move_to_element(services)
    hover.perform()
    service_1 = driver.find_element_by_css_selector(
        'li:nth-of-type(3) > .nav__sub-menu > li:nth-of-type(1) > .nav__sub-menu-link'
    ).click()
    url = "https://sibedge.com/en/services/development/"
    assert driver.current_url == url, "URL не совпадет"


def test_services_2(driver):
    driver.get(link)
    services = driver.find_element_by_css_selector(".nav__item:nth-of-type(3) .nav__item-link")
    hover = ActionChains(driver).move_to_element(services)
    hover.perform()
    service_2 = driver.find_element_by_css_selector(
        'li:nth-of-type(3) > .nav__sub-menu > li:nth-of-type(2) > .nav__sub-menu-link'
    ).click()
    url = "https://sibedge.com/en/services/qa/"
    assert driver.current_url == url, "URL не совпадет"


def test_services_3(driver):
    driver.get(link)
    services = driver.find_element_by_css_selector(".nav__item:nth-of-type(3) .nav__item-link")
    hover = ActionChains(driver).move_to_element(services)
    hover.perform()
    service_3 = driver.find_element_by_css_selector(
        'li:nth-of-type(3) > .nav__sub-menu > li:nth-of-type(3) > .nav__sub-menu-link'
    ).click()
    url = "https://sibedge.com/en/services/devops/"
    assert driver.current_url == url, "URL не совпадет"

def test_services_4(driver):
    driver.get(link)
    services = driver.find_element_by_css_selector(".nav__item:nth-of-type(3) .nav__item-link")
    hover = ActionChains(driver).move_to_element(services)
    hover.perform()
    service_4 = driver.find_element_by_css_selector(
        'li:nth-of-type(3) > .nav__sub-menu > li:nth-of-type(4) > .nav__sub-menu-link'
    ).click()
    url = "https://sibedge.com/en/services/r-d/"
    assert driver.current_url == url, "URL не совпадет"

def test_models(driver):
    driver.get(link)
    models = driver.find_element_by_css_selector(
        ".header__nav.js--header-nav > .nav > li:nth-of-type(4) > .nav__item-link"
    ).click()
    header = driver.find_element_by_css_selector(".redesign-header__title").text
    assert header != 0


def test_projects(driver):
    driver.get(link)
    projects = driver.find_element_by_css_selector(
        ".header__nav.js--header-nav > .nav > li:nth-of-type(5) > .nav__item-link"
    ).click
    header = driver.find_element_by_css_selector(
        ".redesign-header__subtitle-text"
    ).text
    assert len(header) != 0

def test_clients(driver):
    driver.get(link)
    clients = driver.find_element_by_css_selector(
        ".header__nav.js--header-nav > .nav > li:nth-of-type(6) > .nav__item-link"
    ).click
    header = driver.find_element_by_css_selector(
        ".redesign-header__subtitle-text"
    ).text
    assert len(header) != 0

def test_contacts(driver):
    driver.get(link)
    contacts = driver.find_element_by_css_selector(
        ".header__nav.js--header-nav > .nav > li:nth-of-type(7) > .nav__item-link"
    ).click()
    header = driver.find_element_by_css_selector(
        ".redesign-discuss-project-content__contacts-second > .redesign-discuss-project-content__contacts-second-title"
    ).text
    assert len(header) != 0

def test_main_logo(driver):
    driver.get(link)
    logo = driver.find_element_by_css_selector(
        ".header__logo > svg"
    ).click()
    url = "https://sibedge.com/en/"
    assert driver.current_url == url

def test_get_in_touch(driver):
    driver.get(link)
    button = driver.find_element_by_css_selector(
        ".header__mail-button"
    ).click()
    header = driver.find_element_by_css_selector(
        ".feedback-form.js--feedback-form.js--form.visible > form[method='post'] > .feedback-form__title"
    ).text
    assert  "Share" in header
    close_button = driver.find_element_by_css_selector(
        ".feedback-form.js--feedback-form.js--form.visible > form[method='post']  .feedback-form__close.js--form-close > svg"
    ).click()

class TestForms():
    @pytest.mark.parametrize('data', ["Daniel", "Джордж"])
    def test_write_to_us(self, driver):
        button = driver.find_element_by_css_selector(
            ".header__mail-button"
        ).click()

        name = driver.find_element_by_css_selector(
            ".feedback-form.js--feedback-form.js--form.visible > form[method='post'] > div:nth-of-type(3) > .feedback-form__placeholder.js--form-placeholder.feedback-form.js--feedback-form.js--form.visible > form[method='post'] > div:nth-of-type(3) > .feedback-form__placeholder.js--form-placeholder"
        ).click()
        name.send_keys(f"{data}")


        email = driver.find_element_by_css_selector(
            ".feedback-form.js--feedback-form.js--form.visible > form[method='post'] > div:nth-of-type(5) > .feedback-form__placeholder.js--form-placeholder"
        ).click()
        email.send_keys("test@email.ru")

        company = driver.find_element_by_css_selector(
            ".feedback-form.js--feedback-form.js--form.visible > form[method='post'] > div:nth-of-type(6) > .feedback-form__placeholder.js--form-placeholder"
        ).click()
        company.send_keys("Test Company Name!")

        phone = driver.find_element_by_css_selector(
            '.feedback-form__field.js--form-field.valid-invisible-success > .feedback-form__placeholder.js--form-placeholder'
        ).click()
        phone.send_keys("+79994520296")

        message = driver.find_element_by_css_selector(
            'div:nth-of-type(8) > .feedback-form__placeholder.js--form-placeholder'
        ).click
        message.send_keys('Hello, World! This is test automated script.')



