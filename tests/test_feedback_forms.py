from pages.feedback_forms import FeedBackForms, LINK


def test_send_write_to_us_form(driver):
    page = FeedBackForms(driver, LINK)
    page.open()
    page.accept_cookie()
    page.open_and_send_write_to_us_form()


