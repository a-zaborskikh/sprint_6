import allure
from locators.header_page_locators import HeaderPageLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):
    """Класс Шапки сайта"""
    # driver = None

    def __init__(self, driver):
        super().__init__(driver)

    """Методы класса"""

    @allure.step("Клик по кнопке 'Заказать' из хедера")
    def click_header_order_btn(self):
        self.click_on_element(HeaderPageLocators.order_btn)

    @allure.step("Клик по лого 'Самокат' из хедера")
    def click_header_scooter_logo(self):
        self.click_on_element(HeaderPageLocators.scooter_logo)

    @allure.step("Клик по лого 'Яндекс' из хедера")
    def click_header_yandex_logo(self):
        self.click_on_element(HeaderPageLocators.yandex_logo)
