import allure
from selenium.webdriver.common.action_chains import ActionChains
from locators.order_page_locators import OrderPageLocators
from helpers import RandomDataGenerator, MetroStationGenerator
from pages.base_page import BasePage


class OrderPage(BasePage):
    """Класс страницы Оформления заказов"""
    def __init__(self, driver):
        super().__init__(driver)
        self.generator_data = RandomDataGenerator()
        self.generator_state = MetroStationGenerator()
        self.actions = ActionChains(driver)

    """Методы класса"""
    @allure.step('Заполнение поля "Имя"')
    def enter_name_input(self, value):
        self.send_keys(OrderPageLocators.name_input, value)

    @allure.step('Заполнение поля "Фамилия"')
    def enter_lastname_input(self, value):
        self.send_keys(OrderPageLocators.lastname_input, value)

    @allure.step('Заполнение поля "Адрес"')
    def enter_address_input(self, value):
        self.send_keys(OrderPageLocators.address_input, value)

    @allure.step('Выбор станции метро')
    def select_metro_station_dropdown(self, value):
        self.send_keys(OrderPageLocators.metro_station_dropdown, value)
        self.press_arrow_down()
        self.press_enter()
        self.perform_actions()

    @allure.step('Заполнение поля "Телефон"')
    def enter_phone_input(self, value):
        self.send_keys(OrderPageLocators.phone_input, value)

    @allure.step('Клик по кнопке "Далее"')
    def click_next_btn(self):
        self.click_on_element(OrderPageLocators.next_btn)

    @allure.step('Клик по инпуту с выбор дат')
    def click_date_input(self):
        self.click_on_element(OrderPageLocators.date_rent_today_input)

    @allure.step('Клик по сегодняшней дате в календаре')
    def click_today_datepicker(self):
        self.click_on_element(OrderPageLocators.date_rent_today_datepick)

    @allure.step('Клик по дропдауну со списком дат аренды')
    def click_rent_period_dropdown(self):
        self.click_on_element(OrderPageLocators.rent_period_dropdown)

    @allure.step('Рандомный выбор периода аренды из списка')
    def select_rent_period(self):
        self.select_random_option(OrderPageLocators.rent_period_dropdown_list)

    @allure.step('Рандомный выбор периода аренды из списка')
    def select_color_checkboxes(self):
        self.select_random_option(OrderPageLocators.colors_checkboxes)

    @allure.step('Заполнение поля "Комментарий"')
    def enter_comments_input(self, value):
        self.send_keys(OrderPageLocators.comments_input, value)

    @allure.step('Клик по кнопке "Заказать"')
    def click_order_btn(self):
        self.click_on_element(OrderPageLocators.order_btn)

    @allure.step('Клик по кнопке "Да" при подтверждении заказа')
    def click_confirm_order_btn(self):
        self.click_on_element(OrderPageLocators.confirm_order_btn)

    @allure.step('Получение текста "Оформить заказ"')
    def get_title_order_placed(self):
        return self.get_actually_text(OrderPageLocators.title_order_placed)

    """Готовый сборник методов"""
    @allure.step('Заполнение формы "Для кого самокат"')
    def enter_random_data_in_form_personal_info(self):
        self.enter_name_input(self.generator_data.get_first_name())
        self.enter_lastname_input(self.generator_data.get_last_name())
        self.enter_address_input(self.generator_data.get_address())
        self.select_metro_station_dropdown(self.generator_state.get_random_station())
        self.enter_phone_input(self.generator_data.get_phone_number())
        self.click_next_btn()

    @allure.step('Заполнение формы "Про аренду"')
    def enter_random_data_in_form_rental_info(self):
        self.click_date_input()
        self.click_date_input()
        self.click_today_datepicker()
        self.click_rent_period_dropdown()
        self.select_rent_period()
        self.select_color_checkboxes()
        self.enter_comments_input(self.generator_data.get_random_comment())
        self.click_order_btn()
        self.click_confirm_order_btn()
