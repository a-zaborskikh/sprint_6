from selenium.webdriver.common.by import By


class HeaderPageLocators:
    """Класс локаторов Шапки сайта"""

    order_btn = [By.CLASS_NAME, 'Button_Button__ra12g']  # Кнопка "Заказать"

    scooter_logo = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']  # Лого "Самокат"
    yandex_logo = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']  # Лого "Яндекс"
