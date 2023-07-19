"""
F.O.O.D.Y. - [F]antastic [O]rganized [O]ptions for [D]elightful [Y]umminess

FOODY is a simple tool, that lets you create a pool of dishes you usually cook / want to cook and
organizes them in the background.

You can set your starting day of the week and for how many weekdays you need to plan in advance.
The app will randomly choose dishes from the pool and assign them to a weekday, once done
it will write everything (means Weekday and dish at the moment) into a file (simple textfile for now).

"""


class Dish:

    def __init__(self, name: str):
        self.name = name

    def display_dish(self):
        return f'Name: {self.name}'


class Menu:

    def __init__(self):
        self.dish_list = []

    def add_dish(self):
        new_dish_name = input("Welches Gericht möchtest du hinzufügen? \n ")
        new_dish = Dish(new_dish_name)
        self.dish_list.append(new_dish)

    def display_menu(self):
        for dish in self.dish_list:
            print(dish.display_dish())


new_menu = Menu()
i = int(input("Wie viele Gerichte möchten Sie hinzufügen?"))
j = 0
while j < i:
    new_menu.add_dish()
    j += 1

