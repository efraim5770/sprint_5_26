from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.locators import WebsiteLocators as L
from src.data import Urls, TestUser


class TestUserLogin:

    def test_login_via_account_button(self, driver):
        driver.get(Urls.main())
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(L.LOGIN_INTO_ACCOUNT_BUTTON)).click()
        wait.until(EC.url_to_be(Urls.login()))

        wait.until(EC.presence_of_element_located(L.EMAIL_INPUT_FORM)).send_keys(TestUser.login)
        wait.until(EC.presence_of_element_located(L.PASSWORD_INPUT_FORM)).send_keys(TestUser.password)
        wait.until(EC.element_to_be_clickable(L.LOGIN_BUTTON_FORM)).click()

        assert wait.until(EC.visibility_of_element_located(L.MAKE_ORDER_BUTTON)).is_displayed()

    def test_login_via_account_button_in_header(self, driver):
        driver.get(Urls.main())
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(L.ACCOUNT_BUTTON)).click()
        wait.until(EC.url_to_be(Urls.login()))

        wait.until(EC.presence_of_element_located(L.EMAIL_INPUT_FORM)).send_keys(TestUser.login)
        wait.until(EC.presence_of_element_located(L.PASSWORD_INPUT_FORM)).send_keys(TestUser.password)
        wait.until(EC.element_to_be_clickable(L.LOGIN_BUTTON_FORM)).click()

        assert wait.until(EC.visibility_of_element_located(L.MAKE_ORDER_BUTTON)).is_displayed()

    # 3. Ссылка «Войти» на форме регистрации
    def test_login_via_registration_form(self, driver):
        driver.get(Urls.register())
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(L.LOGIN_TEXT_LINK)).click()
        wait.until(EC.url_to_be(Urls.login()))

        wait.until(EC.presence_of_element_located(L.EMAIL_INPUT_FORM)).send_keys(TestUser.login)
        wait.until(EC.presence_of_element_located(L.PASSWORD_INPUT_FORM)).send_keys(TestUser.password)
        wait.until(EC.element_to_be_clickable(L.LOGIN_BUTTON_FORM)).click()

        assert wait.until(EC.visibility_of_element_located(L.MAKE_ORDER_BUTTON)).is_displayed()

    # 4. Ссылка «Войти» на форме «Забыли пароль»
    def test_login_via_forgot_password_form(self, driver):
        driver.get(Urls.forgot_password())
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(L.LOGIN_TEXT_LINK)).click()
        wait.until(EC.url_to_be(Urls.login()))

        wait.until(EC.presence_of_element_located(L.EMAIL_INPUT_FORM)).send_keys(TestUser.login)
        wait.until(EC.presence_of_element_located(L.PASSWORD_INPUT_FORM)).send_keys(TestUser.password)
        wait.until(EC.element_to_be_clickable(L.LOGIN_BUTTON_FORM)).click()

        assert wait.until(EC.visibility_of_element_located(L.MAKE_ORDER_BUTTON)).is_displayed()
