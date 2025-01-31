import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class BasePage:
    """Базовый класс для страниц"""

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)

    def send_keys(self, locator, value):
        """Заполнить значением"""
        self.driver.find_element(*locator).send_keys(value)

    def click_on_element(self, locator):
        """Кликнуть по элементу"""
        self.driver.find_element(*locator).click()

    def find_element(self, locator):
        """Найти элемент"""
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        """Добавление всех элементов в список"""
        return self.driver.find_elements(*locator)

    def wait_for_visibility_of_element(self, locator, timeout=10):
        """Ожидание, пока элемент станет видимым"""
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        """Ожидание, пока элемент станет кликабельным."""
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_url_to_be(self, url, timeout=10):
        """Ожидание, пока URL страницы станет равным заданному."""
        return WebDriverWait(self.driver, timeout).until(EC.url_to_be(url))

    def scroll(self, locator):
        """Скролл до нужного элемента"""
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_current_url(self):
        """Получить текущий адрес страницы"""
        current_url = self.driver.current_url
        return current_url

    def get_actually_text(self, locator):
        """Получить фактический текст элемента"""
        actually_text = self.driver.find_element(*locator).text
        return actually_text

    def switch_to_window(self):
        """Переключиться на вкладку"""
        self.driver.switch_to.window(self.driver.window_handles[1])

    def press_arrow_down(self):
        """Нажатие клавиши 'Вниз'"""
        self.actions.send_keys(Keys.ARROW_DOWN)

    def press_enter(self):
        """Нажатие клавиши 'Enter'"""
        self.actions.send_keys(Keys.ENTER).perform()

    def perform_actions(self):
        """Выполняет все ожидающие действия в ActionChains"""
        self.actions.perform()

    def select_random_option(self, locator):
        """Выбор случайного элемента из списка"""
        options = self.driver.find_elements(*locator)
        if options:
            random_option = random.choice(options)
            random_option.click()
