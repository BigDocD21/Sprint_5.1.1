import pytest
from helpers import safe_click, perform_login, perform_registration, wait_for_visible
from constants import BASE_URL, generate_unique_email, generate_unique_password
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait

class TestNavigationFlow:
    def test_navigation_to_constructor_from_cabinet(self, driver):
        email = generate_unique_email()
        password = generate_unique_password()
        name = "Дима"

        driver.get(f"{BASE_URL}/register")
        perform_registration(driver, name, email, password)
        
        wait = WebDriverWait(driver, 15)
        wait.until(lambda d: d.current_url.endswith("/login"))
        
        perform_login(driver, email, password)

        safe_click(driver, Locators.Nav.LINK_CABINET)
        wait_for_visible(driver, Locators.Login.CHECK_LOGGED_IN)
        
        safe_click(driver, Locators.Nav.LINK_CONSTRUCTOR)
        
        wait_for_visible(driver, Locators.Tabs.HEADER_TITLE)
        
        current_url = driver.current_url
        expected_url = f"{BASE_URL}/"
        assert current_url == expected_url, f"Ожидался URL {expected_url}, но получен: {current_url}"

    def test_navigation_via_logo(self, driver):
        safe_click(driver, Locators.Nav.LINK_CABINET)

        profile_element = wait_for_visible(driver, Locators.Login.CHECK_LOGGED_IN)
        assert profile_element.is_displayed(), "Пользователь не авторизован. Сессия потеряна."

        safe_click(driver, Locators.Nav.LOGO)

        wait_for_visible(driver, Locators.Tabs.HEADER_TITLE)
        
        current_url = driver.current_url
        expected_url = f"{BASE_URL}/"
        assert current_url == expected_url, f"Ожидался URL {expected_url}, но получен: {current_url}"
        