import pytest
from helpers import safe_click, wait_for_visible
from constants import BASE_URL
from locators import Locators

class TestNavigationFlow:
    def test_navigation_to_constructor_from_cabinet(self, authorized_user):
        driver = authorized_user
        
        safe_click(driver, Locators.Nav.LINK_CABINET)
        safe_click(driver, Locators.Nav.LINK_CONSTRUCTOR)
        
        wait_for_visible(driver, Locators.Tabs.HEADER_TITLE)
        
        assert driver.current_url.startswith(BASE_URL)

    def test_navigation_via_logo(self, authorized_user):
        driver = authorized_user
        
        safe_click(driver, Locators.Nav.LINK_CABINET)
        safe_click(driver, Locators.Nav.LOGO)
        
        wait_for_visible(driver, Locators.Tabs.HEADER_TITLE)
        
        assert driver.current_url.startswith(BASE_URL)
        