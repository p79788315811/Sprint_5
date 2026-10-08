import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from helpers import dismiss_overlay


class TestProfileNavigation:
    def test_transition_to_personal_cabinet(self, driver, logged_in_user):
        """Тест перехода в личный кабинет."""
        wait = WebDriverWait(driver, 10)
        dismiss_overlay(driver)
        wait.until(EC.element_to_be_clickable(PERSONAL_CABINET_LINK))
        driver.find_element(*PERSONAL_CABINET_LINK).click()
        # маркер успеха — ссылка «Профиль» в кабинете (только в ассерте)
        assert wait.until(EC.visibility_of_element_located(PROFILE_LINK))

    def test_transition_from_profile_to_constructor(self, driver, logged_in_user):
        """Переход из личного кабинета в конструктор через кнопку «Конструктор»."""
        wait = WebDriverWait(driver, 10)
        dismiss_overlay(driver)
        wait.until(EC.element_to_be_clickable(PERSONAL_CABINET_LINK))
        driver.find_element(*PERSONAL_CABINET_LINK).click()
        wait.until(EC.visibility_of_element_located(PROFILE_LINK))
        dismiss_overlay(driver)
        wait.until(EC.element_to_be_clickable(CONSTRUCTOR_BUTTON))
        driver.find_element(*CONSTRUCTOR_BUTTON).click()
        # маркер успеха загрузки конструктора — заголовок «Соберите бургер»
        assert wait.until(EC.visibility_of_element_located(CONSTRUCTOR_TITLE))

    def test_transition_via_logo(self, driver, logged_in_user):
        """Переход из личного кабинета в конструктор через логотип."""
        wait = WebDriverWait(driver, 10)
        dismiss_overlay(driver)
        wait.until(EC.element_to_be_clickable(PERSONAL_CABINET_LINK))
        driver.find_element(*PERSONAL_CABINET_LINK).click()
        wait.until(EC.visibility_of_element_located(PROFILE_LINK))
        dismiss_overlay(driver)
        wait.until(EC.visibility_of_element_located(LOGO))
        # кликаем по <a>-родителю SVG-логотипа
        logo = driver.find_element(*LOGO)
        driver.execute_script("arguments[0].parentNode.click();", logo)
        # маркер успеха — заголовок конструктора
        assert wait.until(EC.visibility_of_element_located(CONSTRUCTOR_TITLE))

    def test_logout(self, driver, logged_in_user):
        """Выход из аккаунта по кнопке «Выход»."""
        wait = WebDriverWait(driver, 10)
        dismiss_overlay(driver)
        wait.until(EC.element_to_be_clickable(PERSONAL_CABINET_LINK))
        driver.find_element(*PERSONAL_CABINET_LINK).click()
        wait.until(EC.visibility_of_element_located(PROFILE_LINK))
        dismiss_overlay(driver)
        wait.until(EC.element_to_be_clickable(EXIT_BUTTON))
        driver.find_element(*EXIT_BUTTON).click()
        # маркер успеха выхода — форма входа (кнопка «Войти»)
        assert wait.until(EC.visibility_of_element_located(LOGIN_SUBMIT_BUTTON))