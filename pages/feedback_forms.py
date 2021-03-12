import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage
from .locators import SubscribeFormLocators, MainPageLocators, WriteToUsFormLocators

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LINK = "https://dev.sibedge.com/clients/"

"""This class describes methods for interaction with Feedback forms"""
class FeedBackForms(BasePage):

    def open_about_us_and_form(self):
        about_us = self.driver.find_element(By.CSS_SELECTOR, ".nav__item:nth-of-type(2) .nav__item-link")
        hover = ActionChains(self.driver).move_to_element(about_us)
        hover.perform()
        button = self.driver.find_element(By.CSS_SELECTOR, MainPageLocators.SUBSCRIBE_TO_US_BUTTON)
        button.click()

    def accept_cookie(self):
        cookies_accept = self.driver.find_element(By.CSS_SELECTOR,
            ".cookie-alert__button.cookie-alert__button--agree.js--cookie-alert-allow")
        cookies_accept.click()

    def open_and_send_write_to_us_form(self):
        button = self.driver.find_element(By.CSS_SELECTOR, MainPageLocators.HEADER_FORM_BUTTON)
        button.click()

        name = self.driver.find_element(By.ID, WriteToUsFormLocators.NAME_FIELD)
        name.click()
        name.send_keys('TestName')

        email = self.driver.find_element(By.ID, WriteToUsFormLocators.EMAIL_FIELD)
        email.send_keys("testemail@email.com")

        phone = self.driver.find_element(By.ID, WriteToUsFormLocators.PHONE_FIELD)
        phone.send_keys("+79513454323")

        message = self.driver.find_element(By.ID, WriteToUsFormLocators.MESSAGE_FIELD)
        message.send_keys("Hello. Have a good day!")

        send_button = self.driver.find_element(By.NAME, WriteToUsFormLocators.SEND_BUTTON)
        send_button.click()

        thank_you_notice = self.driver.find_element(
            By.CLASS_NAME, WriteToUsFormLocators.THANK_YOU_NOTICE_MESSAGE
        )

        assert thank_you_notice != 0

    def open_and_send_subscribe_to_us_form(self):

        name = self.driver.find_element(By.ID, SubscribeFormLocators.NAME_FIELD)
        name.send_keys('TestName')

        email = self.driver.find_element(By.ID, SubscribeFormLocators.EMAIL_FIELD)
        email.send_keys("testemail@email.com")

        company = self.driver.find_element(By.ID, SubscribeFormLocators.MESSAGE_FIELD)
        company.send_keys("Hello. Have a good day!")

        #captcha = self.driver.find_element(By.ID, SubscribeFormLocators.CAPTCHA)
        #captcha.click()

        #mainWin = self.driver.current_window_handle
        # move the driver to the first iFrame
        #b = self.driver.switch_to.frame(self.driver.find_elements_by_class_name("a-wa03y9u232ri"))
        #time.sleep(3)

        #checkbox = WebDriverWait(self.driver, 10).until(
        #    EC.presence_of_element_located((By.ID, "recaptcha-anchor"))
        #)
        #checkbox.click()
        #back = self.driver.switch_to.window(mainWin)

        send_button = self.driver.find_element(By.NAME, SubscribeFormLocators.SEND_BUTTON)
        send_button.click()

        thank_you_notice = self.driver.find_element(
            By.CLASS_NAME, SubscribeFormLocators.THANK_YOU_NOTICE_MESSAGE
        )

        assert thank_you_notice != 0
        time.sleep(5)
