class MenuItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category  # "food" або "drink"

    def get_info(self):
        return f"Назва: {self.name}, Ціна: {self.price} грн, Категорія: {self.category}"


class FoodItem(MenuItem):
    def __init__(self, name, price, calories):
        super().__init__(name, price, "food")
        self.calories = calories

    def get_info(self):
        return super().get_info() + f", Калорії: {self.calories}"


class DrinkItem(MenuItem):
    def __init__(self, name, price, size):
        super().__init__(name, price, "drink")
        self.size = size  # "S", "M", "L"

    def get_info(self):
        return super().get_info() + f", Розмір: {self.size}"


class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.items = []
        self.status = "pending"  

    def add_item(self, item):
        if isinstance(item, MenuItem):
            self.items.append(item)
        else:
            raise ValueError("Об'єкт повинен бути типу MenuItem")

    def calculate_total(self):
        return sum(item.price for item in self.items)

    def set_status(self, status):
        if status in ["pending", "preparing", "ready", "completed"]:
            self.status = status
        else:
            raise ValueError("Недопустимий статус замовлення")

    def display_order(self):
        print(f"Замовлення #{self.order_id} (Статус: {self.status})")
        for item in self.items:
            print(f" - {item.get_info()}")
        print(f"Загальна сума: {self.calculate_total()} грн")



pizza = FoodItem("Піца Маргарита", 150, 800)
burger = FoodItem("Бургер Чізбургер", 120, 600)
coffee = DrinkItem("Кава Американо", 50, "M")
juice = DrinkItem("Апельсиновий сік", 70, "L")

order = Order(order_id=1)

order.add_item(pizza)
order.add_item(burger)
order.add_item(coffee)
order.add_item(juice)

order.display_order()

order.set_status("preparing")
order.display_order()

order.set_status("completed")
order.display_order()