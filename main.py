from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

nestle = CoffeeMaker()
cashier = MoneyMachine()
menu = Menu()
item = MenuItem()

is_on = True
profit = 0

while is_on:
    choice = input(f"What would you like? ({menu.get_items()}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        nestle.report()
        cashier.report()
    else:
        drink = menu.find_drink(choice)
        if nestle.is_resource_sufficient(drink):
            if cashier.make_payment(drink.cost):
                nestle.make_coffee(drink)

#make_payment already calls a function that processes the coins
