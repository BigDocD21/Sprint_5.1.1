import pytest
from helpers import perform_registration, wait_for_visible, safe_click
from constants import BASE_URL, generate_unique_email, generate_unique_password
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegistrationFlow:
    def test_successful_registration(self, driver):
      
        name = "Дима"
        email = generate_unique_email()
        password = generate_unique_password()

        driver.get(f"{BASE_URL}/register")
        
        perform_registration(driver, name, email, password)
        
        wait = WebDriverWait(driver, 15)
        wait.until(EC.url_contains("/login"))
        
        login_email_field = wait_for_visible(driver, Locators.Login.INPUT_EMAIL)
        
        assert login_email_field.is_displayed(), \
            f"Ошибка регистрации: не удалось перейти на страницу входа. Использован email: {email}"
        