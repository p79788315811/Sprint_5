import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from utils import generate_unique_email, generate_password, generate_name
class TestRegistration:
    @pytest.mark.parametrize("password", ["12345", "123456"])
    def test_successful_registration(self, driver, password):
        driver.get(MAIN_PAGE_URL)  # Используем обновлённый URL ← URL ИЗМЕНЁН**
        driver.find_element(By.XPATH, PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(By.XPATH, "//a[text()='Зарегистрироваться']").click()

        name = generate_name()
        email = generate_unique_email()

        driver.find_element(By.XPATH, NAME_INPUT_REGISTER).send_keys(name)
        driver.find_element(By.XPATH, EMAIL_INPUT_REGISTER).send_keys(email)
        driver.find_element(By.XPATH, PASSWORD_INPUT_REGISTER).send_keys(password)
        driver.find_element(By.XPATH, SUBMIT_REGISTER_BUTTON).click()


        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, CONSTRUCTOR_BUTTON)))

        assert driver.current_url == MAIN_PAGE_URL

    def test_invalid_password_error(self, driver):
        driver.get(MAIN_PAGE_URL)  # Используем обновлённый URL ← URL ИЗМЕНЁН**
        driver.find_element(By.XPATH, PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(By.XPATH, "//a[text()='Зарегистрироваться']").click()

        driver.find_element(By.XPATH, NAME_INPUT_REGISTER).send_keys("Test")
        driver.find_element(By.XPATH, EMAIL_INPUT_REGISTER).send_keys("test@test.ru")
        driver.find_element(By.XPATH, PASSWORD_INPUT_REGISTER).send_keys("123")
        driver.find_element(By.XPATH, SUBMIT_REGISTER_BUTTON).click()

        error_message = driver.find_element(By.XPATH, ERROR_MESSAGE_PASSWORD)
        assert error_message.is_displayed()
