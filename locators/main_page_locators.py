from selenium.webdriver.common.by import By


class MainPageLocators:
    """Класс локаторов Главной страницы"""

    order_btn = [By.XPATH, '//button[contains(@class,"Button_Middle")][text()="Заказать"]']    # кнопка "Заказать"
    quest_accordion = [By.XPATH, "//div[@class='accordion__heading']"]  # аккордеон с вопросами
    answer_accordion = [By.XPATH, '//*[@class="accordion__panel"]/p']  # аккордеон с ответами

    @staticmethod
    def get_answer_text(quest_id):
        return [By.XPATH, f"//div[@id='accordion__panel-{quest_id}']/p"]
