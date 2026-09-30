import pytest
from locators import *

class TestProfileNavigation:
    def test_transition_to_personal_cabinet(self, driver, logged_in_user):
        """Тест перехода в личный кабинет"""
        # Нажимаем кнопку «Личный кабинет»
        driver.find_element(*PERSONAL_CABINET_LINK).click()

        # Проверяем отображение профиля
        profile_edit = driver.find_element(*PROFILE_EDIT_LINK)
        assert profile_edit.is_displayed(), "Не удалось попасть в личный кабинет!"

    def test_transition_from_profile_to_constructor(self, driver, logged_in_user):
        """Тест перехода из личного кабинета в конструктор через кнопку"""
        # Переходим в личный кабинет
        driver.find_element(*PERSONAL_CABINET_LINK).click()

        # Нажимаем кнопку «Конструктор»
        constructor_btn = driver.find_element(*CONSTRUCTOR_BUTTON)
        constructor_btn.click()

        # Проверяем загрузку конструктора
        buns_tab = driver.find_element(*BUN_TAB)
        assert buns_tab.is_displayed(), "Конструктор не загрузился!"

    def test_transition_via_logo(self, driver, logged_in_user):
        """Тест перехода через логотип Stellar Burgers"""
        # Переходим в личный кабинет
        driver.find_element(*PERSONAL_CABINET_LINK).click()

        # Кликаем на логотип
        logo = driver.find_element(*LOGO)
        logo.click()

        # Проверяем возврат в конструктор
        buns_section = driver.find_element(*BUNS_SECTION)
        assert buns_section.is_displayed(), "Переход через логотип не сработал!"

    def test_logout(self, driver, logged_in_user):
        """Тест выхода из аккаунта"""
        # Переходим в личный кабинет
        driver.find_element(*PERSONAL_CABINET_LINK).click()

        # Нажимаем кнопку «Выйти»
        logout_btn = driver.find_element(*EXIT_BUTTON)
        logout_btn.click()

        # Проверяем возврат на главную страницу
        login_btn = driver.find_element(*LOGIN_BUTTON_MAIN)
        assert login_btn.is_displayed(), "Не удалось выйти из аккаунта!"