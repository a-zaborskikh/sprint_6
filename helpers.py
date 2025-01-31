import random
from faker import Faker


class RandomDataGenerator:
    def __init__(self):
        self.fake = Faker('ru_RU')

    def get_first_name(self):
        return self.fake.first_name()

    def get_last_name(self):
        return self.fake.last_name()

    def get_address(self):
        return self.fake.street_name() + ', дом ' + str(random.randint(1, 100))

    def get_phone_number(self):
        return self.fake.numerify('8925#######')

    def get_random_comment(self):
        """Генерация рандомного комментария"""
        if random.choice([True, False]):
            random_comment = self.fake.sentence()
        else:
            random_comment = ""

        return random_comment


class MetroStationGenerator:
    def __init__(self):
        self.metro_stations = [
            "Александровский сад",
            "Арбатская",
            "Беляево",
            "Библиотека им. Ленина",
            "Варшавская",
            "Киевская",
            "Краснопресненская",
            "Кутузовская",
            "Парк Культуры",
            "Смоленская",
            "Таганская",
            "Тверская",
            "Чистые пруды",
            "Щёлковская",
        ]

    def get_random_station(self):
        return random.choice(self.metro_stations)
