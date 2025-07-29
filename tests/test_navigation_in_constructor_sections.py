from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.locators import WebsiteLocators as L        # сокращение не обязательно
from src.data import Urls


class TestSectionsNavigation:

    def test_navigation_to_sections_sauces(self, driver):
        driver.get(Urls.main())
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(L.SAUCES_SECTION_INACTIVE)).click()
        sauces_active = wait.until(EC.visibility_of_element_located(L.SAUCES_SECTION_ACTIVE))

        assert "current" in sauces_active.get_attribute("class")

    def test_navigation_to_sections_buns(self, driver):
        driver.get(Urls.main())
        wait = WebDriverWait(driver, 10)

        # сначала делаем вкладку «Булки» неактивной
        wait.until(EC.element_to_be_clickable(L.SAUCES_SECTION_INACTIVE)).click()
        wait.until(EC.visibility_of_element_located(L.SAUCES_SECTION_ACTIVE))

        wait.until(EC.element_to_be_clickable(L.BUNS_SECTION_INACTIVE)).click()
        buns_active = wait.until(EC.visibility_of_element_located(L.BUNS_SECTION_ACTIVE))

        assert "current" in buns_active.get_attribute("class")

    def test_navigation_to_sections_stuffings(self, driver):
        driver.get(Urls.main())
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(L.STUFFINGS_SECTION_INACTIVE)).click()
        stuffings_active = wait.until(EC.visibility_of_element_located(L.STUFFINGS_SECTION_ACTIVE))

        assert "current" in stuffings_active.get_attribute("class")
