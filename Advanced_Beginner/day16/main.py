from menu import Menu, MenuItem
from cofee_maker import CoffeeMaker
from mm import MoneyMachine

cashier = MoneyMachine()
coffee_maker = CoffeeMaker()
waiter = Menu()

is_on = True
while is_on:
    options = waiter.get_items()
    choice = input(f"What would you like({options})?")
    if choice == 'off':
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        cashier.report()
    else:
        drink = waiter.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if cashier.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
