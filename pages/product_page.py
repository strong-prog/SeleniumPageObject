import time

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def can_add_product_to_basket(self):
        self.should_be_basket_link()
        self.add_product_to_basket()
        self.should_be_correct_text_product_in_message()
        self.should_be_correct_text_price_in_message()

    def should_be_basket_link(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BASKET), 'Ссылка на добавление в козину не найдена!'

    def add_product_to_basket(self):
        add_basket_link = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        add_basket_link.click()
        self.solve_quiz_and_get_code()

    def should_be_correct_text_product_in_message(self):
        message_product_text = self.browser.find_element(*ProductPageLocators.PROD_MESSAGE).text
        fact_product_text = self.browser.find_element(*ProductPageLocators.PROD_FACT).text
        assert message_product_text == fact_product_text, 'Товар в корзине не соответствует выбраному товару!'

    def should_be_correct_text_price_in_message(self):
        message_price_text = self.browser.find_element(*ProductPageLocators.PRICE_MASSAGE).text
        fact_price_text = self.browser.find_element(*ProductPageLocators.PRICE_FACT).text
        assert message_price_text == fact_price_text, 'Цена в корзине не соответствует цене товара!'
