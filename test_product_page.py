import pytest

from .pages.product_page import ProductPage

x_num = 7
base_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
urls = [f'{base_link}/?promo=offer{num}' for num in range(10) if num != x_num]
x_link = pytest.param(f'{base_link}/?promo=offer{x_num}', marks=pytest.mark.xfail(reason='Ошибка на странице!'))
urls.insert(x_num, x_link)


@pytest.mark.parametrize('link', urls)
def test_quest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.can_add_product_to_basket()
