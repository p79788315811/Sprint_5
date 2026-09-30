import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import random
import string
from locators import MAIN_PAGE_URL


# Генераторы данных
def generate_email():
    """Генерирует уникальный email в формате имя_фамилия_когорта_цифры@домен"""
    name = ''.join(random.choices(string.ascii_lowercase, k=5))
    surname = ''.join(random.choices(string.ascii_lowercase, k=7))
    cohort = random.randint(1000, 9999)
    digits = random.randint(100, 999)
    domain = random.choice(['yandex.ru', 'mail.ru', 'gmail.com'])
    return f"{name}_{surname}_{cohort}_{digits}@{domain}"


def generate_password():
    """Генерирует пароль длиной 8 символов"""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=8))

def generate_name():
    """Генерирует случайное имя"""
    return ''.join(random.choices(string.ascii_lowercase, k=6)).capitalize()

# Фикстура для выбора браузера
@pytest.fixture(params=['chrome', 'firefox'], scope='session')
def browser_type(request):
    """Фикстура для параметризации браузеров"""
    return request.param

# Основная фикстура драйвера
@pytest.fixture
def driver(browser_type):
    """Основная фикстура для управления драйвером"""
    if browser_type == 'chrome':
        options = ChromeOptions()
        # options.add_argument('--headless')  # Раскомментируйте для безголового режима
        driver = webdriver.Chrome(options=options)
    elif browser_type == 'firefox':
        options = FirefoxOptions()
        # options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser_type}")

    driver.get(MAIN_PAGE_URL)
    driver.maximize_window()

    yield driver

    # Гарантированное закрытие браузера
    try:
        driver.quit()
    except Exception as e:
        print(f"Ошибка при закрытии драйвера: {e}")

# Фикстура с данными пользователя
@pytest.fixture
def user_data():
    """Фикстура с данными для регистрации/авторизации"""
    return {
        'email': generate_email(),
        'password': generate_password(),
        'name': generate_name()
    }
