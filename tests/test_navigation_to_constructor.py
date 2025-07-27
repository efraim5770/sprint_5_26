from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators import WebsiteLocators
import src.data as data

class TestConstructorNavigation:

    def test_navigation_from_account_to_constructor_via_constructor_button(self, driver):
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
        wait.until(EC.url_to_be(data.login_page_url))
        account_button = wait.until(EC.element_to_be_clickable(WebsiteLocators.ACCOUNT_BUTTON))
        account_button.click()
        wait.until(EC.url_to_be(data.profile_page_url))

        # Кликаем кнопку "Конструктор"
        constructor_button = wait.until(EC.element_to_be_clickable(WebsiteLocators.CONSTRUCTOR_BUTTON))
        constructor_button.click()

        # Ожидаем переход на страницу конструктора
        wait.until(EC.url_to_be(data.main_page_url))
        constructor_header = wait.until(EC.presence_of_element_located(WebsiteLocators.CONSTRUCTOR_HEADER))
        assert constructor_header.is_displayed()

    def test_navigation_from_account_to_constructor_via_logo(self, driver):
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

        # Кликаем на логотип Stellar Burgers
        logo_button = wait.until(EC.element_to_be_clickable(WebsiteLocators.SERVICE_LOGO_BUTTON))
        logo_button.click()

        # Ожидаем переход на страницу конструктора
        wait.until(EC.url_to_be(data.main_page_url))
        constructor_header = wait.until(EC.presence_of_element_located(WebsiteLocators.CONSTRUCTOR_HEADER))
        assert constructor_header.is_displayed()