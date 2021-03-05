from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import FeedbackFormLocators, MainPageLocators
import pytest
import time
from datetime import datetime

link = "https://se.sibedge.com/clients/"

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
        name.send_keys('TestName')

        email = self.driver.find_element(By.NAME, FeedbackFormLocators.EMAIL_FIELD)
        email.send_keys("testemail@email.com") #element is not interactable because of under placed another same name element

        phone = self.driver.find_element(By.NAME, FeedbackFormLocators.PHONE_FIELD)
        phone.send_keys("+79513454323")

        message = self.driver.find_element(By.NAME, FeedbackFormLocators.MESSAGE_FIELD)
        message.send_keys("Hello! This is the automated test message for Message field. Have a good day!")

        send_button = self.driver.find_element(By.NAME, FeedbackFormLocators.SUBMIT_BUTTON)
        send_button.click()

        thank_you_notice = self.driver.find_element(By.CLASS_NAME, FeedbackFormLocators.THANK_YOU_NOTICE_MESSAGE)

        assert thank_you_notice != 0

        time.sleep(5)

