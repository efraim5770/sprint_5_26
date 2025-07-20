import pytest
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestCheckChapterBread:
    def test_check_chapter_bread_successful_result(self, start_from_login_page):
        driver = start_from_login_page

        # Нажали на раздел начинки "Соусы"
        WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located(Locators.inscription_sause)).click()

        # Нажали на раздел "Булки"
        WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located(Locators.inscription_bread)).click()

        # Проверяем наличие активного раздела
        new_element = WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located(Locators.active_section))
        assert new_element.is_displayed()

        # Проверяем, что активная вкладка соответствует разделу "Булки"
        active_tab = WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located(Locators.active_section))
        assert "Булки" in active_tab.text


class TestCheckChapterFillings:
    def test_check_chapter_fillings_successful_result(self, start_from_login_page):
        driver = start_from_login_page

        # Нажали на раздел "Начинки"
        WebDriverWait(driver, timeout=10).until(
            EC.visibility_of_element_located(Locators.inscription_fillings)).click()

        # Проверяем наличие активного раздела
        new_element = WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located(Locators.active_section))
        assert new_element.is_displayed()

        # Проверяем, что активная вкладка соответствует разделу "Начинки"
        active_tab = WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located(Locators.active_section))
        assert "Начинки" in active_tab.text


class TestCheckChapterSauce:
    def test_check_chapter_sauce_successful_result(self, start_from_login_page):
        driver = start_from_login_page

        # Нажали на раздел "Соусы"
        WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located(Locators.inscription_sause)).click()

        # Проверяем наличие активного раздела
        WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located(Locators.active_section)).is_displayed()

        # Проверяем, что активная вкладка соответствует разделу "Соусы"
        active_tab = WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located(Locators.active_section))
        assert "Соусы" in active_tab.text


