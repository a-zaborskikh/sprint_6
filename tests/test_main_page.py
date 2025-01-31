import allure
import pytest
from data import QuestData
from pages.main_page import MainPage


class TestMainPage:
    """Тестирование Главной страницы"""
    @allure.title('Вопрос корректно раскрывается при клике. Текст ответа соответствует ожидаемому')
    @allure.description('Каждый вопрос кликабелен, ответ на вопрос соответствует ождаемому тексту')
    @pytest.mark.parametrize("question_id, expected", QuestData.test_data)
    def test_answers_text_to_questions(self, open_page, question_id, expected):
        driver = open_page
        # инициализация классов
        main_page = MainPage(driver)

        # Клик по вопросу
        main_page.click_question_buttons(question_id)

        # Проверяем, что текст ответа соответствует ожидаемому результату
        assert main_page.get_answer_text(question_id) == expected
