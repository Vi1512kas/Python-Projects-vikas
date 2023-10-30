from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
my_moneyMachine = MoneyMachine()
my_coffeMaker = CoffeeMaker()
print((my_coffeMaker.report()))
print(my_moneyMachine.report())