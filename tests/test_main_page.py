import allure
from pages.main_page import MainPage, LINK
"""
Here are located all test cases, type 'pytest -v test_main_page.py' 
in command line to execute test cases  
Parameters:
Choose browser language: --browser_language=[ru]/[en]  
Create .html report: --html=[path/name].html --self-contained-html --capture sys 
for capturing output
For creating allure report: 
1) pytest -v -s --alluredir='dir' 'test_file.py' 
3) allure serve 'dir'
"""

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
def test_user_can_go_to_main_page_by_clicking_to_logo(driver):
    page = MainPage(driver, LINK)
    page.open()
    page.accept_cookie()
    page.open_main_page_by_click_to_logo()

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
def test_open_subscribe_to_us_form(driver):
    page = MainPage(driver, LINK)
    page.open()
    page.accept_cookie()
    page.open_subscribe_to_us_form()

@allure.severity(allure.severity_level.CRITICAL)
def test_open_sitemap_page(driver):
    page = MainPage(driver, LINK)
    page.open()
    page.accept_cookie()
    page.open_sitemap_page()