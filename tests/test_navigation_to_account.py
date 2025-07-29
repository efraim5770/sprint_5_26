from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.locators import WebsiteLocators as L
from src.data import Urls, TestUser

class TestConstructorNavigation:

    def test_navigation_from_account_to_constructor_via_constructor_button(self, driver):
        driver.get(Urls.login())
        wait = WebDriverWait(driver, 10)

        wait.until(EC.presence_of_element_located(L.EMAIL_INPUT_FORM)).send_keys(TestUser.login)
        wait.until(EC.presence_of_element_located(L.PASSWORD_INPUT_FORM)).send_keys(TestUser.password)
        wait.until(EC.element_to_be_clickable(L.LOGIN_BUTTON_FORM)).click()

        wait.until(EC.url_to_be(Urls.main()))

        wait.until(EC.element_to_be_clickable(L.ACCOUNT_BUTTON)).click()
        wait.until(EC.url_to_be(Urls.profile()))

        wait.until(EC.element_to_be_clickable(L.CONSTRUCTOR_BUTTON)).click()

        wait.until(EC.url_to_be(Urls.main()))
        assert wait.until(EC.visibility_of_element_located(L.CONSTRUCTOR_HEADER)).is_displayed()

   def test_navigation_from_account_to_constructor_via_logo(self, driver):
        driver.get(Urls.login())
        wait = WebDriverWait(driver, 10)

        wait.until(EC.presence_of_element_located(L.EMAIL_INPUT_FORM)).send_keys(TestUser.login)
        wait.until(EC.presence_of_element_located(L.PASSWORD_INPUT_FORM)).send_keys(TestUser.password)
        wait.until(EC.element_to_be_clickable(L.LOGIN_BUTTON_FORM)).click()

        wait.until(EC.url_to_be(Urls.main()))

        wait.until(EC.element_to_be_clickable(L.ACCOUNT_BUTTON)).click()
        wait.until(EC.url_to_be(Urls.profile()))

        wait.until(EC.element_to_be_clickable(L.SERVICE_LOGO_BUTTON)).click()

        wait.until(EC.url_to_be(Urls.main()))
        assert wait.until(EC.visibility_of_element_located(L.CONSTRUCTOR_HEADER)).is_displayed()
