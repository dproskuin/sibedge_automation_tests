from pages.main_page import MainPage, link
import pytest

@pytest.mark.regression
def test_user_can_go_to_models_page(driver):
    page = MainPage(driver, link)
    page.open()
    page.accept_cookie()
    page.open_models_page()

def test_user_can_go_to_projects_page(driver):
    page = MainPage(driver, link)
    page.open()
    page.accept_cookie()
    page.open_projects_page()

def test_user_can_go_to_clients_page(driver):
    page = MainPage(driver, link)
    page.open()
    page.accept_cookie()
    page.open_clients_page()

def test_user_can_go_to_contacts_page(driver):
    page = MainPage(driver, link)
    page.open()
    page.accept_cookie()
    page.open_contacts_page()

def test_user_can_go_to_development_page(driver):
    page = MainPage(driver, link)
    page.open()
    page.accept_cookie()
    page.open_development_page()

def test_user_can_go_to_qa_page(driver):
    page = MainPage(driver, link)
    page.open()
    page.accept_cookie()
    page.open_qa_page()

def test_user_can_go_to_devops_page(driver):
    page = MainPage(driver, link)
    page.open()
    page.accept_cookie()
    page.open_devops_page()

def test_user_can_go_to_r_d_page(driver):
    page = MainPage(driver, link)
    page.open()
    page.accept_cookie()
    page.open_r_d_page()

def test_user_can_go_to_main_page_by_clicking_to_logo(driver):
    page = MainPage(driver, link)
    page.open()
    page.accept_cookie()
    page.open_main_page_by_click_to_logo()
    url = "https://sibedge.com/en/"
    assert driver.current_url == url

def test_user_can_open_get_in_touch_form(driver):
    page = MainPage(driver, link)
    page.open()
    page.accept_cookie()
    page.open_get_in_touch_form()
    page.close_get_in_touch_form()

def test_open_why_sibedge_page(driver):
    page = MainPage(driver, link)
    page.open()
    page.accept_cookie()
    page.open_why_sibedge_page()

def test_open_press_page(driver):
    page = MainPage(driver, link)
    page.open()
    page.accept_cookie()
    page.open_press_page()

def test_open_blog_page(driver):
    page = MainPage(driver, link)
    page.open()
    page.accept_cookie()
    page.open_blog_page()


def test_open_subscribe_to_us_form(driver):
    page = MainPage(driver, link)
    page.open()
    page.accept_cookie()
    page.open_subscribe_to_us_form()



@pytest.mark.parametrize('language', ["en", "ru"])
def test_user_should_see_en_and_ru_pages(driver, language):
    link = f"https://sibedge.com/{language}/"
    driver.get(link)
    url = driver.current_url
    assert url == link, "URL не совпадают!"


