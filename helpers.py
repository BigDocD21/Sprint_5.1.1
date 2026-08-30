from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from constants import WAIT_TIMEOUT
from locators import Locators

def safe_click(driver, locator_tuple):
    wait = WebDriverWait(driver, WAIT_TIMEOUT)
    element = wait.until(EC.element_to_be_clickable(locator_tuple))
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    driver.execute_script("arguments[0].click();", element)
    return element

def wait_for_visible(driver, locator_tuple):
    wait = WebDriverWait(driver, WAIT_TIMEOUT)
    return wait.until(EC.visibility_of_element_located(locator_tuple))

def perform_login(driver, email, password):
    wait = WebDriverWait(driver, WAIT_TIMEOUT)
    
    email_field = wait.until(EC.element_to_be_clickable(Locators.Login.INPUT_EMAIL))
    email_field.clear()
    email_field.send_keys(email)
    
    password_field = wait.until(EC.element_to_be_clickable(Locators.Login.INPUT_PASSWORD))
    password_field.clear()
    password_field.send_keys(password)
    
    submit_btn = wait.until(EC.element_to_be_clickable(Locators.Login.BTN_SUBMIT))
    driver.execute_script("arguments[0].click();", submit_btn)

def perform_registration(driver, name, email, password):
    wait = WebDriverWait(driver, WAIT_TIMEOUT)
    
    name_field = wait.until(EC.element_to_be_clickable(Locators.Reg.FIELD_NAME))
    name_field.clear()
    name_field.send_keys(name)
    
    email_field = wait.until(EC.element_to_be_clickable(Locators.Reg.FIELD_EMAIL))
    email_field.clear()
    email_field.send_keys(email)
    
    password_field = wait.until(EC.element_to_be_clickable(Locators.Reg.FIELD_PASSWORD))
    password_field.clear()
    password_field.send_keys(password)
    
    submit_btn = wait.until(EC.element_to_be_clickable(Locators.Reg.BUTTON_REGISTER))
    driver.execute_script("arguments[0].click();", submit_btn)