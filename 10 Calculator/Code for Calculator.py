# Calculator Project:

# I created a calculator with the following design and experience:
#       1. text-based, user enters a number, then is prompted to selected their desired operation
#       2. then, they choose the next number and are given the result of the operation.
#       3. lastly, they are prompted to type y to continue calculation with previous result or type n to start new calculation
#       4. there is of course ASCII art to make the program more attractive.

# this calculator will have various functions:
# the add, subtract, multiple, and divide functions:
# a while loop is used to continuously add operations and new numbers at the user's command.

# The calculator function will be called again using recursion if the user is done with their calculations (ie types 'n'), which will trigger the console to clear and redisplay the ASCII art logo.

# create new file for the logo art called art.py
# now save ASCII art to desired name like "logo"

   logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


from art import logo

def add(n1, n2):
   return n1 + n2
def subtract(n1, n2):
   return n1 - n2
def multiply(n1, n2):
   return n1 * n2
def divide(n1, n2):
   return n1 / n2

operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide,
              }

def caluclator():
   print(logo)

   num1 = float(input("What's the first number?: "))

   should_continue = True

   while should_continue == True:
      operation_symbol = input("Pick an operation from the line above: ")
      num2 = float(input("What's the second number?: "))
      calculation_function = operations[operation_symbol]
      answer = calculation_function(num1, num2)

   print(f"{num1} {operation} {num2} = {answer}")

   if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ") == "y":
      num1 = answer
   else:
      should_continue = False
      calculator()