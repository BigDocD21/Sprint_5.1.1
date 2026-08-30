import pytest
from selenium.webdriver.common.by import By
from helpers import safe_click, wait_for_visible
from constants import BASE_URL
from locators import Locators

class TestIngredientsTabs:
    def test_page_loads_and_header_visible(self, driver):

        driver.get(BASE_URL)
        header = wait_for_visible(driver, Locators.Tabs.HEADER_TITLE)
        assert header.is_displayed(), "Заголовок страницы не отображается"


    def test_switch_to_sauces_tab(self, driver):

        driver.get(BASE_URL)
        safe_click(driver, Locators.Tabs.TAB_SAUCES)
        
        active_locator = Locators.Tabs.get_active_parent_locator(Locators.Tabs.TAB_SAUCES)
        active_tab = wait_for_visible(driver, active_locator)
        assert "tab_tab_type_current" in active_tab.get_attribute("class"), "Вкладка 'Соусы' не стала активной"


    def test_switch_to_fillings_tab(self, driver):

        driver.get(BASE_URL)
        safe_click(driver, Locators.Tabs.TAB_FILLINGS)
        
        active_locator = Locators.Tabs.get_active_parent_locator(Locators.Tabs.TAB_FILLINGS)
        active_tab = wait_for_visible(driver, active_locator)
        assert "tab_tab_type_current" in active_tab.get_attribute("class"), "Вкладка 'Начинки' не стала активной"

    def test_switch_to_buns_tab(self, driver):
        driver.get(BASE_URL)
        safe_click(driver, Locators.Tabs.TAB_BUNS)
        
        active_locator = Locators.Tabs.get_active_parent_locator(Locators.Tabs.TAB_BUNS)
        active_tab = wait_for_visible(driver, active_locator)
        assert "tab_tab_type_current" in active_tab.get_attribute("class")
        
        ingredients_list = wait_for_visible(driver, (By.CSS_SELECTOR, "ul.BurgerIngredients_ingredients__list__2A-mT"))
        assert ingredients_list.is_displayed()