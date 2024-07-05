from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
coffee_machine = CoffeeMaker()
money_counter = MoneyMachine()

is_on = True
while is_on:
    choice = input(f"What coffee do you wanna buy? {menu.get_items()}")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_machine.report()
    else:
        choice = menu.find_drink(choice)
        coffee_machine.is_resource_sufficient(choice)
        money_counter.make_payment(choice.cost)
        coffee_machine.make_coffee(choice)




