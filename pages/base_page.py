from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import math


class BasePage:

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        WebDriverWait(self.browser, 3).until(EC.alert_is_present())
        alert = self.browser.switch_to.alert
        print('Переход на первый alert.')
        x = alert.text.split(' ')[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        print(f'Ввод ответа: {answer}')
        alert.send_keys(answer)
        alert.accept()
        print('Клик на подтверждение.')


'''
        WebDriverWait(self.browser, 3).until(EC.alert_is_present())
        try:
            alert = self.browser.switch_to.alert
            print('Переход на второй alert.')
            alert_text = alert.text
            print(f'Ваш код: {alert_text}')
            alert.accept()
            print('Клик на подтверждение.')
        except NoSuchElementException:
            print('Второе оповещение не найдено!')
'''