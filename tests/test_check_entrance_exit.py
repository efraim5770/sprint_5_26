import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import Locators
from curl import *
from data import Credantial


class TestLogOutOfYourAccount:
    def test_logout_from_batton_exit_in_personal_account_exit(self, start_from_login_page):
        driver = start_from_login_page

        # Ждем загрузки "булок"
        WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located(Locators.inscription_bread))

        # Кликаем по кнопке "личный кабинет"
        driver.find_element(*Locators.button_personal_area).click()

        # Жем загрузки надписи "профиль"
        WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located(Locators.inscription_profile))

        # Кликаем по кнопке "выход"
        driver.find_element(*Locators.button_exit).click()

        # Ждем перехода на страницу логина
        WebDriverWait(driver, timeout=10).until(EC.url_to_be(login_site))

        # Проверяем URL адрес страницы логина
        assert driver.current_url == login_site


class TestEntranceOfBigMainButton:
    def test_entrance_from_button_sign_in_main_page_login_completed(self, start_from_site_not_login):
        driver = start_from_site_not_login

        # Жмем кнопку "Войти в аккаунт"
        driver.find_element(*Locators.entrance_on_the_main).click()

        # Ищем поля и проходим авторизацию
        driver.find_element(*Locators.field_email).send_keys(Credantial.email)
        driver.find_element(*Locators.field_password).send_keys(Credantial.password)
        driver.find_element(*Locators.button_entrance).click()

        # Ждем перехода на главную страницу
        WebDriverWait(driver, timeout=10).until(EC.url_to_be(main_site))

        # Проверяем что мы на основной странице сайта
        assert driver.current_url == main_site


class TestEntranceOfPasswordRecoveryButton:
    def test_entrance_from_batton_password_recovery_form_login_completed(self, start_from_recovery_page):
        driver = start_from_recovery_page

        # Жмем загрузки "булок"
        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((Locators.inscription_bread)))

        # Проверяем что мы на основной странице сайта
        assert driver.current_url == main_site


class TestEntranceOfBattonRegistrationForm:
    def test_entrance_from_batton_registration_form_login_completed(self, start_from_main_not_login):
        driver = start_from_main_not_login

        # Жмем кнопку "зарегаться"
        driver.find_element(*Locators.inscription_login).click()

        # Жмем кнопку "войти"
        driver.find_element(*Locators.inscription_button_entrance).click()

        # Ищем поля и проходим авторизацию
        driver.find_element(*Locators.field_email).send_keys(Credantial.email)
        driver.find_element(*Locators.field_password).send_keys(Credantial.password)
        driver.find_element(*Locators.button_entrance).click()

        # Ждем перехода на главную страницу
        WebDriverWait(driver, timeout=10).until(EC.url_to_be(main_site))

        # Проверяем что мы на основной странице сайта
        assert driver.current_url == main_site






