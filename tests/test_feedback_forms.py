from pages.feedback_forms import FeedBackForms, LINK

def test_send_write_to_us_form(driver):

    page = FeedBackForms(driver, LINK)
    page.open()
    page.accept_cookie()
    page.open_and_send_write_to_us_form()

def test_send_subscribe_to_us_form(driver):

    page = FeedBackForms(driver, LINK)
    page.open()
    page.open_about_us_and_form()
    page.open_and_send_subscribe_to_us_form()

def test_send_main_page_form(driver):

    page = FeedBackForms(driver, LINK)
    page.open_and_send_main_page_form()

def test_send_models_page_form(driver):

    page = FeedBackForms(driver, LINK)
    page.open_and_send_models_page_form()

def test_send_about_us_page_form(driver):

    page = FeedBackForms(driver, LINK)
    page.open_and_send_about_us_page_form()

def test_send_contacts_page_form(driver):

    page = FeedBackForms(driver, LINK)
    page.open_and_send_contacts_page_form()

def test_send_blog_page_form(driver):

    page = FeedBackForms(driver, LINK)
    page.open_and_send_blog_page_form()



