from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import math


class BasePage:

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        # Проверка присутствия элемента.
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        # Проверка отсутствия элемента.
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        # Проверка, что элемент исчезнет.
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def solve_quiz_and_get_code(self):
        # Переход на alert, вычисление числа и ввод числа.
        WebDriverWait(self.browser, 3).until(EC.alert_is_present())
        alert = self.browser.switch_to.alert
        x = alert.text.split(' ')[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()


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
