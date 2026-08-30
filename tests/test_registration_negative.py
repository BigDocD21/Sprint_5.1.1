import pytest
from helpers import perform_registration, wait_for_visible, safe_click
from constants import BASE_URL, generate_unique_email
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegistrationInvalidPassword:
    def test_registration_invalid_password(self, driver):

        email = generate_unique_email()
        name = "Дима"
        
        invalid_password = "123" 

        driver.get(f"{BASE_URL}/register")
        
        perform_registration(driver, name, email, invalid_password)
        
        assert "/register" in driver.current_url, \
            "Ошибка: неожиданно перешли на страницу входа. Регистрация прошла успешно, хотя пароль был невалидным."
        
        form_container = wait_for_visible(driver, Locators.Reg.FORM_CONTAINER)
        assert form_container.is_displayed(), "Форма регистрации исчезла после попытки регистрации с неверным паролем."
        