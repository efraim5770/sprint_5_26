from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.locators import WebsiteLocators as L
import src.data as data


class TestUserLogin:

    # 1. Главная → «Войти в аккаунт»
    def test_login_via_account_button(self, driver):
        driver.get(data.main_page_url)
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(L.LOGIN_INTO_ACCOUNT_BUTTON)).click()
        wait.until(EC.url_to_be(data.login_page_url))

        wait.until(EC.presence_of_element_located(L.EMAIL_INPUT_FORM)).send_keys(data.test_user_login)
        wait.until(EC.presence_of_element_located(L.PASSWORD_INPUT_FORM)).send_keys(data.test_user_password)
        wait.until(EC.element_to_be_clickable(L.LOGIN_BUTTON_FORM)).click()

        assert wait.until(EC.visibility_of_element_located(L.MAKE_ORDER_BUTTON)).is_displayed()

    # 2. Кнопка «Личный кабинет» в хедере
    def test_login_via_account_button_in_header(self, driver):
        driver.get(data.main_page_url)
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(L.ACCOUNT_BUTTON)).click()
        wait.until(EC.url_to_be(data.login_page_url))

        wait.until(EC.presence_of_element_located(L.EMAIL_INPUT_FORM)).send_keys(data.test_user_login)
        wait.until(EC.presence_of_element_located(L.PASSWORD_INPUT_FORM)).send_keys(data.test_user_password)
        wait.until(EC.element_to_be_clickable(L.LOGIN_BUTTON_FORM)).click()

        assert wait.until(EC.visibility_of_element_located(L.MAKE_ORDER_BUTTON)).is_displayed()

    # 3. Ссылка «Войти» на форме регистрации
    def test_login_via_registration_form(self, driver):
        driver.get(data.register_page_url)
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(L.LOGIN_TEXT_LINK)).click()
        wait.until(EC.url_to_be(data.login_page_url))

        wait.until(EC.presence_of_element_located(L.EMAIL_INPUT_FORM)).send_keys(data.test_user_login)
        wait.until(EC.presence_of_element_located(L.PASSWORD_INPUT_FORM)).send_keys(data.test_user_password)
        wait.until(EC.element_to_be_clickable(L.LOGIN_BUTTON_FORM)).click()

        assert wait.until(EC.visibility_of_element_located(L.MAKE_ORDER_BUTTON)).is_displayed()

    # 4. Ссылка «Войти» на форме «Забыли пароль»
    def test_login_via_forgot_password_form(self, driver):
        driver.get(data.forgot_password_page_url)
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(L.LOGIN_TEXT_LINK)).click()
        wait.until(EC.url_to_be(data.login_page_url))

        wait.until(EC.presence_of_element_located(L.EMAIL_INPUT_FORM)).send_keys(data.test_user_login)
        wait.until(EC.presence_of_element_located(L.PASSWORD_INPUT_FORM)).send_keys(data.test_user_password)
        wait.until(EC.element_to_be_clickable(L.LOGIN_BUTTON_FORM)).click()

        assert wait.until(EC.visibility_of_element_located(L.MAKE_ORDER_BUTTON)).is_displayed()
