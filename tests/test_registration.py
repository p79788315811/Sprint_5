import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from constants import REGISTER_PAGE_URL
from helpers import generate_name, generate_password, generate_unique_email, dismiss_overlay


class TestRegistration:
    def test_successful_registration(self, driver):
        """Успешная регистрация с паролем от 6 символов."""
        driver.get(REGISTER_PAGE_URL)
        wait = WebDriverWait(driver, 10)
        dismiss_overlay(driver)
        wait.until(EC.visibility_of_element_located(REGISTER_NAME_INPUT))

        driver.find_element(*REGISTER_NAME_INPUT).send_keys(generate_name())
        driver.find_element(*REGISTER_EMAIL_INPUT).send_keys(generate_unique_email())
        driver.find_element(*REGISTER_PASSWORD_INPUT).send_keys(generate_password())
        driver.find_element(*REGISTER_SUBMIT_BUTTON).click()

        # маркер успеха — переход к форме входа (проверка только в ассерте)
        assert wait.until(EC.visibility_of_element_located(SUCCESS_REGISTRATION))

    def test_invalid_password_error(self, driver):
        """Короткий пароль (менее 6 символов) показывает ошибку."""
        driver.get(REGISTER_PAGE_URL)
        wait = WebDriverWait(driver, 10)
        dismiss_overlay(driver)
        wait.until(EC.visibility_of_element_located(REGISTER_NAME_INPUT))

        driver.find_element(*REGISTER_NAME_INPUT).send_keys(generate_name())
        driver.find_element(*REGISTER_EMAIL_INPUT).send_keys(generate_unique_email())
        driver.find_element(*REGISTER_PASSWORD_INPUT).send_keys("12345")
        driver.find_element(*REGISTER_SUBMIT_BUTTON).click()

        # маркер ошибки проверяем прямо в ассерте
        assert wait.until(EC.visibility_of_element_located(PASSWORD_ERROR))