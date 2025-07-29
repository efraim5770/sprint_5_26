from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.locators import WebsiteLocators as L
from src.data import Urls, TestUser


class TestAccountNavigation:

    def test_navigate_to_account_page(self, driver):
        driver.get(Urls.login())
        wait = WebDriverWait(driver, 10)

        # вводим e‑mail и пароль
        wait.until(EC.presence_of_element_located(L.EMAIL_INPUT_FORM))\
            .send_keys(TestUser.login)
        wait.until(EC.presence_of_element_located(L.PASSWORD_INPUT_FORM))\
            .send_keys(TestUser.password)

        wait.until(EC.element_to_be_clickable(L.LOGIN_BUTTON_FORM)).click()

        # ожидаем редирект на главную
        wait.until(EC.url_to_be(Urls.main()))

        # «Личный кабинет»
        wait.until(EC.element_to_be_clickable(L.ACCOUNT_BUTTON)).click()

        # страница профиля
        wait.until(EC.url_to_be(Urls.profile()))

        # кнопка «Выход» присутствует
        assert wait.until(
            EC.visibility_of_element_located(L.LOGOUT_BUTTON)
        ).is_displayed()
