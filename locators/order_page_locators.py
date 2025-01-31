from selenium.webdriver.common.by import By


class OrderPageLocators:
    """Класс локаторов страницы Оформления Заказа"""

    """Локаторы для формы заказа с персональной информацией"""
    name_input = [By.XPATH, '//input[contains(@placeholder, "Имя")]']  # Инпут "Имя"
    lastname_input = [By.XPATH, '//input[contains(@placeholder, "Фамилия")]']  # Инпут "Фамилия"
    address_input = [By.XPATH, '//input[contains(@placeholder, "Адрес")]']  # Инпут "Адрес"
    metro_station_dropdown = [By.XPATH, '//input[contains(@placeholder, "Станция")]']  # DropDown "Станция метро"
    phone_input = [By.XPATH, '//input[contains(@placeholder, "Телефон")]']  # Инпут "Телефон"
    next_btn = [By.XPATH, '//div[contains(@class, "Order")]/button']  # Кнопка "Далее"

    """Локаторы для формы заказа с информацией об аренде"""
    date_rent_today_input = [By.XPATH, '//input[contains(@placeholder, "Когда привезти")]']  # Инпут "Когда привезти"
    date_rent_today_datepick = [By.XPATH, '//div[contains(@class, "day--today")]']  # Датапикер с датой сегодня
    rent_period_dropdown = [By.XPATH, '//div[contains(text(), "Срок аренды")]']  # DropDown "Срок аренды"
    rent_period_dropdown_list = [By.CLASS_NAME, 'Dropdown-menu']  # Список вариантов "Срок аренды"
    colors_checkboxes = [By.CLASS_NAME, 'Checkbox_Input__14A2w']  # Все чекбоксы "Цвет самоката"
    comments_input = [By.XPATH, '//input[contains(@placeholder, "Комментарий")]']  # Инпут "Комментарий"
    order_btn = [By.XPATH, '//*[contains(@class,"Order_B")]/button[text()="Заказать"]']  # Кнопка "Заказать"
    confirm_order_btn = [By.XPATH, '//button[contains(@class, "1CSJM")][text()="Да"]']  # Кнопка "Да"
    title_order_placed = [By.XPATH, '//div[contains(@class,"Order_ModalHeader")]']  # Заголовок "Заказ оформлен"
