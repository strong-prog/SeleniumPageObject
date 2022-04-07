import pytest
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/'


def test_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, '#login_link')


@pytest.xfail
def test_login_link_fail(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, '#magic_link')
