"""Here are located test cases for site pages.

Executing:
Type 'pytest [filename] (test_main_page.py)'
to the command line to execute test cases

Parameters:
Choose browser language: --browser_language=[ru]/[en]
-v = verbose mode
-m = run marked tests
-s = string output
for rerunning failure tests == --reruns [number]
Creating allure report:
1) pytest --alluredir=[dir] [test_file.py]
3) allure serve [dir].
"""
import allure
from pages.main_page import MainPage, LINK

@allure.severity(allure.severity_level.CRITICAL)
def test_user_can_go_to_models_page(driver):
    page = MainPage(driver, LINK)
    page.open()
    page.accept_cookie()
    page.open_models_page()

@allure.severity(allure.severity_level.CRITICAL)
def test_user_can_go_to_projects_page(driver):
    page = MainPage(driver, LINK)
    page.open()
    page.accept_cookie()
    page.open_projects_page()

@allure.severity(allure.severity_level.CRITICAL)
def test_user_can_go_to_clients_page(driver):
    page = MainPage(driver, LINK)
    page.open()
    page.accept_cookie()
    page.open_clients_page()

@allure.severity(allure.severity_level.CRITICAL)
def test_user_can_go_to_contacts_page(driver):
    page = MainPage(driver, LINK)
    page.open()
    page.accept_cookie()
    page.open_contacts_page()

@allure.severity(allure.severity_level.CRITICAL)
def test_user_can_go_to_development_page(driver):
    page = MainPage(driver, LINK)
    page.open()
    page.accept_cookie()
    page.open_development_page()

@allure.severity(allure.severity_level.CRITICAL)
def test_user_can_go_to_qa_page(driver):
    page = MainPage(driver, LINK)
    page.open()
    page.accept_cookie()
    page.open_qa_page()

@allure.severity(allure.severity_level.CRITICAL)
def test_user_can_go_to_devops_page(driver):
    page = MainPage(driver, LINK)
    page.open()
    page.accept_cookie()
    page.open_devops_page()

@allure.severity(allure.severity_level.CRITICAL)
def test_user_can_go_to_squads_product_page(driver):
    page = MainPage(driver, LINK)
    page.open()
    page.accept_cookie()
    page.open_squads_product_page()

@allure.severity(allure.severity_level.CRITICAL)
def test_user_can_open_get_in_touch_form(driver):
    page = MainPage(driver, LINK)
    page.open()
    page.accept_cookie()
    page.open_get_in_touch_form()
    page.close_get_in_touch_form()

@allure.severity(allure.severity_level.CRITICAL)
def test_user_can_go_to_team_extension_page(driver):
    page = MainPage(driver, LINK)
    page.open()
    page.accept_cookie()
    page.open_team_extension_page()

@allure.severity(allure.severity_level.CRITICAL)
def test_open_why_sibedge_page(driver):
    page = MainPage(driver, LINK)
    page.open()
    page.accept_cookie()
    page.open_why_sibedge_page()

@allure.severity(allure.severity_level.CRITICAL)
def test_open_press_page(driver):
    page = MainPage(driver, LINK)
    page.open()
    page.accept_cookie()
    page.open_press_page()

@allure.severity(allure.severity_level.CRITICAL)
def test_open_blog_page(driver):
    page = MainPage(driver, LINK)
    page.open()
    page.accept_cookie()
    page.open_blog_page()


@allure.severity(allure.severity_level.CRITICAL)
def test_open_sitemap_page(driver):
    page = MainPage(driver, LINK)
    page.open()
    page.accept_cookie()
    page.open_sitemap_page()
