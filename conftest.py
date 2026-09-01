import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from constants import WAIT_TIMEOUT
from helpers import safe_click, perform_login, perform_registration, wait_for_visible
from constants import BASE_URL, generate_unique_email, generate_unique_password
from locators import Locators

@pytest.fixture(scope="class")
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_used": 0,
        "credentials_use_account_storage": False,
        "autofill.enabled": False
    }
    options.add_experimental_option("prefs", prefs)
    
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    
    options.add_argument("--log-level=3")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def authorized_user(driver):
    email = generate_unique_email()
    password = generate_unique_password()
    name = "Дима"

    driver.get(f"{BASE_URL}/register")
    perform_registration(driver, name, email, password)
    
    driver.get(f"{BASE_URL}/login")

    perform_login(driver, email, password)

    wait_for_visible(driver, Locators.Login.CHECK_LOGGED_IN)
    
    yield driver