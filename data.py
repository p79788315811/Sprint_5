# -*- coding: utf-8 -*-
# Константы приложения: URL-адреса (вынесены из locators, т.к. это не локаторы)

MAIN_PAGE_URL = "https://stellarburgers.education-services.ru"  # Основной URL приложения

# URL-адреса страниц (для проверок навигации)
LOGIN_PAGE_URL = MAIN_PAGE_URL + "/login"  # Страница входа
REGISTER_PAGE_URL = MAIN_PAGE_URL + "/register"  # Страница регистрации
RECOVERY_PAGE_URL = MAIN_PAGE_URL + "/forgot-password"  # Страница восстановления пароля
PROFILE_PAGE_URL = MAIN_PAGE_URL + "/account/profile"  # Личный кабинет


def dismiss_overlay(driver):
    """Скрывает модальный оверлей через JS, если он есть (иначе перехватывает клики)."""
    try:
        driver.execute_script(
            "var els=document.querySelectorAll('[class*=Modal_modal_overlay]');"
            "for(var e of els){e.style.display='none';}"
            "var conts=document.querySelectorAll('[class*=Modal_modal]');"
            "for(var c of conts){c.style.display='none';}"
        )
    except Exception:
        pass