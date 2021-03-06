"""This module contains configurations for browser and tests."""
import pytest
from selenium import webdriver

def pytest_addoption(parser):

    parser.addoption("--browser_language", action="store", default="en",
                     help="Choose browser language: ru or en")

@pytest.fixture(autouse=True, scope="function")
def driver(request):
    """Setup and teardown options for webdriver"""
    browser_language = request.config.getoption("browser_language")

    if browser_language == "ru":

        print("\nStart browser for test...")
        options = webdriver.ChromeOptions()
        options.add_argument("--lang=ru")
        options.add_argument("--start-maximized")
        options.add_argument("--user-agent=test_agent")
        # options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)

    elif browser_language == "en":

        print("\nStart browser for test...")
        options = webdriver.ChromeOptions()
        options.add_argument("--lang=en")
        options.add_argument("--start-maximized")
        options.add_argument("--user-agent=test_agent")
        # options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)

    else:
        raise pytest.UsageError("--browser_language is invalid, supported languages: en, ru")

    yield driver
    print("\nquit browser..")
    driver.quit()
