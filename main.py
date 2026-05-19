from hotel_logic import HotelSystem, Room, Guest

def main():
    system = HotelSystem()

    while True:
        print("\n--- ПАНЕЛЬ УПРАВЛЕНИЯ ОТЕЛЕМ ---")
        print("1. Добавить комнату | 2. Добавить гостя")
        print("3. Создать бронь    | 4. Просмотр данных (Rooms/Guests/Bookings)")
        print("5. Поиск и Фильтр   | 6. Управление (Update/Delete)")
        print("0. Выйти")

        choice = input("Выберите действие: ")

        # --- 1. Добавление ---
        if choice == "1":
            try:
                num = int(input("Номер: ")); r_type = input("Тип: "); price = float(input("Цена: "))
                system.add_room(Room(num, r_type, price))
                print("✅ Комната добавлена!")
            except ValueError: print("❌ Ошибка ввода!")

        elif choice == "2":
            try:
                g_id = int(input("ID гостя: ")); name = input("Имя: "); phone = input("Телефон: "); city = input("Город: ")
                system.add_guest(Guest(g_id, name, phone, city))
                print("✅ Гость добавлен!")
            except ValueError: print("❌ Ошибка ввода!")

        # --- 3. Бронирование ---
        elif choice == "3":
            try:
                b_id = int(input("ID брони: ")); r_num = int(input("Номер комнаты: "))
                g_id = int(input("ID гостя: ")); nights = int(input("Кол-во ночей: "))
                res = system.create_booking(b_id, r_num, g_id, nights)
                print(f"✅ Бронь создана! Итого: {res} KZT" if res else "❌ Ошибка бронирования.")
            except ValueError: print("❌ Ошибка!")

        # --- 4. Просмотр ---
        elif choice == "4":
            print("\n1. Все комнаты | 2. Все гости | 3. Все брони")
            sub = input("Выберите: ")
            if sub == "1": print(system.get_all_rooms())
            elif sub == "2": print(system.get_all_guests())
            elif sub == "3": print(system.get_all_bookings())

        # --- 5. Поиск и Фильтр ---
        elif choice == "5":
            print("\n1. Сортировка по цене | 2. Фильтр по типу")
            sub = input("Выберите: ")
            if sub == "1": print(system.sort_rooms())
            elif sub == "2": print(system.filter_rooms(input("Введите тип (Single/Double): ")))

        # --- 6. Управление ---
        elif choice == "6":
            print("\n1. Изменить цену | 2. Удалить комнату | 3. Сделать доступной")
            sub = input("Выберите: ")
            try:
                num = int(input("Введите номер комнаты: "))
                if sub == "1":
                    p = float(input("Новая цена: ")); system.update_price(num, p)
                elif sub == "2": system.delete_room(num)
                elif sub == "3": system.update_status(num, True)
                print("✅ Успешно выполнено!")
            except ValueError: print("❌ Ошибка ввода!")

        elif choice == "0":
            print("Выход."); break
        else: print("❌ Неверный выбор.")

if __name__ == "__main__":
    main()