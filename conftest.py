import pytest
from selenium import webdriver
from pages.base_page import BasePage



def pytest_addoption(parser):
    parser.addoption('--browser_language', action='store', default='en',
                     help="Choose language: ru or en")

@pytest.fixture(autouse=True, scope='function')
def driver(request):
    global driver
    browser_language = request.config.getoption("browser_language")

    if browser_language == "ru":

        print('\nStart browser for test...')
        options = webdriver.ChromeOptions()
        options.add_argument('--lang=ru')
        driver = webdriver.Chrome(chrome_options=options)

    elif browser_language == "en":

        print('\nStart browser for test...')
        options = webdriver.ChromeOptions()
        options.add_argument('--lang=en')
        driver = webdriver.Chrome(chrome_options=options)

    else:
        raise pytest.UsageError("--browser_language is invalid, supported languages: en, ru")

    yield driver
    print('\nquit browser..')
    driver.quit()


