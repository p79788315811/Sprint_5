# -*- coding: utf-8 -*-
# Модуль вспомогательных функций (хелперы)

import random
import string


def generate_unique_email():
    """Генерирует уникальный email в формате имя_фамилия_когорта_цифры@домен."""
    name = ''.join(random.choices(string.ascii_lowercase, k=5))
    surname = ''.join(random.choices(string.ascii_lowercase, k=7))
    cohort = random.randint(1000, 9999)
    digits = random.randint(100, 999)
    domain = random.choice(['yandex.ru', 'mail.ru', 'gmail.com'])
    return f"{name}_{surname}_{cohort}_{digits}@{domain}"


def generate_password(length=8):
    """Генерирует пароль заданной длины (по умолчанию 8 символов)."""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))


def generate_name():
    """Генерирует случайное имя."""
    return ''.join(random.choices(string.ascii_lowercase, k=6)).capitalize()


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


def open_constructor(driver):
    """Открывает главную страницу и убирает модальное окно, мешающее кликам."""
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from locators import CONSTRUCTOR_TITLE
    from constants import MAIN_PAGE_URL

    driver.get(MAIN_PAGE_URL)
    dismiss_overlay(driver)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(CONSTRUCTOR_TITLE))


def fill_and_submit_login(driver, user):
    """Заполняет форму входа и отправляет её."""
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from locators import EMAIL_INPUT, PASSWORD_INPUT, LOGIN_SUBMIT_BUTTON

    wait = WebDriverWait(driver, 10)
    dismiss_overlay(driver)
    wait.until(EC.visibility_of_element_located(EMAIL_INPUT))
    driver.find_element(*EMAIL_INPUT).send_keys(user['email'])
    driver.find_element(*PASSWORD_INPUT).send_keys(user['password'])
    dismiss_overlay(driver)  # модалка может появиться позже — прячем перед кликом
    wait.until(EC.element_to_be_clickable(LOGIN_SUBMIT_BUTTON))
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()