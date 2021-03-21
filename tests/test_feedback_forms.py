import allure
from pages.feedback_forms import FeedBackForms
"""Here are located test cases for site pages.

Executing:
Type 'pytest [filename] (test_main_page.py)'
to the command line to execute test cases

Parameters:
Choose browser language: --browser_language=[ru]/[en] 
-v = verbose mode
-m = run marked tests
-s = string output

Creating allure report:
1) pytest --alluredir=[dir] [test_file.py]
3) allure serve [dir].
"""

@allure.severity(allure.severity_level.CRITICAL)
def test_send_write_to_us_form(driver):
    page = FeedBackForms(driver)
    page.accept_cookie()
    page.open_and_send_write_to_us_form()

@allure.severity(allure.severity_level.CRITICAL)
def test_send_subscribe_to_us_form(driver):
    page = FeedBackForms(driver)
    page.open_about_us_and_form()
    page.open_and_send_subscribe_to_us_form()

@allure.severity(allure.severity_level.CRITICAL)
def test_send_main_page_form(driver):
    page = FeedBackForms(driver)
    page.open_and_send_main_page_form()

@allure.severity(allure.severity_level.CRITICAL)
def test_send_models_page_form(driver):
    page = FeedBackForms(driver)
    page.open_and_send_models_page_form()

@allure.severity(allure.severity_level.CRITICAL)
def test_send_about_us_page_form(driver):
    page = FeedBackForms(driver)
    page.open_and_send_about_us_page_form()

@allure.severity(allure.severity_level.CRITICAL)
def test_send_contacts_page_form(driver):
    page = FeedBackForms(driver)
    page.open_and_send_contacts_page_form()

@allure.severity(allure.severity_level.NORMAL)
def test_send_blog_page_form(driver):
    page = FeedBackForms(driver)
    page.open_and_send_blog_page_form()

@allure.severity(allure.severity_level.NORMAL)
def test_send_development_service_form(driver):
    page = FeedBackForms(driver)
    page.open_and_send_development_service_form()

@allure.severity(allure.severity_level.NORMAL)
def test_send_extension_service_form(driver):
    page = FeedBackForms(driver)
    page.open_and_send_extension_service_form()

@allure.severity(allure.severity_level.NORMAL)
def test_send_squads_service_form(driver):
    page = FeedBackForms(driver)
    page.open_and_send_squads_service_form()

@allure.severity(allure.severity_level.NORMAL)
def test_send_devops_service_form(driver):
    page = FeedBackForms(driver)
    page.open_and_send_devops_service_form()

@allure.severity(allure.severity_level.NORMAL)
def test_send_qa_service_form(driver):
    page = FeedBackForms(driver)
    page.open_and_send_qa_service_form()

@allure.severity(allure.severity_level.NORMAL)
def test_send_agile_article_form(driver):
    page = FeedBackForms(driver)
    page.open_and_send_agile_article_form()

@allure.severity(allure.severity_level.NORMAL)
def test_send_pitfalls_article_form(driver):
    page = FeedBackForms(driver)
    page.open_and_send_pitfalls_article_form()

@allure.severity(allure.severity_level.NORMAL)
def test_send_cto_article_form(driver):
    page = FeedBackForms(driver)
    page.open_and_send_cto_article_form()

@allure.severity(allure.severity_level.NORMAL)
def test_send_anchorfree_case_form(driver):
    page = FeedBackForms(driver)
    page.open_and_send_anchorfree_case_form()

