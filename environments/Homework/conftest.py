import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def browser():
    print('\nstart browser for test..')
    browser_obj = webdriver.Chrome()
    yield browser_obj
    print('\nbrowser quit')
    browser_obj.quit()


# для корректного отображения кириллицы в параметризаторах
def pytest_make_parametrize_id(config, val): return repr(val)


# добавляем параметр запуска тестов в командной строке(чем запускать, хромом или фаерфоксом) По умолчанию хром
def pytest_addoption(parser):
    # parser.addoption('--browser_name', action='store', default=None, help="Choose browser: chrome or firefox")
    # Можно задать значение параметра по умолчанию,
    # чтобы в командной строке не обязательно было указывать параметр --browser_name, например, так:
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")

    parser.addoption('--language', action='store', default=None,
                     help="Choose language: '--language=en', '--language=ru'")


# Запуск браузера(для каждой функции)
@pytest.fixture(scope="function")  # по умолчанию запускается для каждой функции
def browser(request):
    browser_name = request.config.getoption("browser_name")  # получаем параметр командной строки browser_name
    user_language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    # options_firefox = OptionsFirefox()
    # options_firefox.set_preference("intl.accept_languages", user_language)

    browser_chr = webdriver.Chrome(options=options)
    browser_chr.set_preference("intl.accept_languages", user_language)
    browser = None
    if browser_name == "chrome":
        print("\nstart Сhrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart Firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
