import random
# __________________Exercise 1 : Geometry____________________________

class circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def print_definition(self):
        print(f"Circle with radius {self.radius}")


# __________________Exercise 2 : Custom List Class____________________________

class MyList:
    def __init__(self, letters):
        self.letters = letters

    def reverse(self):
        return self.letters[::-1]

    def sort(self):
        return sorted(self.letters)

    def random(self):
        return [random.randint(0, 100) for i in range(len(self.letters))]


# __________________Exercise 3 : Restaurant Menu Manager____________________________

class MenuManager:
    def __init__(self, menu):
        self.menu = menu

    def add_item(self, name, price, spice, gluten):
        self.menu.append(
            {"name": name, "price": price, "spice": spice, "gluten": gluten}
        )

    def update_item(self, name, price, spice, gluten):
        for item in self.menu:
            if item["name"] == name:
                item["price"] = price
                item["spice"] = spice
                item["gluten"] = gluten
                return
        print("Dish not in menu")

    def remove_item(self, name):
        for item in self.menu:
            if item["name"] == name:
                self.menu.remove(item)
                return
        print("Dish not in menu")


menu_list = [
    {"name": "Soup", "price": 10, "spice": "B", "gluten": False},
    {"name": "Hamburger", "price": 15, "spice": "A", "gluten": True},
    {"name": "Salad", "price": 18, "spice": "A", "gluten": False},
    {"name": "French Fries", "price": 5, "spice": "C", "gluten": False},
    {"name": "Beef bourguignon", "price": 25, "spice": "B", "gluten": True},
]