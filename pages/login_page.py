from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # Проверка на корректный url адрес.
        assert 'login' in self.browser.current_url,\
            'Некорректный url адрес'

    def should_be_login_form(self):
        # Проверка, что есть форма логина.
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM),\
            'Форма логина не найдена!'

    def should_be_register_form(self):
        # Проверка, что есть форма регистрации на странице.
        assert self.is_element_present(*LoginPageLocators.REG_FORM),\
            'Форма регистрации не найдена!'

    def register_new_user(self):
        email = str(time.time()) + '@strong.org'
        password = '092303920'
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_input.send_keys(email)
        password_one_input = self.browser.find_element(*LoginPageLocators.PASSWORD_ONE_INPUT)
        password_one_input.send_keys(password)
        password_two_input = self.browser.find_element(*LoginPageLocators.PASSWORD_TWO_INPUT)
        password_two_input.send_keys(password)
        button_registration = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION)
        button_registration.click()

