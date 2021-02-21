from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import FeedbackFormLocators, MainPageLocators
import pytest
import time

link = "https://se.sibedge.com/en/"

class FeedBackForms(BasePage):

    def accept_cookie(self):

        cookies_accept = self.driver.find_element(By.CSS_SELECTOR,
            ".cookie-alert__button.cookie-alert__button--agree.js--cookie-alert-allow")
        cookies_accept.click()

    def open_and_send_write_to_us_form(self):

        button = self.driver.find_element(By.CSS_SELECTOR, MainPageLocators.HEADER_FORM_BUTTON)
        button.click()

        name = self.driver.find_element(By.NAME, FeedbackFormLocators.NAME_FIELD)
        name.click()
        name.send_keys("SomeTestName")
        time.sleep(2)

        email = self.driver.find_element(By.NAME, FeedbackFormLocators.EMAIL_FIELD)
        email.click()
        email.send_keys("testemail@email.com")

        phone = self.driver.find_element(By.NAME, FeedbackFormLocators.PHONE_FIELD)
        phone.click()
        phone.send_keys("+79513454323")

        message = self.driver.find_element(By.NAME, FeedbackFormLocators.MESSAGE_FIELD)
        message.click()
        message.send_keys("Hello! This is the automated test message for Message field. Have a good day!")

        send_button = self.driver.find_element(By.NAME, FeedbackFormLocators.SUBMIT_BUTTON)
        send_button.click()

        time.sleep(5)