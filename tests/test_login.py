import pytest
from helpers import safe_click, perform_login, wait_for_visible
from constants import BASE_URL, generate_unique_email, generate_unique_password
from locators import Locators

class TestLoginFlows:
    def test_login_from_main_page(self, driver):

        email = generate_unique_email()
        password = generate_unique_password()
        
        driver.get(BASE_URL)
        
        safe_click(driver, Locators.Nav.LINK_CABINET)
        perform_login(driver, email, password)
        

        profile_element = wait_for_visible(driver, Locators.Login.CHECK_LOGGED_IN)
        assert profile_element.is_displayed(), f"Не удалось залогиниться с email: {email}"

    def test_login_from_cabinet_link(self, driver):

        email = generate_unique_email()
        password = generate_unique_password()
        
        driver.get(BASE_URL)
        safe_click(driver, Locators.Nav.LINK_CABINET)
        perform_login(driver, email, password)
        
        profile_element = wait_for_visible(driver, Locators.Login.CHECK_LOGGED_IN)
        assert profile_element.is_displayed(), f"Не удалось залогиниться с email: {email}"

    def test_login_from_registration_form(self, driver):

        email = generate_unique_email()
        password = generate_unique_password()
        
        driver.get(BASE_URL)
        safe_click(driver, Locators.Nav.LINK_CABINET)
        perform_login(driver, email, password)
        
        profile_element = wait_for_visible(driver, Locators.Login.CHECK_LOGGED_IN)
        assert profile_element.is_displayed(), f"Не удалось залогиниться с email: {email}"

    def test_login_from_restore_password_form(self, driver):

        email = generate_unique_email()
        password = generate_unique_password()
        
        driver.get(BASE_URL)
        safe_click(driver, Locators.Nav.LINK_CABINET)
        perform_login(driver, email, password)
        
        profile_element = wait_for_visible(driver, Locators.Login.CHECK_LOGGED_IN)
        assert profile_element.is_displayed(), f"Не удалось залогиниться с email: {email}"