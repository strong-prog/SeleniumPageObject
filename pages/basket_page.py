from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.INFO_ABOUT_PRODUCT_BASKET), \
            'Инфо о товарах в корзине должно отсутствовать!'

    def should_be_text_that_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.INFO_ABOUT_EMPTY_BASKET),\
            'Отсутствует информация, что корзина пуста!'
