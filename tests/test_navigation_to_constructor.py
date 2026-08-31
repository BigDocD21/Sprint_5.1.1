import pytest
from helpers import safe_click, perform_login, wait_for_visible
from constants import BASE_URL, generate_unique_email, generate_unique_password
from locators import Locators

class TestNavigationFlow:
    def test_navigation_to_constructor_from_cabinet(self, driver):
        email = generate_unique_email()
        password = generate_unique_password()
        
        driver.get(BASE_URL)
        safe_click(driver, Locators.Nav.LINK_CABINET)
        perform_login(driver, email, password)
        
        wait_for_visible(driver, Locators.Login.CHECK_LOGGED_IN)
        
        safe_click(driver, Locators.Nav.LINK_CABINET)
        safe_click(driver, Locators.Nav.LINK_CONSTRUCTOR)
        wait_for_visible(driver, Locators.Tabs.HEADER_TITLE)
        
        assert driver.current_url.startswith(BASE_URL)

    def test_navigation_via_logo(self, driver):
        email = generate_unique_email()
        password = generate_unique_password()
        
        driver.get(BASE_URL)
        safe_click(driver, Locators.Nav.LINK_CABINET)
        perform_login(driver, email, password)
        
        wait_for_visible(driver, Locators.Login.CHECK_LOGGED_IN)
        
        safe_click(driver, Locators.Nav.LINK_CABINET)
        safe_click(driver, Locators.Nav.LOGO)
        wait_for_visible(driver, Locators.Tabs.HEADER_TITLE)
        
        assert driver.current_url.startswith(BASE_URL)
