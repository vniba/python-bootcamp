
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_is = True

while machine_is:
    user_choice = input(f"what would you like? {menu.get_items()}: ").lower()

    if user_choice == 'off':
        machine_is = False

    elif user_choice == 'report':
        coffee_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
