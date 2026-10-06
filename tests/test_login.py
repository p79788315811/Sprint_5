import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from data import MAIN_PAGE_URL, REGISTER_PAGE_URL, RECOVERY_PAGE_URL, dismiss_overlay


class TestLogin:
    def _fill_and_submit_login(self, driver, user):
        wait = WebDriverWait(driver, 10)
        dismiss_overlay(driver)
        wait.until(EC.visibility_of_element_located(EMAIL_INPUT))
        driver.find_element(*EMAIL_INPUT).send_keys(user['email'])
        driver.find_element(*PASSWORD_INPUT).send_keys(user['password'])
        dismiss_overlay(driver)  # модалка может появиться позже — прячем перед кликом
        wait.until(EC.element_to_be_clickable(LOGIN_SUBMIT_BUTTON))
        driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

    def test_login_via_main_button(self, driver, registered_user):
        """Вход по кнопке «Войти в аккаунт» на главной."""
        wait = WebDriverWait(driver, 10)
        driver.get(MAIN_PAGE_URL)
        dismiss_overlay(driver)
        wait.until(EC.element_to_be_clickable(LOGIN_BUTTON_MAIN))
        driver.find_element(*LOGIN_BUTTON_MAIN).click()
        self._fill_and_submit_login(driver, registered_user)
        # маркер успеха входа — рабочая область конструктора
        assert wait.until(EC.visibility_of_element_located(CONSTRUCTOR_TITLE))

    def test_login_via_personal_account(self, driver, registered_user):
        """Вход через кнопку «Личный Кабинет»."""
        wait = WebDriverWait(driver, 10)
        driver.get(MAIN_PAGE_URL)
        dismiss_overlay(driver)
        wait.until(EC.element_to_be_clickable(PROFILE_BUTTON))
        driver.find_element(*PROFILE_BUTTON).click()
        self._fill_and_submit_login(driver, registered_user)
        assert wait.until(EC.visibility_of_element_located(CONSTRUCTOR_TITLE))

    def test_login_from_registration_form(self, driver, registered_user):
        """Вход через ссылку «Войти» на форме регистрации."""
        wait = WebDriverWait(driver, 10)
        driver.get(REGISTER_PAGE_URL)
        dismiss_overlay(driver)
        wait.until(EC.element_to_be_clickable(LOGIN_LINK_FROM_REGISTER))
        driver.find_element(*LOGIN_LINK_FROM_REGISTER).click()
        self._fill_and_submit_login(driver, registered_user)
        assert wait.until(EC.visibility_of_element_located(CONSTRUCTOR_TITLE))

    def test_login_from_recovery_form(self, driver, registered_user):
        """Вход через ссылку «Войти» на форме восстановления пароля."""
        wait = WebDriverWait(driver, 10)
        driver.get(RECOVERY_PAGE_URL)
        dismiss_overlay(driver)
        wait.until(EC.element_to_be_clickable(LOGIN_LINK_FROM_RECOVERY))
        driver.find_element(*LOGIN_LINK_FROM_RECOVERY).click()
        self._fill_and_submit_login(driver, registered_user)
        assert wait.until(EC.visibility_of_element_located(CONSTRUCTOR_TITLE))