class Chef:
    def prepare_dish(self, dish_name):
        # Simulating the preparation process
        print(f"Chef is preparing {dish_name}.")

class Menu:
    def __init__(self):
        self.available_dishes = []

    def add_dish(self, dish_name):
        self.available_dishes.append(dish_name)

    def display_menu(self):
        print("Menu:")
        for dish in self.available_dishes:
            print(f"- {dish}")

# Creating instances
menu = Menu()
chef = Chef()

# Adding dishes to the menu
menu.add_dish("Spaghetti Bolognese")
menu.add_dish("Chicken Alfredo")

# Displaying the menu
menu.display_menu()

# Customer orders a dish
customer_order = "Spaghetti Bolognese"
chef.prepare_dish(customer_order)
