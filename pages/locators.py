from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REG_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    ADD_BASKET = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary')
    PROD_MESSAGE = (By.CSS_SELECTOR, '.alert:nth-child(1)  strong')
    PROD_FACT = (By.CSS_SELECTOR, '.col-sm-6 h1')
    PRICE_MASSAGE = (By.CSS_SELECTOR, '.alert:nth-child(3)  strong')
    PRICE_FACT = (By.CSS_SELECTOR, '.price_color:nth-child(2)')
