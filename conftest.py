import pytest
from selenium import webdriver
from curl import *
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from geniration_ep import EmailPasswordGenerator
from data import Credantial


@pytest.fixture
def driver():  # основная фикстура
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver  # возвращаем драйвер без return
    driver.quit()  # закрываем драйвер


@pytest.fixture
def start_from_login_page(driver):
    login_page = login_site
    driver.get(login_page)

    # Ищем поля и проходим авторизацию
    driver.find_element(*Locators.field_email).send_keys(Credantial.email)
    driver.find_element(*Locators.field_password).send_keys(Credantial.password)
    driver.find_element(*Locators.button_entrance).click()

    return driver


@pytest.fixture
def start_from_recovery_page(driver):
    login_page = login_site
    driver.get(login_page)

    # Кликаем по кнопке "восстановить пароль"
    driver.find_element(*Locators.button_restore_password).click

    # Ждем загрузку кнопки "войти"
    WebDriverWait(driver, timeout=6).until(EC.visibility_of_element_located(Locators.inscription_button_entrance))

    # Кликаем по маленькой кнопке "Войти"
    driver.find_element(*Locators.inscription_button_entrance).click()

    # Ищем поля и проходим авторизацию
    driver.find_element(*Locators.field_email).send_keys(Credantial.email)
    driver.find_element(*Locators.field_password).send_keys(Credantial.password)
    driver.find_element(*Locators.button_entrance).click()

    return driver


@pytest.fixture
def start_from_login_page(driver):
    main_page = main_site
    driver.get(main_page)

    # Кликаем по кнопке "личный кабинет"
    driver, find_element(*Locators.button_personal_area).click()

    # Кликаем по маленькой кнопке "войти"
    driver.find_element(*Locators.button_entrance).click()

    # Ищем поля и проходим авторизацию
    driver.find_element(*Locators.field_email).send_keys(Credantial.email)
    driver.find_element(*Locators.field_password).send_keys(Credantial.password)
    driver.find_element(*Locators.button_entrance).click()

    return driver


@pytest.fixture
def start_from_register_page(driver):
    register_page = register_site
    driver.get(register_page)

    # Находим надпись "войти" и жмем
    driver.find_element(*Locators.inscription_button_entrance).click()

    # Ищем поля и проходим авторизацию
    driver.find_element(*Locators.field_email).send_keys(Credantial.email)
    driver.find_element(*Locators.field_password).send_keys(Credantial.password)
    driver.find_element(*Locators.button_entrance).click()

    return driver


@pytest.fixture
def start_from_main_not_login(driver):
    login_page = login_site
    driver.get(login_page)

    return driver


@pytest.fixture
def start_from_site_not_login(driver):
    login_page = main_site
    driver.get(login_page)

    return driver


@pytest.fixture
def resister_new_account(driver):
    login_page = login_site
    driver.get(login_page)

    # Кликаем по надписи "Зарегистрироваться"
    driver.find_element(*Locators.inscription_login).click()

    # Генерация email и password
    generator = EmailPasswordGenerator()
    email, password = generator.generate()

    # Ищем поле "Имя" и заполни его
    driver.find_element(*Locators.field_name).send_keys(Credantial.name)

    # Ищем поле "email" и заполни его
    driver.find_element(*Locators.field_email).send_keys(email)

    # Ищем поле "Пароль" и заполнить его
    driver.find_element(*Locators.field_password).send_keys(password)

    # Жмем н кнопку зарегаться
    driver.find_element(*Locators.button_login).click()

    # Ждем кнопку войти
    WebDriverWait(driver, timeout=4).until(EC.visibility_of_element_located(Locators.button_entrance))

    return driver, email, password


