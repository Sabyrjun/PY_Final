import unittest
import os
from hotel_logic import HotelSystem, Room


class TestHotelSystem(unittest.TestCase):

    # Этот метод запускается перед каждым тестом (создает тестовую базу)
    def setUp(self):
        self.system = HotelSystem("test_data.json")
        self.system.rooms = []  # Очищаем список для чистоты теста

    # Этот метод удаляет тестовую базу после выполнения тестов
    def tearDown(self):
        if os.path.exists("test_data.json"):
            os.remove("test_data.json")

    # Тест 1: Проверка добавления комнаты
    def test_add_room(self):
        room = Room(101, "Single", 15000.0)
        self.system.add_room(room)
        self.assertEqual(len(self.system.rooms), 1)
        self.assertEqual(self.system.rooms[0]["number"], 101)

    # Тест 2: Проверка поиска свободных комнат
    def test_get_available(self):
        self.system.add_room(Room(101, "Single", 15000.0, available=True))
        self.system.add_room(Room(102, "Double", 20000.0, available=False))

        available = self.system.get_available_rooms()
        self.assertEqual(len(available), 1)
        self.assertEqual(available[0]["number"], 101)

    # Тест 3: Проверка успешного бронирования
    def test_book_room(self):
        self.system.add_room(Room(200, "Suite", 50000.0, available=True))
        success = self.system.book_room(200)

        self.assertTrue(success)  # Бронь должна пройти
        self.assertFalse(self.system.rooms[0]["available"])  # Статус комнаты должен стать False


if __name__ == '__main__':
    unittest.main()