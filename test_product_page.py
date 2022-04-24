import pytest
from .pages.product_page import ProductPage

# pytest -s -v --tb=line --browser_name=chrome --language=en test_product_page.py


@pytest.mark.skip
@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser, link):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_link()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_correct_text_product_in_message()
    page.should_be_correct_text_price_in_message()


@pytest.mark.xfail(reason='Этот баг исправят позже!')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason='Этот баг исправят позже!')
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_is_disappeared_success_message()
