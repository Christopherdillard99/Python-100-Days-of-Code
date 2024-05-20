# Coffee Machine using Object-Oriented Programming:
# starting code is provided in files for coffee_maker.py, menu.py, money_machine.py
# same variable names have been changes since the previous version but this OOP version most of the same logic. Read CAREFULLY.

# -------------------------------------------------------

# TODO 1: review functionality requirements for Coffee Machine Project:

# 1. Print Report
# 2. Check for whether resources are sufficient
# 3. Process the transaction of coins
# 4. Check to see if transaction is successful
# 5. Make the coffee

# -------------------------------------------------------

# TODO 2: read through the Coffee Machine Documentation to understand what each method and attribute does for the three classes (but here it is bellow):

# MenuItem Class
# Attributes:

        # - name
        # (str) The name of the drink.
        # e.g. “latte”
        # - cost
        # (float) The price of the drink.
        # e.g 1.5
        # - ingredients
        # (dictionary) The ingredients and amounts required to make the drink.
        # e.g. {“water”: 100, “coffee”: 16}

# Menu Class
# Methods:

        # - get_items()
        # Returns all the names of the available menu items as a concatenated string.
        # e.g. “latte/espresso/cappuccino”
        # - find_drink(order_name)
        # Parameter order_name: (str) The name of the drinks order.
        # Searches the menu for a particular drink by name. Returns a MenuItem object if it exists,
        # otherwise returns None.

# CoffeeMaker Class
# Methods:

        # - report()
        # Prints a report of all resources.
        # e.g.
        # Water: 300ml
        # Milk: 200ml
        # Coffee: 100g
        # - is_resource_sufficient(drink)
        # Parameter drink: (MenuItem) The MenuItem object to make.
        # Returns True when the drink order can be made, False if ingredients are insufficient.
        # e.g.
        # True
        # - make_coffee(order)
        # Parameter order: (MenuItem) The MenuItem object to make.
        # Deducts the required ingredients from the resources.

# MoneyMachine Class
# Methods:

        # - report()
        # Prints the current profit
        # e.g.
        # Money: $0
        # - make_payment(cost)
        # Parameter cost: (float) The cost of the drink.
        # Returns True when payment is accepted, or False if insufficient.
        # e.g. False

# -------------------------------------------------------

# TODO 3: start out in main.py with this code:
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# from the documentation, I can see that there are two report() methods that can be printed from the CoffeeMaker and the MoneyMachine classes for reports on remaining resources and total profit, respectively.

# start by creating objects from the three classes.
# using default Python snake case (with underscore as separator), so that the object's name reads the same to a human as its corresponding class name.

# 1. Creating Reports

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

money_machine.report()
coffee_maker.report()

        # the report is printed as:
        # Money: $0
        # Water: 300ml
        # Milk: 200ml
        # Coffee: 100g

# 2. Checking to see if resources are sufficient.

# there is a method for this in the CoffeeMaker class.
# just need to pass the drink name for the drink argument
# i.e. is_resource_sufficient(drink)
# additionally the Menu class has a method called get_items() that returns the names of all available menu items as a concatenated string " i.e. "latte/espresso/cappuccino" "
# also, the find_drink(order_name) method searches the money for name of drink and return the MenuItem object if it exists, otherwise it returns None. 

# make while loop for this checking if the machine is on.
# make sure to remove comments before running the code so that is doesn't surpass the character limit.

is_on = True

while is_on:
    options = menu.get_items() # this saves the options from the previously created menu object as a string into the new options variable.
    choice = input(f"What would you like? ({options})")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice) # the order_name argument as a string for the find_drink() method is the choice variable I created.
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink) # pass in the order drink as the input parameter.

# in the accompnaying files, there's already code that runs background reports for resources and money that with subsequent order.
# furthermore, the program automatically prints a message that the order cannot be fulfilled if the resources are not sufficient (look into the is_resource_sufficient(drink) method in the CoffeeMaker class to see more.).

# this resulting code using Object Oriented Programming is much simpler, while still being easy to interpret:

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
money_machine.report()
coffee_maker.report()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options})")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
