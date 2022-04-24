import time

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_basket_link(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BASKET),\
            'Ссылка на добавление в козину не найдена!'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PROD_MESSAGE), \
            'Сообщение о добавлении товара должно отсутствовать!'

    def should_is_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.PROD_MESSAGE), \
            'Сообщение о добавлении товара не исчезло!'

    def add_product_to_basket(self):
        add_basket_link = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        add_basket_link.click()

    def should_be_correct_text_product_in_message(self):
        message_product_text = self.browser.find_element(*ProductPageLocators.PROD_MESSAGE).text
        fact_product_text = self.browser.find_element(*ProductPageLocators.PROD_FACT).text
        assert message_product_text == fact_product_text,\
            'Товар в сообщении не соответствует выбраному товару!'

    def should_be_correct_text_price_in_message(self):
        message_price_text = self.browser.find_element(*ProductPageLocators.PRICE_MASSAGE).text
        fact_price_text = self.browser.find_element(*ProductPageLocators.PRICE_FACT).text
        assert message_price_text == fact_price_text,\
            'Цена в сообщении не соответствует цене товара!'
