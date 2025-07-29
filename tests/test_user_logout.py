from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.locators import WebsiteLocators as L
from src.data import Urls, TestUser


class TestUserLogout:

    def test_logout_from_account(self, driver):
        driver.get(Urls.login())                   # страница входа
        wait = WebDriverWait(driver, 10)

        # логинимся
        wait.until(EC.presence_of_element_located(L.EMAIL_INPUT_FORM)).send_keys(TestUser.login)
        wait.until(EC.presence_of_element_located(L.PASSWORD_INPUT_FORM)).send_keys(TestUser.password)
        wait.until(EC.element_to_be_clickable(L.LOGIN_BUTTON_FORM)).click()

        # подтверждаем редирект на главную
        wait.until(EC.url_to_be(Urls.main()))

        # «Личный кабинет» → профиль
        wait.until(EC.element_to_be_clickable(L.ACCOUNT_BUTTON)).click()
        wait.until(EC.url_to_be(Urls.profile()))

        # «Выйти»
        wait.until(EC.element_to_be_clickable(L.LOGOUT_BUTTON)).click()

        # снова форма логина
        wait.until(EC.url_to_be(Urls.login()))
        assert wait.until(EC.visibility_of_element_located(L.EMAIL_INPUT_FORM)).is_displayed()
