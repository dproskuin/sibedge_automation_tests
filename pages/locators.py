from selenium.webdriver.common.by import By
"""
Here are located locators for elements. 
Structure - Page (class) -> Locator for element (constant) 
"""



class ModelsPageLocators():

    MODELS_HEADER = (By.CSS_SELECTOR, ".redesign-header__title")

class ProjectsPageLocators():

    PROJECTS_HEADER = (By.CSS_SELECTOR, ".redesign-header__title")

class ClientsPageLocators():

    CLIENTS_HEADER = (By.CSS_SELECTOR, ".redesign-header__subtitle-text")
    CLIENTS_TITLE = (By.CSS_SELECTOR, ".redesign-header__title")

class ContactsPageLocators():

    CONTACTS_HEADER = (By.CSS_SELECTOR,
    ".redesign-discuss-project-content__contacts-second > .redesign-discuss-project-content__contacts-second-title"
     )

    CONTACTS_ADRESSES_LIST = (By.CSS_SELECTOR, ".redesign-contacts-representation > .js--container-elements.redesign-contacts-representation-list")

class DevelopmentPageLocators():

    DEVELOPMENT_HEADER = (By.CSS_SELECTOR, ".contain-within.redesign-header.redesign-page__header > .redesign-header__title")

class QaPageLocators():

    QA_HEADER = (By.CSS_SELECTOR, ".contain-within.redesign-header.redesign-page__header > .redesign-header__title")

class DevopsPageLocators():

    DEVOPS_HEADER = (By.CSS_SELECTOR, ".contain-within.redesign-header.redesign-page__header > .redesign-header__title")

class SquadsProductLocators():

    SQUADS_PRODUCT_HEADER = (By.CSS_SELECTOR, "li:nth-of-type(3) > .nav__sub-menu > li:nth-of-type(3) > .nav__sub-menu-link")

class TeamExtensionLocators():

    TEAMEXTENSION_HEADER = (By.CSS_SELECTOR, ".redesign-header__title-highlight")

class WhySibedgePageLocators():

    WHYSIBEDGE_HEADER = (By.CSS_SELECTOR, "header > .redesign-header__title")

class PressPageLocators():

    PRESS_HEADER = (By.CSS_SELECTOR, ".main-slider__title")

class BlogPageLocators():

    BLOG_HEADER = (By.CSS_SELECTOR, ".redesign-header__title-highlight")

class MainPageLocators():

    MAIN_URL = ("https://se.sibedge.com/en/")

    HEADER_FORM_BUTTON = ".header__mail-button > .header__mail-button-text"

class SubscribeToUsFormLocators():

    SUBSCRIBETOUS_HEADER = (By.CSS_SELECTOR, ".feedback-form.js--email-subscribe-form.js--form.visible > form[method='post'] > .feedback-form__title")

class GetInTouchFormLocators():

    GETINTOUCH_HEADER = (By.CSS_SELECTOR, ".feedback-form.js--feedback-form.js--form.visible > form[method='post'] > .feedback-form__title")

class SitemapLocators():

    SITEMAP_HEADER = (By.CSS_SELECTOR, ".contain-within.sitemap-container > .sitemap-container-header")

class FeedbackFormLocators(): #geintouch

    NAME_FIELD = "user_name"

    PHONE_FIELD = "user_phone"

    EMAIL_FIELD = "user_email"

    MESSAGE_FIELD = "MESSAGE" #Company field has the same name, ask to change

    LAST_NAME_FIELD = "user_last_name"

    SUBMIT_BUTTON = "submit"

    THANK_YOU_NOTICE_MESSAGE = "feedback-form__notice"