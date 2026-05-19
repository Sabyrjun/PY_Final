# Требование 7: Использование модулей из других файлов
from hotel_logic import HotelSystem, Room


def main():
    system = HotelSystem()

    # Требование 2: Цикл while для меню
    while True:
        print("\n--- СИСТЕМА УПРАВЛЕНИЯ ОТЕЛЕМ ---")
        print("1. Добавить новую комнату")
        print("2. Показать свободные комнаты")
        print("3. Забронировать комнату")
        print("4. Выйти")

        # Требование 1: User input
        choice = input("Выберите действие (1-4): ")

        if choice == "1":
            # Требование 9: Input validation (Проверка ввода на ошибки)
            try:
                num = int(input("Введите номер комнаты (число): "))
                r_type = input("Введите тип (например, Single): ")
                price = float(input("Введите цену за ночь: "))

                new_room = Room(num, r_type, price)
                system.add_room(new_room)
                print("✅ Комната успешно добавлена!")
            except ValueError:
                print("❌ Ошибка: Номер комнаты и цена должны быть числами!")

        elif choice == "2":
            available = system.get_available_rooms()
            print("\n--- Свободные комнаты ---")
            for r in available:
                print(f"Номер: {r['number']}, Тип: {r['type']}, Цена: {r['price']}")

        elif choice == "3":
            try:
                num = int(input("Введите номер комнаты для брони: "))
                if system.book_room(num):
                    print("✅ Комната успешно забронирована!")
                else:
                    print("❌ Комната не найдена или уже занята.")
            except ValueError:
                print("❌ Ошибка: Введите корректный номер!")

        elif choice == "4":
            print("До свидания!")
            break  # Выход из цикла

        else:
            print("❌ Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()