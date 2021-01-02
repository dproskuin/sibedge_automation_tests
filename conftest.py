import pytest
from selenium import webdriver

@pytest.fixture(autouse=True, scope='function')
def driver():
    print('\nStart browser for test...')
    driver = webdriver.Chrome()
    yield driver
    print('\nquit browser..')
    driver.quit()