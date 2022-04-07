import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        '--browser_name',
        action='store',
        default='chrome',
        help='--browser_name: chrome или firefox'
    )
    parser.addoption(
        '--language',
        action='store',
        default='en',
        help='--language: ru или en'
    )


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    browser = None
    user_language = request.config.getoption('language')
    if browser_name == 'chrome':
        print('Запуск браузера Chrome...')
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        print('Запуск браузера Firefox...')
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError('--browser_name должен быть chrome или firefox')
    yield browser
    print('Закрытие браузера...')
    browser.quit()
