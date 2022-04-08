from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/'


def go_to_link_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, '#login_link')
    login_link.click()


def test_quest_can_go_to_login_link(browser):
    browser.get(link)
    go_to_link_page(browser)
