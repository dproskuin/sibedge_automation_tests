from selenium import webdriver
import pytest

link = "https://sibedge.com/en/"


class TestForms():

    @pytest.mark.parametrize('language', ["en", "ru"])
    def test_user_should_see_main_page(self, driver, language):
        link = f"https://sibedge.com/{language}/"
        driver.get(link)
        url = driver.current_url
        assert url == link, "URL не совпадают"


    def test_write_to_us(self, driver):

        driver.get(link)
        button = driver.find_element_by_css_selector(
            ".header__mail-button"
        ).click()

        name = driver.find_element_by_css_selector(
            ".feedback-form.js--feedback-form.js--form.visible > form[method='post'] > div:nth-of-type(3) > .feedback-form__placeholder.js--form-placeholder.feedback-form.js--feedback-form.js--form.visible > form[method='post'] > div:nth-of-type(3) > .feedback-form__placeholder.js--form-placeholder"
        ).click()
        name.send_keys("Name")

        email = driver.find_element_by_css_selector(
            ".feedback-form.js--feedback-form.js--form.visible > form[method='post'] > div:nth-of-type(5) > .feedback-form__placeholder.js--form-placeholder"
        ).click()
        email.send_keys("test@email.ru")

        company = driver.find_element_by_css_selector(
            ".feedback-form.js--feedback-form.js--form.visible > form[method='post'] > div:nth-of-type(6) > .feedback-form__placeholder.js--form-placeholder"
        ).click()
        company.send_keys("Test Company Name!")

        phone = driver.find_element_by_css_selector(
            '.feedback-form__field.js--form-field.valid-invisible-success > .feedback-form__placeholder.js--form-placeholder'
        ).click()
        phone.send_keys("+79994520296")

        message = driver.find_element_by_css_selector(
            'div:nth-of-type(8) > .feedback-form__placeholder.js--form-placeholder'
        ).click
        message.send_keys('Hello, World! This is test automated script.')


