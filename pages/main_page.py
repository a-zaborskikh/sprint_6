import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    """Класс Главной страницы"""

    def __init__(self, driver):
        super().__init__(driver)

    """Методы класса"""
    @allure.step("Скролл до кнопки 'Заказать' на Главной странице")
    def scroll_to_order_btn(self):
        self.scroll(MainPageLocators.order_btn)

    @allure.step("Клик по кнопке 'Заказать' на Главной странице")
    def click_order_btn(self):
        self.click_on_element(MainPageLocators.order_btn)

    @allure.step("Скролл к блоку с вопросами")
    def scroll_to_quest(self):
        self.scroll(MainPageLocators.quest_accordion)

    @allure.step("Найти и кликнуть вопрос из блока вопросов")
    def find_and_click_elements(self, question_id):
        elements = self.find_elements(MainPageLocators.quest_accordion)
        elements[question_id].click()

    @allure.step("Ожидание и получение текста ответа из вопроса")
    def get_answer_text(self, question_id):
        self.wait_for_visibility_of_element(MainPageLocators.get_answer_text(question_id))
        return self.get_actually_text(MainPageLocators.get_answer_text(question_id))

    """Готовый сборник методов"""
    @allure.step("Скролл и клик по кнопке 'Заказать' на Главной странице")
    def click_main_order_btn(self):
        self.scroll_to_order_btn()
        self.click_order_btn()

    @allure.step('Нажать на один из вопросов списка')
    def click_question_buttons(self, question_id):
        self.scroll_to_quest()
        self.find_and_click_elements(question_id)
