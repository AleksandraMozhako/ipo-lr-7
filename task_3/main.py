#Можако 4 вариант
import json
import os

def show_menu():
    print("Выберите пункт от 1 до 4:")
    print("1.Вывести все записи")
    print("2.Добавить запись")
    print("3.Удалить запись")
    print("4.Выйти")
    return input("Введите свой выбор: ")

def show_all_cars(cars):
    print("=" * 10 + "Все записи" + "="*10)
    if not cars:
        print("Записей нет")
    else:
        for car in cars:
            petrol_car = "Да" if car["is_petrol"] else "Нет"
            print(f"id: {car['id']}")
            print(f"Название модели: {car['name']}")
            print(f"Производитель: {car['manufacturer']}")
            print(f"Заправляется бензином: {petrol_car}")
            print(f"Объем бака в литрах: {car['tank_volume']}")
            print("-" * 50)

def add_car(cars):
    new_id = max([c["id"] for c in cars], default = 0) + 1
    name = input("Введите модель машины: ").strip()
    manufacturer = input("Введите производителя:").strip()
    is_petrol_input = input("Ваша машина заправляется бензином? (да/нет): ").strip().lower()
    is_petrol = True if is_petrol_input in ("да") else False 
    tank_volume = int(input("Введите объем в литрах: "))

    new_car = {
        "id": new_id,
        "name": name,
        "manufacturer": manufacturer,
        "is_petrol": is_petrol,
        "tank_volume": tank_volume
    }
    cars.append(new_car)

    with open("cars.json", "w", encoding="utf-8") as f:
        json.dump(cars, f, ensure_ascii=False, indent=4)
    print("Запись добавлена")

def delete_car(cars):
    old_id = int(input("Введите id машины для удаления: "))
    len_before = len(cars)
    cars[:] = [c for c in cars if c["id"] != old_id]

    if len(cars) == len_before:
        print("="*10 + " Машина с данным id не найдена " + "=" * 10)
    else:
        for index, car in enumerate(cars, start=1):
            car["id"] = index
            
        with open("cars.json", "w", encoding="utf-8") as f:
            json.dump(cars, f, ensure_ascii = False, indent = 4)
        print("Запись удалена")
    return cars

def main():
    print("start code ...")
    if os.path.exists("cars.json"):
        with open("cars.json", "r", encoding="utf-8") as f:
            cars = json.load(f)
    else:
        cars = []

    while True:
        choice = show_menu()

        if choice == "1":
            show_all_cars(cars)
        elif choice == "2":
            add_car(cars)
        elif choice == "3":
            cars = delete_car(cars)
        elif choice == "4":
            break
        else:
            print("Неправильный ввод")

    print("... end code")

if __name__ == "__main__":
    main()
