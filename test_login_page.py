from .pages.login_page import LoginPage


def test_quest_should_be_correct_url(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
