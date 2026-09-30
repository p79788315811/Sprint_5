import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

class TestLogin:
    def test_login_from_main(self, driver):
        driver.get(MAIN_PAGE_URL)  # Используем обновлённый URL ← URL ИЗМЕНЁН**
        driver.find_element(By.XPATH, LOGIN_BUTTON_MAIN).click()
        self._perform_login(driver)

    def test_login_from_personal_account(self, driver):
        driver.get(MAIN_PAGE_URL)  # Используем обновлённый URL ← URL ИЗМЕНЁН**
        driver.find_element(By.XPATH, PERSONAL_ACCOUNT_BUTTON).click()
        self._perform_login(driver)

    def _perform_login(self, driver):
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, EMAIL_INPUT_LOGIN)))

        driver.find_element(By.XPATH, EMAIL_INPUT_LOGIN).send_keys("test@test.ru")
        driver.find_element(By.XPATH, PASSWORD_INPUT_LOGIN).send_keys("123456")
        driver.find_element(By.XPATH, SUBMIT_LOGIN_BUTTON).click()

        wait.until(EC.url_contains("account"))
        assert "account" in driver.current_url
