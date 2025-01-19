class Transport:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return f"Марка: {self.brand}, Модель: {self.model}, Рік випуску: {self.year}"

    def honk(self):
        return "Сигнал транспорту: Біп!"

# Клас Car (наслідується від Transport)
class Car(Transport):
    def __init__(self, brand, model, year, fuel_type):
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Тип пального: {self.fuel_type}"

    def honk(self):
        return "Сигнал автомобіля: Біп-біп!"

# Клас Bicycle (наслідується від Transport)
class Bicycle(Transport):
    def __init__(self, brand, model, year, gear_count):
        super().__init__(brand, model, year)
        self.gear_count = gear_count

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Кількість передач: {self.gear_count}"

    def honk(self):
        return "Сигнал велосипеда: Дзинь-дзинь!"

# Тестування
if __name__ == "__main__":
    # Створення об'єктів
    car = Car("Toyota", "Corolla", 2020, "Бензин")
    bicycle = Bicycle("Giant", "Escape 3", 2021, 21)

    # Виведення інформації
    print(car.get_info())
    print(car.honk())
    print(bicycle.get_info())
    print(bicycle.honk())