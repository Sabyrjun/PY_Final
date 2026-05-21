import json
import os

# ООП: Базовый класс
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def get_role(self):
        return "Person"

# ООП: Наследование
class Guest(Person):
    def __init__(self, id, name, phone, city):
        super().__init__(id, name)
        self.phone = phone
        self.city = city
    def get_role(self):
        return "Guest"
    def to_dict(self):
        return {"id": self.id, "name": self.name, "phone": self.phone, "city": self.city, "role": self.get_role()}

class Room:
    def __init__(self, number, r_type, price, available=True):
        self.number = number
        self.type = r_type
        self.price = price
        self.available = available
    def to_dict(self):
        return {"number": self.number, "type": self.type, "price": self.price, "available": self.available}

class HotelSystem:
    def __init__(self, filename="data.json"):
        self.filename = filename
        # ГАРАНТИЯ: Инициализация ДО всего остального
        self.data = {"rooms": [], "guests": [], "bookings": []}
        self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    loaded = json.load(f)
                    if isinstance(loaded, dict):
                        self.data = loaded
            except:
                self.data = {"rooms": [], "guests": [], "bookings": []}

    def save_data(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=4)

    # Функции с параметрами и возвращаемыми значениями
    def add_room(self, room):
        self.data["rooms"].append(room.to_dict())
        self.save_data()

    def add_guest(self, guest):
        self.data["guests"].append(guest.to_dict())
        self.save_data()

    def find_room(self, number):
        for r in self.data["rooms"]:
            if r["number"] == number:
                return r
        return None

    def create_booking(self, b_id, room_num, guest_id, nights):
        room = self.find_room(room_num)
        if room and room["available"]:
            room["available"] = False
            # Расчет цены
            total_price = room["price"] * nights
            # Сохраняем бронь вместе с ценой
            self.data["bookings"].append({
                "bId": b_id, "roomNum": room_num, "guestId": guest_id, "nights": nights, "totalPrice": total_price})
            self.save_data()
            return total_price  # Возвращаем цену, чтобы вывести её пользователю
        return False

    # Advanced: Filter + Lambda
    def filter_rooms(self, r_type):
        return list(filter(lambda x: x["type"].lower() == r_type.lower(), self.data["rooms"]))

    # Advanced: Lambda сортировка
    def sort_rooms(self):
        return sorted(self.data["rooms"], key=lambda x: x["price"])


    def update_price(self, number, new_price):
        room = self.find_room(number)
        if room:
            room["price"] = new_price
            self.save_data()
            return True
        return False

    def update_status(self, number, status):
        room = self.find_room(number)
        if room:
            room["available"] = status
            self.save_data()
            return True
        return False

    def get_all_rooms(self): return self.data.get("rooms", [])
    def get_all_guests(self): return self.data.get("guests", [])
    def get_all_bookings(self): return self.data.get("bookings", [])