import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import MAIN_PAGE_URL, REGISTER_PAGE_URL, LOGIN_PAGE_URL
from helpers import generate_name, generate_password, generate_unique_email, dismiss_overlay
from locators import (
    REGISTER_NAME_INPUT,
    REGISTER_EMAIL_INPUT,
    REGISTER_PASSWORD_INPUT,
    REGISTER_SUBMIT_BUTTON,
    SUCCESS_REGISTRATION,
    EMAIL_INPUT,
    PASSWORD_INPUT,
    LOGIN_SUBMIT_BUTTON,
    CONSTRUCTOR_TITLE,
)


@pytest.fixture(params=['chrome', 'firefox'], scope='session')
def browser_type(request):
    """Фикстура для параметризации браузеров."""
    return request.param


@pytest.fixture
def driver(browser_type):
    """Основная фикстура для управления драйвером."""
    if browser_type == 'chrome':
        options = ChromeOptions()
        driver = webdriver.Chrome(options=options)
    else:
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)

    driver.get(MAIN_PAGE_URL)
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture
def registered_user(driver):
    """Предусловие: регистрирует уникального пользователя и возвращает его данные."""
    user = {
        'name': generate_name(),
        'email': generate_unique_email(),
        'password': generate_password(),
    }

    driver.get(REGISTER_PAGE_URL)
    wait = WebDriverWait(driver, 10)
    dismiss_overlay(driver)
    wait.until(EC.visibility_of_element_located(REGISTER_NAME_INPUT))
    driver.find_element(*REGISTER_NAME_INPUT).send_keys(user['name'])
    driver.find_element(*REGISTER_EMAIL_INPUT).send_keys(user['email'])
    driver.find_element(*REGISTER_PASSWORD_INPUT).send_keys(user['password'])
    driver.find_element(*REGISTER_SUBMIT_BUTTON).click()
    wait.until(EC.visibility_of_element_located(SUCCESS_REGISTRATION))

    return user


@pytest.fixture
def logged_in_user(driver, registered_user):
    """Предусловие: зарегистрированный и авторизованный пользователь."""
    wait = WebDriverWait(driver, 10)
    driver.get(LOGIN_PAGE_URL)
    dismiss_overlay(driver)
    wait.until(EC.visibility_of_element_located(EMAIL_INPUT))
    driver.find_element(*EMAIL_INPUT).send_keys(registered_user['email'])
    driver.find_element(*PASSWORD_INPUT).send_keys(registered_user['password'])
    dismiss_overlay(driver)
    wait.until(EC.element_to_be_clickable(LOGIN_SUBMIT_BUTTON))
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()
    wait.until(EC.visibility_of_element_located(CONSTRUCTOR_TITLE))

    return registered_user