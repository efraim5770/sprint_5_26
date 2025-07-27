import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators import WebsiteLocators
import src.data as data

class TestUserLogout:

    def test_logout_from_account(self, driver):
        driver.get(data.login_page_url)
        wait = WebDriverWait(driver, 10)

        # Входим в личный кабинет пользователя
        email_input = wait.until(EC.presence_of_element_located(WebsiteLocators.EMAIL_INPUT_FORM))
        email_input.send_keys(data.test_user_login)
        password_input = wait.until(EC.presence_of_element_located(WebsiteLocators.PASSWORD_INPUT_FORM))
        password_input.send_keys(data.test_user_password)
        login_button = wait.until(EC.element_to_be_clickable(WebsiteLocators.LOGIN_BUTTON_FORM))
        login_button.click()

        # Переходим на страницу личного кабинета
        wait.until(EC.url_to_be(data.main_page_url))
        account_button = wait.until(EC.element_to_be_clickable(WebsiteLocators.ACCOUNT_BUTTON))
        account_button.click()
        wait.until(EC.url_to_be(data.profile_page_url))

        # Нажимаем кнопку "Выйти"
        logout_button = wait.until(EC.element_to_be_clickable(WebsiteLocators.LOGOUT_BUTTON))
        logout_button.click()

        # Ожидаем перехода на страницу входа в аккаунт
        wait.until(EC.url_to_be(data.login_page_url))

        # Ожидаем, что форма логина отображается
        login_form = wait.until(EC.presence_of_element_located(WebsiteLocators.EMAIL_INPUT_FORM))
        assert login_form.is_displayed()
