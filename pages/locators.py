"""Locators for page's elements and feedback form's elements
   Structure: Page (class) -> Locators (constant=list).
"""
from selenium.webdriver.common.by import By


class ModelsPageLocators:
    MODELS_HEADER = (By.CSS_SELECTOR, ".redesign-header__title")


class ProjectsPageLocators:
    PROJECTS_HEADER = (By.CSS_SELECTOR, ".redesign-header__title")


class ClientsPageLocators:
    CLIENTS_HEADER = (By.CSS_SELECTOR, ".redesign-header__subtitle-text")

    CLIENTS_TITLE = (By.CSS_SELECTOR, ".redesign-header__title")


class ContactsPageLocators:
    CONTACTS_HEADER = (
        By.CSS_SELECTOR,
        ".redesign-discuss-project-content__contacts-second"
        " > .redesign-discuss-project-content__contacts-second-title"
    )

    CONTACTS_ADRESSES_LIST = (
        By.CSS_SELECTOR,
        ".redesign-contacts-representation"
        " > .js--container-elements.redesign-contacts-representation-list"
    )


class DevelopmentPageLocators:
    DEVELOPMENT_HEADER = (
        By.CSS_SELECTOR,
        ".contain-within.redesign-header.redesign-page__header"
        " > .redesign-header__title"
    )


class QaPageLocators:
    QA_HEADER = (
        By.CSS_SELECTOR,
        ".contain-within.redesign-header.redesign-page__header >"
        " .redesign-header__title"
    )


class DevopsPageLocators:
    DEVOPS_HEADER = (
        By.CSS_SELECTOR,
        ".contain-within.redesign-header.redesign-page__header > .redesign-header__title"
    )


class SquadsProductLocators:
    SQUADS_PRODUCT_HEADER = (By.CSS_SELECTOR,
                             "li:nth-of-type(3) > .nav__sub-menu > "
                             "li:nth-of-type(3) > .nav__sub-menu-link"
                             )


class TeamExtensionLocators:
    TEAMEXTENSION_HEADER = (By.CSS_SELECTOR, ".redesign-header__title-highlight")


class WhySibedgePageLocators:
    WHYSIBEDGE_HEADER = (By.CSS_SELECTOR, "header > .redesign-header__title")


class PressPageLocators:
    PRESS_HEADER = (By.CSS_SELECTOR, ".main-slider__title")


class BlogPageLocators:
    BLOG_HEADER = (By.CSS_SELECTOR, ".redesign-header__title-highlight")


class MainPageLocators:
    MAIN_URL = "https://se.sibedge.com/en/"

    HEADER_FORM_BUTTON = ".header__mail-button > .header__mail-button-text"

    SUBSCRIBE_TO_US_BUTTON = "li:nth-of-type(2) > .nav__sub-menu" \
                             " > li:nth-of-type(5) > .nav__sub-menu-link"

    ABOUT_US_BUTTON = ".nav__item:nth-of-type(2) .nav__item-link"

    COOKIE_ALLOW_BUTTON = ".cookie-alert__button.cookie-alert__button--agree.js" \
                          "--cookie-alert-allow"


class GetInTouchFormLocators:
    GETINTOUCH_HEADER = (By.CSS_SELECTOR,
                         ".feedback-form.js--feedback-form.js--form.visible"
                         " > form[method='post'] > .feedback-form__title"
                         )


class SitemapLocators:
    SITEMAP_HEADER = (By.CSS_SELECTOR,
                      ".contain-within.sitemap-container > .sitemap-container-header"
                      )


class SubscribeFormLocators:
    NAME_FIELD = "feedback_user_namesubscribe"

    EMAIL_FIELD = "feedback_user_emailsubscribe"

    MESSAGE_FIELD = "feedback_message_companysubscribe"

    SEND_BUTTON = \
        ".feedback-form.js--email-subscribe-form.js--form.visible" \
        " > form[method='post'] button[name='submit']"

    THANK_YOU_NOTICE_MESSAGE = "feedback-form__notice"

    SUBSCRIBE_TO_US = "nav__sub-menu-link js--form-open"


class WriteToUsFormLocators:
    NAME_FIELD = "feedback_user_namefooter"

    EMAIL_FIELD = "feedback_user_emailfooter"

    COMPANY_FIELD = "feedback_message_companyfooter"

    PHONE_FIELD = "feedback_user_phonefooter"

    MESSAGE_FIELD = "feedback_messagefooter"

    SEND_BUTTON = "submit"

    THANK_YOU_NOTICE_MESSAGE = "feedback-form__notice"


class BaseFeedbackFormLocators:
    NAME_FIELD = "user_first_name"

    LAST_NAME_FIELD = "user_last_name"

    EMAIL_FIELD = "user_email"

    COMPANY_FIELD = "user_company"

    PHONE_FIELD = "user_phone"

    MESSAGE_FIELD = "feedback_messagefooter"

    SEND_BUTTON = "submit"

    SUCCESS_MESSAGE = \
        "form[method='post'] > .alert.alert--success.feedback-form__alert"
