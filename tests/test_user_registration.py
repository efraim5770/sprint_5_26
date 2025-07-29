from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.locators import WebsiteLocators as L
from src.helpers import (
    generate_name, generate_login, generate_valid_password, generate_invalid_password
)
from src.data import Urls


class TestUserRegistration:

    def test_successful_registration(self, driver):
        driver.get(Urls.register())
        wait = WebDriverWait(driver, 10)

        wait.until(EC.presence_of_element_located(L.NAME_INPUT_FORM)).send_keys(generate_name())
        wait.until(EC.presence_of_element_located(L.EMAIL_INPUT_FORM)).send_keys(generate_login())
        wait.until(EC.presence_of_element_located(L.PASSWORD_INPUT_FORM)).send_keys(generate_valid_password())

        wait.until(EC.element_to_be_clickable(L.REGISTRATION_BUTTON_FORM)).click()

        wait.until(EC.url_to_be(Urls.login()))               # валидация редиректа
        assert wait.until(EC.visibility_of_element_located(L.LOGIN_BUTTON_FORM)).is_displayed()

    def test_registration_with_invalid_password(self, driver):
        driver.get(Urls.register())
        wait = WebDriverWait(driver, 10)

        wait.until(EC.presence_of_element_located(L.NAME_INPUT_FORM)).send_keys(generate_name())
        wait.until(EC.presence_of_element_located(L.EMAIL_INPUT_FORM)).send_keys(generate_login())
        wait.until(EC.presence_of_element_located(L.PASSWORD_INPUT_FORM)).send_keys(generate_invalid_password())

        wait.until(EC.element_to_be_clickable(L.REGISTRATION_BUTTON_FORM)).click()

        assert wait.until(EC.visibility_of_element_located(L.PASSWORD_ERROR_MESSAGE)).is_displayed()
