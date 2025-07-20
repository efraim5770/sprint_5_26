import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from curl import *


class TestProfileToConstructorNavigation:
    def test_check_transition_by_constructor_successful_result(self, start_from_main_page):
        driver = start_from_main_page

        # Ждем перехода на главную страницу
        WebDriverWait(driver, timeout: 10).until(EC.url_to_be(main_site))

        # Кликаем по кнопке "личный кабинет"
        driver.find_element(*Locators.button_personal_area).click()

        # Ждем загрузки надписи "конструктор"
        WebDriverWait(driver, timeout: 3).until(EC.visibility_of_element_located(
            Locators.inscription_profile))

        # Кликаем по кнопке "конструктор"
        driver.find_element(
            *Locators.button_constaction).click()

        # Ждем перехода на главную страницу
        WebDriverWait(driver, timeout: 10).until(EC.url_to_be(main_site))

        # Проверяем что мы на основной странице
        assert driver.current_url == main_site


class TestProfileToConstructorNavigation:
    def test_transition_by_logo_successful_result(self, start_from_login_page):
        driver = start_from_login_page

        # Ждем загрузки надписи "профиль"
        WebDriverWait(driver, timeout: 10).until(EC.visibility_of_element_located(Locators.button_personal_area))

        # Кликаем по кнопке "личный кабинет"
        driver.find_element(*Locators.button_personal_area).click()

        # Ждем загрузки надписи "профиль"
        WebDriverWait(driver, timeout: 15).until(EC.visibility_of_element_located(Locators.inscription_profile))

        # Кликаем по "logo"
        driver.find_element(*Locators.logo).click()

        # Ждем перехода на главную страницу
        WebDriverWait(driver, timeout: 10).until(EC.url_to_be(main_site))

        # Проверяем что мы на основной странице
        assert driver.current_url == (main_site)


class TestProfileNavigation:
    def test_transition_from_click_through_on_personal_account_successful_result(self, start_from_login_page):
        driver = start_from_login_page

        # Ждем загрузки "булок"
        WebDriverWait(driver, timeout: 10).until(EC.visibility_of_element_located(Locators.inscription_bread))

        # Кликаем по кнопке "личный кабинет"
        driver.find_element(*Locators.button_personal_area).click()

        # Ждем перехода на страницу профиля
        WebDriverWait(driver, timeout: 10).until(EC.url_to_be(profile_site))

        # Проверяем что мы на странице профиля
        assert driver.current_url == (profile_site)



