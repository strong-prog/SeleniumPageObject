from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def can_add_product_to_basket(self):
        self.should_be_basket_link()
        self.add_product_to_basket()

    def should_be_basket_link(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BASKET), 'Ссылка на добавление в козину не найдена!'

    def add_product_to_basket(self):
        add_basket_link = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        add_basket_link.click()
        self.solve_quiz_and_get_code()
