import pytest
from helpers import safe_click, perform_login, perform_registration, wait_for_visible
from constants import BASE_URL, generate_unique_email, generate_unique_password
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestNavigationFlow:
    def test_complex_navigation_flow(self, driver):

        email = generate_unique_email()
        password = generate_unique_password()
        name = "Дима"

        driver.get(f"{BASE_URL}/register")

        perform_registration(driver, name, email, password)
        
        wait = WebDriverWait(driver, 15)
        wait.until(lambda d: d.current_url.endswith("/login"))
        
        perform_login(driver, email, password)
        
        profile_element = wait_for_visible(driver, Locators.Login.CHECK_LOGGED_IN)
        assert profile_element.is_displayed(), f"Не удалось авторизоваться. Email: {email}"
        
        header_element = wait_for_visible(driver, Locators.Tabs.HEADER_TITLE)
        assert header_element.is_displayed(), "Заголовок страницы не отображается"

        safe_click(driver, Locators.Nav.LINK_CABINET)
        
        profile_inside = wait_for_visible(driver, Locators.Login.CHECK_LOGGED_IN)
        assert profile_inside.is_displayed(), "Не удалось попасть внутрь профиля для перехода в конструктор"
        
        safe_click(driver, Locators.Nav.LINK_CONSTRUCTOR)
        
        header_element_constructor = wait_for_visible(driver, Locators.Tabs.HEADER_TITLE)
        assert header_element_constructor.is_displayed(), "Заголовок не отображается на странице конструктора"
        
        current_url = driver.current_url
        assert "/constructor" in current_url or "/" in current_url, f"Неверный URL после перехода на конструктор: {current_url}"

        safe_click(driver, Locators.Nav.LINK_CABINET)
        
        profile_inside_return = wait_for_visible(driver, Locators.Login.CHECK_LOGGED_IN)
        assert profile_inside_return.is_displayed(), "Не удалось вернуться в личный кабинет"

        safe_click(driver, Locators.Nav.LINK_CONSTRUCTOR)
        
        header_element_final = wait_for_visible(driver, Locators.Tabs.HEADER_TITLE)
        assert header_element_final.is_displayed(), "Заголовок не отображается после возврата через логотип"
        
        final_url = driver.current_url
        assert final_url.endswith("/") or final_url.endswith("/constructor"), f"Неверный URL после возврата через логотип: {final_url}"

        safe_click(driver, Locators.Nav.LINK_CABINET)
        
        profile_inside = wait_for_visible(driver, Locators.Login.CHECK_LOGGED_IN)
        assert profile_inside.is_displayed(), "Не удалось попасть внутрь профиля для перехода в конструктор"
        
        safe_click(driver, Locators.Nav.LINK_CONSTRUCTOR)
        
        header_element_constructor = wait_for_visible(driver, Locators.Tabs.HEADER_TITLE)
        assert header_element_constructor.is_displayed(), "Заголовок не отображается на странице конструктора"
        
        current_url = driver.current_url
        assert "/constructor" in current_url or "/" in current_url, f"Неверный URL после перехода на конструктор: {current_url}"

        safe_click(driver, Locators.Nav.LINK_CABINET)
        
        profile_inside_return = wait_for_visible(driver, Locators.Login.CHECK_LOGGED_IN)
        assert profile_inside_return.is_displayed(), "Не удалось вернуться в личный кабинет"

        safe_click(driver, Locators.Nav.LOGO)
        
        header_element_final = wait_for_visible(driver, Locators.Tabs.HEADER_TITLE)
        assert header_element_final.is_displayed(), "Заголовок не отображается после возврата через логотип"
        
        final_url = driver.current_url
        assert final_url.endswith("/") or final_url.endswith("/constructor"), f"Неверный URL после возврата через логотип: {final_url}"