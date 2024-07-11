class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_item_price(self, item_name):
        return self.items.get(item_name)

    def update_item_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price


# Создание объектов класса Store
store1 = Store("Продукты у дома", "ул. Ленина, 1")
store2 = Store("Супермаркет 'Звезда'", "пр. Мира, 15")
store3 = Store("Мини-маркет 'Удача'", "ул. Гагарина, 7")

# Добавление товаров в магазины
store1.add_item("хлеб", 30)
store1.add_item("молоко", 60)
store1.add_item("яйца", 80)

store2.add_item("мясо", 300)
store2.add_item("рыба", 250)
store2.add_item("овощи", 100)

store3.add_item("фрукты", 150)
store3.add_item("сок", 90)
store3.add_item("печенье", 70)

# Тестирование методов
print(f"Цена хлеба в {store1.name}: {store1.get_item_price('хлеб')} руб.")
store1.update_item_price("хлеб", 35)
print(f"Новая цена хлеба в {store1.name}: {store1.get_item_price('хлеб')} руб.")

print(f"Цена мяса в {store2.name}: {store2.get_item_price('мясо')} руб.")
store2.remove_item("мясо")
print(f"Цена мяса после удаления в {store2.name}: {store2.get_item_price('мясо')}")

print(f"Цена сока в {store3.name}: {store3.get_item_price('сок')} руб.")
print(f"Цена несуществующего товара в {store3.name}: {store3.get_item_price('кофе')}")