import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

class TestConstructor:
    def test_bun_tab(self, driver):
        driver.get(MAIN_PAGE_URL)  # Используем обновлённый URL ← URL ИЗМЕНЁН**
        driver.find_element(By.XPATH, BUN_TAB).click()

        wait = WebDriverWait(driver, 10)
        active_tab = driver.find_element(By.XPATH, BUN_TAB)
        assert "tab_tab_active" in active_tab.get_attribute("class")

    def test_sauce_tab(self, driver):
        driver.get(MAIN_PAGE_URL)  # Используем обновлённый URL ← URL ИЗМЕНЁН**
        driver.find_element(By.XPATH, SAUCE_TAB).click()

        wait = WebDriverWait(driver, 10)
        active_tab = driver.find_element(By.XPATH, SAUCE_TAB)
        assert "tab_tab_active" in active_tab.get_attribute("class")

    def test_filling_tab(self, driver):
        driver.get(MAIN_PAGE_URL)  # Используем обновлённый URL ← URL ИЗМЕНЁН**
        driver.find_element(By.XPATH, FILLING_TAB).click()

        wait = WebDriverWait(driver, 10)
        active_tab = driver.find_element(By.XPATH, FILLING_TAB)
        assert "tab_tab_active" in active_tab.get_attribute("class")
