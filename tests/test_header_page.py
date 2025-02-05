import allure
from config import BaseURL
from data import OtherUrls
from pages.base_page import BasePage
from pages.header_page import HeaderPage


class TestHeaderPage:
    """Тестирование Шапки страницы"""

    @allure.title('Логотип Самоката ведет на главную страницу сайта')
    @allure.description('Проверка базовой ссылки при клике на логотип Самоката')
    def test_transfer_to_main_by_scooter_logo_success(self, open_page):
        driver = open_page
        # инициализация классов
        header_page = HeaderPage(driver)
        base_page = BasePage(driver)

        # Клик по лого Самокат
        header_page.click_header_yandex_logo()

        # Проверяем, что по клику осуществляется переход на главную страницу
        assert base_page.get_current_url() == BaseURL().base_url

    @allure.title('Логотип Яндекса ведет на страницу сайта Дзен')
    @allure.description('При клике на логотип Яндекса открывается новая вкладка с сайтом Дзен')
    def test_transfer_to_dzen_by_yandex_logo_success(self, open_page):
        driver = open_page
        # инициализация классов
        header_page = HeaderPage(driver)
        base_page = BasePage(driver)

        # Клик по лого Яндекс
        header_page.click_header_yandex_logo()
        base_page.switch_to_window()

        # Проверяем, что открылась страница сайта Дзен
        assert base_page.wait_for_url_to_be(OtherUrls().dzen_url)
