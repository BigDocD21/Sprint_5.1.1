#1:Навигация
LOCATORS_NAV = {
    #Ссылка на главную страницу (Конструктор)
    "link_constructor": "a[href='/']",
    
    #Логотип в шапке сайта
    "logo": "a.AppHeader_header__logo__2D0X2",
    
    # Ссылка "Личный Кабинет" на главной странице
    "link_cabinet": "a[href='/account']",
    
    #Ссылка на страницу входа
    "link_login_main": "a[href='/login']",
    
    # Ссылка на страницу регистрации
    "link_register": "a[href='/register']",
    
    # Ссылка на восстановление пароля
    "link_restore": "a[href='/forgot-password']",
    
    #Заголовок "Соберите бургер"
    "header_title": "h1.text_type_main-large"
}


#2: Вкладки
LOCATORS_TABS = {
    #Вкладка "Булки"
    "tab_buns": "//div[contains(@class, 'tab_tab__1SPyG')]//span[contains(text(), 'Булки')]",
    
    #Вкладка "Соусы"
    "tab_sauces": "//div[contains(@class, 'tab_tab__1SPyG')]//span[contains(text(), 'Соусы')]",
    
    #Вкладка "Начинки"
    "tab_fillings": "//div[contains(@class, 'tab_tab__1SPyG')]//span[contains(text(), 'Начинки')]"
}

#3:Вход
LOCATORS_LOGIN = {
    #Поле ввода Email
    "input_email": "input[type='text'][name='name']",
    
    # Поле ввода пароля
    "input_password": "input[type='password']",
    
    #Кнопка "Войти"
    "btn_submit": "button.button_button__33qZ0",
    
    # Элемент подтверждения входа
    "check_logged_in": "a[href='/account']",
    
    #Ссылка "Выйти"
    "link_logout": "a[href='/logout']"
}


#4:Регистрация
LOCATORS_REG = {
    # Контейнер всей формы регистрации
    "form_container": ".Auth_form__3qKeq",
    
    #Поле ввода имени пользователя
    "field_name": ".Auth_form__3qKeq input[name='name']",
    
    # Поле ввода Email
    "field_email": ".Auth_form__3qKeq input[type='text']",
    
    #Поле ввода пароля
    "field_password": ".Auth_form__3qKeq input[type='password']",
    
    #Кнопка "Зарегистрироваться"
    "button_register": ".Auth_form__3qKeq button.button_button__33qZ0"
}