from pages.feedback_forms import FeedBackForms, link
import pytest
from datetime import datetime
import time


def test_send_write_to_us_form(driver):
    page = FeedBackForms(driver, link)
    page.open()
    page.accept_cookie()
    page.open_and_send_write_to_us_form()


