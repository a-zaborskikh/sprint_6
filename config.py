class BaseURL:
    """Класс для хранения базовых URL приложения."""

    base_url = 'https://qa-scooter.praktikum-services.ru/'

    @classmethod
    def get_base_url(cls):
        """Метод для получения базового URL."""
        return cls.base_url
