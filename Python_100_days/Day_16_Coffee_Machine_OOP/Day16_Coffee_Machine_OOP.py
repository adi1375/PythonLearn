from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffe_maker = CoffeeMaker()
money = MoneyMachine()
menu = Menu()

repeat = True
while repeat:
    menu_items = menu.get_items()
    order = input(f"What would you like to order? {menu_items} ").lower()
    if order == "off":
        repeat=False
        print("Good Bye.")
    elif order == "report":
        coffe_maker.report()
        money.report()
    else:
        drink = menu.find_drink(order)
        if coffe_maker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffe_maker.make_coffee(drink)
        