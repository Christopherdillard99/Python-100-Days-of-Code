# Day 15: Virtual Coffee Machine Project:
# Vairtual Coffee Machine Project code starting at line 46:

# Setting up a Local Developement Environment:
# IDE - Integrated Development Environment:
# some examples are Jupitor, Thonny, Spider, VS Code

# I will be using PyCharm (IDE specialized for Python)

# Steps: 
# 1. Install the latest version of Python (https://www.python.org/downloads/) - option for free 30 day trial for professional version.
# but I'll downloasd the free-to-use, open-source community version.

# benefits of PyCharm:

# feature of spell check for non-code language as well (ie Human languages) - alerted by a squiggle underline and a message when hovered-over text.
# more space to develop: 
            # you can split the screen. right click on file name and select Split and Move Right
            # this way you can easily refer to code held within another file when you are importing and calling the code in a new file.

# Built-In Linter:
# it picks out pieces of the code that might not be in accordance with the general conventions or coding style that is being followed
# think: am I indenting with multiple spaces or using the tab key?
#        maximum line length
#        blank lines between code blocks
#        etc.

# PEP8 is a very popular style-guide for coding in Python, which I will be following.
# https://peps.python.org/pep-0008/
# for example, following PEP8, and indentation should be equal to 4 spaces, with preference of spaces over tabs and maximum line length is 79 characters, 2 blank lines before and after functions.
# PyCharm automatically applies these rules and guidances to the code being entered to suggest changes.
# that being said, the code will still run as expected if you don't apply the suggested changes to the code, as long as it's valid.

# you can also see you edit history with a time stamp for the last 12 hours, you can copy and paste from that saved code or just revert everything back to that previous saved version.

# you can also view the structure of the code. The structure pain then shows you the names of all the variables and functions that you created in the code.

# Refactor Rename:
# this is SUPER useful to automatically rename a function or variable in all instances where it current name is being referrenced instead of manually searching the code.
#       1. Right click on name of function or variable.
#       2. Go to hover over refactor and select Rename on the list of options that pop up on the right-hand side.
#       3. Then it tells you how many usages this name has and tell you the lines of code where it is currently present.
#       4. Finally, select "Do Refactor" to enact changes across all of these instances.
#       5. This is much safer then just doing a find-and-replace method, which would reveal places where terms are used in print statements, which you might not want to change.

#-------------------------------------------------------------------------------------------------------------------------------------

# Virtual Coffee Machine Project Code that take coin payments to create coffee:
# it makes 3 hot flavors - being espresso, latte, and cappuccino.
# 1. Espresso - 50ml Water & 18g Coffee - Price = $1.50.
# 2. Latte - 200ml Water & 24g Coffee & 150ml Milk - Price = $2.50.
# 3. Cappuccino - 250ml Water & 24g Coffee & 100ml Milk - Price = $3.00.

# all of this information will be included in a dicitonary 

# additionally the latte machine has materials it needs to manage:
# 300ml water, 200ml Milk, 100g Coffee.
# Using US currency for coin values: Penny 1 cent, Nickel 5 cents, Dime 10 cents, Quarter 25 cents, 50-cent coins = 50 cents, dollar coins = 1 dollar.
# these values will be represented in decimal values like so: 0.01, 0.05, 0.1, 0.25, 0.5, 1.0.

# Program Requirements:
#           1. Print Report - as in type "Report" as input and it will reveal all the available resources in the machine.
#           2. Check that the resources are sufficient when the user orders a drink, by checking against the recipe for the requested drinks if atleast one resource is insufficient.
#           3. The user is prompted to enter the quantity of the currency they want to enter into the machine in descending order from dollar coint to pennies.
#           4. If not enough, money is refunded. If you pay over the cost you get the drink and the change back.

# Succinct Virtual Coffee Machine Program Requirements:
# 1. Prompt user about which coffee they would like.
# 2. Turn off the Coffee Machine with "off" prompt.
# 3. Print Report if user enters "report" to reveal available resources.
# 4. Check whether resources are enough to complete user's order.
# 5. Check whether user enters enough money by quantity of each coins to add up to product price.
# 6. Make the Coffee and return change for successful transactions.
# 7. If not enough resources return money and ask for different product selection.
# 8. If not enough money from user, alert them and they can abort purchase to have change returned.


# this is the dictionary that contains all the requirements to make and purchase each beverage.
# each list of ingredients has three inputs (keys) for water, coffee, and sometimes milk.
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# By default, the coffee machine has these measurements for each resource which will be exhausted after each purchase.

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# also, running profit needs to be set to 0 initially:

profit = 0

def is_resource_sufficient(order_recipe):
    """This returns True when order can be fulfilled or False if remaining input quantities are insufficient."""
    for ingredients in order_recipe:
        if order_recipe[ingredients] > resources[ingredients]:
            print(f"Sorry there is not enough {input}.")
            return False
    return True

# calculate_transaction() calculates the sums of each coins values, multiplied by the specified quantity.
def calculate_transaction():
    """Returns the total sum value of quantities of each coin entered by user."""
    print("Please enter your coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

# is_transaction_successful() check to see whether user payment is enough to actually proceed to the next step.
def is_transaction_successful(total_payment, drink_price):
    """Returns True when the payment is enough, or False if money is insufficient."""
    if total_payment >= drink_price:
        change = round(total_payment - drink_price, 2)
        print(f"Your total change is ${change}.")
        global profit
        profit += drink_price
        return True
    else:
        print("Insufficient payment received. Here is your money back.")
        return False

# If user payment was enough, the program then ensures that the machine has enough remaining resource to make the drink.
def make_coffee(drink_name, order_recipe):
    """Deducts the quantity of required ingredients from the machine's available resources."""
    for ingredients in order_recipe:
        resources[ingredients] -= order_recipe[ingredients]
    print(f"Please take your {drink_name} ☕️. Enjoy!")

# the is_on condition is set to true by default, but changes to false is user enters "off".
is_on = True


# this while loop runs as long as the machine is on, in case a user wants multiple drinks. 
# is also checks for spelling and alerts the user of these mistakes with the chance to re-enter their order.

while is_on:
    choice = input("Would you like an espresso, latte, or cappuccino: ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif choice not in ["espresso", "latte", "cappuccino"]:
        print("Invalid coffee name, please check spelling and enter again.")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = calculate_transaction()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])










