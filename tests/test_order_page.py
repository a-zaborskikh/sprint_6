import allure
import pytest
from pages.header_page import HeaderPage
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:
    """Тестирование страницы 'Оформление заказа'"""
    @allure.title('Заказ корректно оформляется на обоих этапах')
    @allure.description('Оформление заказа по кнопке "Заказать из хедера и на главной страницы"')
    @pytest.mark.parametrize("order_button_action", ["header", "main"])
    def test_order_placement_success(self, open_page, order_button_action):
        driver = open_page
        # инициализация классов
        self.header_page = HeaderPage(driver)
        self.main_page = MainPage(driver)
        self.order_page = OrderPage(driver)

        # Клик по кнопке "Заказать" в зависимости от параметра
        if order_button_action == "header":
            self.header_page.click_header_order_btn()
        elif order_button_action == "main":
            self.main_page.click_main_order_btn()

        # Ввод рандомных данных в форму заказа с персональной информацией
        self.order_page.enter_random_data_in_form_personal_info()
        # Ввод рандомных данных в форму заказа с информацией об аренде
        self.order_page.enter_random_data_in_form_rental_info()

        # Проверяем, что заказ успешно оформлен
        check_place_order_txt = self.order_page.get_title_order_placed()
        assert "Заказ оформлен" in check_place_order_txt
