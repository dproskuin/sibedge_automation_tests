from selenium.webdriver.common.by import By
"""Here are located locators for elements. Structure - Page (class) -> Locator for element (constant) """



class ModelsPageLocators():
    MODELS_HEADER = (By.CSS_SELECTOR, ".redesign-header__title")

class ProjectsPageLocators():
    PROJECTS_HEADER = (By.CSS_SELECTOR, ".redesign-header__title")

class ClientsPageLocators():
    CLIENTS_HEADER = (By.CSS_SELECTOR, ".redesign-header__subtitle-text")

class ContactsPageLocators():
    CONTACTS_HEADER = (By.CSS_SELECTOR, ".redesign-discuss-project-content__contacts-second > .redesign-discuss-project-content__contacts-second-title")

class DevelopmentPageLocators():
    DEVELOPMENT_HEADER = (By.CSS_SELECTOR, ".services-item__desc > .contain-within.contain-within--half.js--emulate-margin-left.services-item__desc-title.services-item__desc-title--huge")

class QaPageLocators():
    QA_HEADER = (By.CSS_SELECTOR, ".services-item__desc > .contain-within.contain-within--half.js--emulate-margin-left.services-item__desc-title.services-item__desc-title--huge")

class DevopsPageLocators():
    DEVOPS_HEADER = (By.CSS_SELECTOR, ".services-item__desc > .contain-within.contain-within--half.js--emulate-margin-left.services-item__desc-title.services-item__desc-title--huge")

class RdPageLocators():
    RD_HEADER = (By.CSS_SELECTOR, ".services-item__desc > .contain-within.contain-within--half.js--emulate-margin-left.services-item__desc-title.services-item__desc-title--huge")

class WhySibedgePageLocators():
    WHYSIBEDGE_HEADER = (By.CSS_SELECTOR, "header > .redesign-header__title")

class PressPageLocators():
    PRESS_HEADER = (By.CSS_SELECTOR, ".main-slider__title")

class BlogPageLocators():
    BLOG_HEADER = (By.CSS_SELECTOR, ".redesign-header__title-highlight")

class MainPageLocators():
    MAIN_URL = ("https://se.sibedge.com/en/")

class SubscribeToUsFormLocators():
    SUBSCRIBETOUS_HEADER = (By.CSS_SELECTOR, ".feedback-form.js--email-subscribe-form.js--form.visible > form[method='post'] > .feedback-form__title")

class GetInTouchFormLocators():
    GETINTOUCH_HEADER = (By.CSS_SELECTOR, ".feedback-form.js--feedback-form.js--form.visible > form[method='post'] > .feedback-form__title")

class SitemapLocators():
    SITEMAP_HEADER = (By.CSS_SELECTOR, ".contain-within.sitemap-container > .sitemap-container-header")