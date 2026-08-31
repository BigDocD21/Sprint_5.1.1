import pytest
from helpers import safe_click, perform_login, wait_for_visible
from constants import BASE_URL
from locators import Locators

USER_EMAIL = "qwerty@yandex.ru"
USER_PASSWORD = "123456"

class TestNavigationFlow:
    def test_navigation_to_constructor_from_cabinet(self, driver):
        driver.get(f"{BASE_URL}/login")
        perform_login(driver, USER_EMAIL, USER_PASSWORD)

        safe_click(driver, Locators.Nav.LINK_CABINET)
        wait_for_visible(driver, Locators.Login.CHECK_LOGGED_IN)
        
        safe_click(driver, Locators.Nav.LINK_CONSTRUCTOR)
        wait_for_visible(driver, Locators.Tabs.HEADER_TITLE)
        
        current_url = driver.current_url
        expected_url = f"{BASE_URL}/"
        assert current_url == expected_url, f"Ожидался URL {expected_url}, но получен: {current_url}"

    def test_navigation_via_logo(self, driver):
        driver.get(f"{BASE_URL}/login")
        perform_login(driver, USER_EMAIL, USER_PASSWORD)

        safe_click(driver, Locators.Nav.LINK_CABINET)
        wait_for_visible(driver, Locators.Login.CHECK_LOGGED_IN)
        
        safe_click(driver, Locators.Nav.LOGO)
        wait_for_visible(driver, Locators.Tabs.HEADER_TITLE)
        
        current_url = driver.current_url
        expected_url = f"{BASE_URL}/"
        assert current_url == expected_url, f"Ожидался URL {expected_url}, но получен: {current_url}"
