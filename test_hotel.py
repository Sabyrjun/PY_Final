import unittest
import os
from hotel_logic import HotelSystem, Room


class TestHotelSystem(unittest.TestCase):

    def setUp(self):
        # Создаем систему с тестовым файлом
        self.system = HotelSystem("test_data.json")
        # Принудительно очищаем данные перед каждым тестом
        self.system.data = {"rooms": [], "guests": [], "bookings": []}

    def tearDown(self):
        # Удаляем тестовый файл после тестов
        if os.path.exists("test_data.json"):
            os.remove("test_data.json")

    # Тест 1: Проверка добавления комнаты
    def test_add_room(self):
        room = Room(101, "Single", 15000.0)
        self.system.add_room(room)
        # Проверяем теперь через словарь data
        self.assertEqual(len(self.system.data["rooms"]), 1)
        self.assertEqual(self.system.data["rooms"][0]["number"], 101)

    # Тест 2: Проверка фильтрации
    def test_filter_rooms(self):
        self.system.add_room(Room(101, "Single", 15000.0, available=True))
        self.system.add_room(Room(102, "Double", 20000.0, available=True))

        filtered = self.system.filter_rooms("Single")
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0]["number"], 101)

    # Тест 3: Проверка успешного бронирования
    def test_create_booking(self):
        self.system.add_room(Room(200, "Suite", 50000.0, available=True))
        # Бронируем
        success = self.system.create_booking(1, 200, 1, 2)

        self.assertTrue(success)  # Должно вернуть цену (True)
        # Проверяем, что комната стала недоступной
        room = self.system.find_room(200)
        self.assertFalse(room["available"])


if __name__ == '__main__':
    unittest.main()