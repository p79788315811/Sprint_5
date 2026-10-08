import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from constants import MAIN_PAGE_URL, REGISTER_PAGE_URL, RECOVERY_PAGE_URL
from helpers import dismiss_overlay, fill_and_submit_login


class TestLogin:
    def test_login_via_main_button(self, driver, registered_user):
        """Вход по кнопке «Войти в аккаунт» на главной."""
        wait = WebDriverWait(driver, 10)
        driver.get(MAIN_PAGE_URL)
        dismiss_overlay(driver)
        wait.until(EC.element_to_be_clickable(LOGIN_BUTTON_MAIN))
        driver.find_element(*LOGIN_BUTTON_MAIN).click()
        fill_and_submit_login(driver, registered_user)
        # маркер успеха входа — рабочая область конструктора
        assert wait.until(EC.visibility_of_element_located(CONSTRUCTOR_TITLE))

    def test_login_via_personal_account(self, driver, registered_user):
        """Вход через кнопку «Личный Кабинет»."""
        wait = WebDriverWait(driver, 10)
        driver.get(MAIN_PAGE_URL)
        dismiss_overlay(driver)
        wait.until(EC.element_to_be_clickable(PROFILE_BUTTON))
        driver.find_element(*PROFILE_BUTTON).click()
        fill_and_submit_login(driver, registered_user)
        assert wait.until(EC.visibility_of_element_located(CONSTRUCTOR_TITLE))

    def test_login_from_registration_form(self, driver, registered_user):
        """Вход через ссылку «Войти» на форме регистрации."""
        wait = WebDriverWait(driver, 10)
        driver.get(REGISTER_PAGE_URL)
        dismiss_overlay(driver)
        wait.until(EC.element_to_be_clickable(LOGIN_LINK_FROM_REGISTER))
        driver.find_element(*LOGIN_LINK_FROM_REGISTER).click()
        fill_and_submit_login(driver, registered_user)
        assert wait.until(EC.visibility_of_element_located(CONSTRUCTOR_TITLE))

    def test_login_from_recovery_form(self, driver, registered_user):
        """Вход через ссылку «Войти» на форме восстановления пароля."""
        wait = WebDriverWait(driver, 10)
        driver.get(RECOVERY_PAGE_URL)
        dismiss_overlay(driver)
        wait.until(EC.element_to_be_clickable(LOGIN_LINK_FROM_RECOVERY))
        driver.find_element(*LOGIN_LINK_FROM_RECOVERY).click()
        fill_and_submit_login(driver, registered_user)
        assert wait.until(EC.visibility_of_element_located(CONSTRUCTOR_TITLE))