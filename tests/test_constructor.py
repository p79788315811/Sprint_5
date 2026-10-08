import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from helpers import open_constructor


class TestConstructor:
    def test_bun_tab(self, driver):
        """Клик по вкладке «Булки» активирует раздел «Булки»."""
        open_constructor(driver)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(BUN_TAB))
        driver.execute_script("arguments[0].click();", driver.find_element(*BUN_TAB))
        assert wait.until(EC.visibility_of_element_located(ACTIVE_BUN_TAB))

    def test_sauce_tab(self, driver):
        """Клик по вкладке «Соусы» активирует раздел «Соусы»."""
        open_constructor(driver)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(SAUCE_TAB))
        driver.execute_script("arguments[0].click();", driver.find_element(*SAUCE_TAB))
        assert wait.until(EC.visibility_of_element_located(ACTIVE_SAUCE_TAB))

    def test_filling_tab(self, driver):
        """Клик по вкладке «Начинки» активирует раздел «Начинки»."""
        open_constructor(driver)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(FILLING_TAB))
        driver.execute_script("arguments[0].click();", driver.find_element(*FILLING_TAB))
        assert wait.until(EC.visibility_of_element_located(ACTIVE_FILLING_TAB))