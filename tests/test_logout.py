import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from helpers import safe_click, perform_login, perform_registration, wait_for_visible
from constants import BASE_URL, generate_unique_email, generate_unique_password
from locators import Locators

class TestLogoutFlow:
    def test_logout_from_personal_cabinet(self, driver):
        
        email = generate_unique_email()
        password = generate_unique_password()
        name = "Дима"
        
        driver.get(f"{BASE_URL}/register")
        
        perform_registration(driver, name, email, password)
        
        wait = WebDriverWait(driver, 15)
        wait.until(lambda d: d.current_url.endswith("/login"))
        
        perform_login(driver, email, password)

        profile_element = wait_for_visible(driver, Locators.Login.CHECK_LOGGED_IN)
        assert profile_element.is_displayed(), f"Пользователь не авторизован после входа. Email: {email}"

        header_element = wait_for_visible(driver, Locators.Tabs.HEADER_TITLE)
        assert header_element.is_displayed(), "Заголовок страницы не отображается"

        safe_click(driver, Locators.Nav.LINK_CABINET)
        
        profile_inside = wait_for_visible(driver, Locators.Login.CHECK_LOGGED_IN)
        assert profile_inside.is_displayed(), "Не удалось попасть внутрь профиля для выхода."
        
        safe_click(driver, Locators.Login.LINK_LOGOUT)
        
        login_email_field = wait_for_visible(driver, Locators.Login.INPUT_EMAIL)
        assert login_email_field.is_displayed(), "Кнопка 'Кабинет' не появилась после выхода."
        
       