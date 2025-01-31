import allure
import pytest
from selenium import webdriver
from config import BaseURL


@allure.step("Инициализация драйвера Selenium")
@pytest.fixture(scope="function")
def setup_driver():
    """Фикстура для инициализации драйвера Selenium"""
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@allure.step("Открытие главной страницы с разворачиванием окна")
@pytest.fixture(scope="function")
def open_page(setup_driver):
    """Фикстура для открытия главной страницы с разворачиванием окна"""
    driver = setup_driver
    driver.get(BaseURL.get_base_url())
    driver.fullscreen_window()
    yield driver
