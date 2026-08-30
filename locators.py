from selenium.webdriver.common.by import By

class Locators:
    #1Навигация
    class Nav:
        LINK_CONSTRUCTOR = (By.CSS_SELECTOR, "a[href='/']")
        LOGO = (By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2 a")
        LINK_CABINET = (By.CSS_SELECTOR, "a[href='/account']")
        LINK_LOGIN_MAIN = (By.CSS_SELECTOR, "a[href='/login']")
        LINK_REGISTER = (By.CSS_SELECTOR, "a[href='/register']")
        LINK_RESTORE = (By.CSS_SELECTOR, "a[href='/forgot-password']")
        HEADER_TITLE = (By.CSS_SELECTOR, "h1.text_type_main-large")

    #2Вкладки
    class Tabs:
        TAB_BUNS = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG')]//span[contains(text(), 'Булки')]")
        TAB_SAUCES = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG')]//span[contains(text(), 'Соусы')]")
        TAB_FILLINGS = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG')]//span[contains(text(), 'Начинки')]")
        
        @staticmethod
        def get_active_parent_locator(tab_locator_tuple):
            
            xpath_string = tab_locator_tuple[1]
            return (By.XPATH, f"{xpath_string}/parent::div[contains(@class, 'tab_tab_type_current__2BEPc')]")

        HEADER_TITLE = (By.CSS_SELECTOR, "h1.text_type_main-large")

    #3.Вход
    class Login:
        INPUT_EMAIL = (By.CSS_SELECTOR, "input[type='text'][name='name']")
        INPUT_PASSWORD = (By.CSS_SELECTOR, "input[type='password']")
        BTN_SUBMIT = (By.CSS_SELECTOR, "button.button_button__33qZ0")
        CHECK_LOGGED_IN = (By.CSS_SELECTOR, "a[href='/account']")
        LINK_LOGOUT = (By.XPATH, "//button[contains(text(), 'Выход')]")
        LINK_LOGIN_INSIDE_FORM = (By.CSS_SELECTOR, "a[href='/login']")

    #4.Регистрация
    class Reg:
        FORM_CONTAINER = (By.CSS_SELECTOR, ".Auth_form__3qKeq")
        FIELD_NAME = (By.XPATH, "//label[contains(text(), 'Имя')]/following-sibling::input")
        FIELD_EMAIL = (By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input")
        FIELD_PASSWORD = (By.XPATH, "//label[contains(text(), 'Пароль')]/following-sibling::input")
        BUTTON_REGISTER = (By.CSS_SELECTOR, ".Auth_form__3qKeq button.button_button__33qZ0")