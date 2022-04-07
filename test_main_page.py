from selenium.webdriver.common.by import By


def test_quest_can_go_to_login_link(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    browser.get(link)
    login_link = browser.find_element(By.CSS_SELECTOR, '#login_link')
    login_link.click()
