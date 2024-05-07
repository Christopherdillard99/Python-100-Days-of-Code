# Day 10: Functions with Outputs:

# Creating a Calculator with the following design and experience:
# text-based, user enters a number, then is prompted to selected their desired operation
# then, they choose the next number and are given the result of the operation.
#  lastly, they are prompted to type y to continue calculation with previous result or type n to start new calculation
# there is of course ASCII art to make the program more attractive.

# Simple functions:

def my_function():
    #do this
    #then do this
    #finally do this

# ^ specify within body of function what tasks you want to be execute when calling or triggering the function.

# Functions with Inputs:

def my_function(something):
    # do this with something
    # then do this
    # finally do this

# here something is the parameter 

my_function(123)

# 123 is the argument now that gets passed through the parameter called something and is used within the body of the function

# functions with inputs allow us to modify the code within the function and get it to do something different each time. 


# Functions with Outputs:

def my_function():
    result = 3 * 2
    return result

# alternatively, and more typically

def my_function():
    return 3*2

#  whenever this function is called, it will display 6, since the result of the operation is equal to six.
# return triggers the function only display this variable, here "result", when the function is called.

# Functions with outputs are like machines that take inputs and produces something else, in the middle there are processes that create changes using the inputs.

# -----------------------------------------------------------------------------


# ex of functions with outputs:
# this function will take the parameters being the first name and last name to produce an output where the first letter of both names are capitalized.

def format_name(f_name, l_name):
   formatted_f_name = f_name.title()
   formatted_l_name = l_name.title()
   print(f"{formatted_f_name} {formatted_l_name}")
  
format_name("ChRis", "DillArd")

# this will return Chris Dillard with the right casing and a space between them using the title function

# alternatively I can format the function to not use print() but instead return within the body of the function with output, 
# next I just put a print statement in front of my text that calls the function with the arguments ChRis and DillArd for the parameters f_name and l_name.

def format_name(f_name, l_name):
  formatted_f_name = f_name.title()
  formatted_l_name = l_name.title()
  return f"{formatted_f_name} {formatted_l_name}"
  
print(format_name("ChRis", "DillArd"))

# -----------------------------------------------------------------------------

# Multiple Return Values:
# in this new code, there are user input for the first and last name.
# if inputs are left blank, the the function check this condition first and will return the "You didn't provide valid outputs." to the user.
# leaving a single return with nothing after it, "return  " after the if statement will yield a message of "none".

def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "You didn't provide valid outputs."
  formatted_f_name = f_name.title()
  formatted_l_name = l_name.title()
  return f"{formatted_f_name} {formatted_l_name}"
  
print(format_name(input("What is your first name?"), input("What is your last name?"))) 

# -----------------------------------------------------------------------------

# creating a program to return how many days there are in a month within any given month, taking in consideration leap years.
# first line inputs the year, second inputs the month in numerical form (1-12)
# take into account the function is_leap(year) created in previous exercise to use within this execises function:
# the print statements in the original is_leap function, were replaced with boolean for True or False so that the days_in_month ONLY displays the days in month, without the extra "Leap Year" or "Not Leap Year" text.

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

# TODO: Add more code here 👇

def days_in_month(year,month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  if month == 2 and is_leap(year):
    return 29
  else:
    return month_days[month - 1]

  
#🚨 Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)

# -----------------------------------------------------------------------------

# Docstrings:
# they must come after the first declaration line when writing a function.
# syntax is ''' three quotation marks, in between these marks you write your documentation in multiple lines with the enter key, so that user can see what the function does.

def format_name(f_name, l_name):
  '''Takes the first name and last name, formatting these to return
the title case version of the full name'''
  if f_name == "" or l_name == "":
    return "You didn't provide valid outputs."
  formatted_f_name = f_name.title()
  formatted_l_name = l_name.title()
  return f"{formatted_f_name} {formatted_l_name}"
  
print(format_name(input("What is your first name?"), input("What is your last name?"))) 

# now, when a user writes out the function to call it, a text box populates the screen to alert the user of the functions purpose that was written within the Docstrings.


# -----------------------------------------------------------------------------

# Ex 1:
# What does this code produce?:

def add(n1, n2):
  return n1 + n2
 
def subtract(n1, n2):
  return n1 - n2
 
def multiply(n1, n2):
  return n1 * n2
 
def divide(n1, n2):
  return n1 / n2
 
print(add(2, multiply(5, divide(8, 4))))

# answer is 12

# Ex 2:
# What is the result of running this code?:

def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)

# this returns 15
# explanation: a = 5, which means c = 5. b = 10, which means d = 10. The output of inner_function becomes the output of outer_function.

# Ex 3:
# What is printed in console after running the following code?:

def my_function(a):
    if a < 40:
        return
        print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"
print(my_function(25))

# this will return "none"
# The return keyword will exit the function and prevent the rest of the code from being executed.
# this is because the return under the first if statement has no text string after it on the same line.

# -----------------------------------------------------------------------------

# Calculator Project:

# Creating a Calculator with the following design and experience:
# text-based, user enters a number, then is prompted to selected their desired operation
# then, they choose the next number and are given the result of the operation.
#  lastly, they are prompted to type y to continue calculation with previous result or type n to start new calculation
# there is of course ASCII art to make the program more attractive.

# this calculator will have various functions:
# the add, subtract, multiple, and divide functions:

def add(n1, n2):
   return n1 + n2

def subtract(n1, n2):
   return n1 - n2

def mutiply(n1, n2):
   return n1 * n2

def divide(n1, n2):
   return n1 / n2

# store these functions within a dictionary so that the keys are each of the symbols used in the previous functions, and the values are  just the names of the functions.

operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide,
              }

# creates variables for number 1 and number 2

num1 = int(input("What's the first number?: "))

for symbol in operations:
   print(symbol)

# now the user will see a list of all the operation symbols, beinng: + - * / 

operation_symbol = input("Pick an operation from the line above: ")

# now the user selects the second number to complete the operation.

num2 = int(input("What's the second number?: "))

calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)


print(f"{num1} {operation} {num2} = {answer}")


# difference between printing to console and returning something as an output from a function.

# ----------------------------------------------------------------------------- 
# version 2:

# the user pick another operation and number, using a previously calculated answer, to pass the first "answer" back into the calculation function with the new operation and number.

def add(n1, n2):
   return n1 + n2
def subtract(n1, n2):
   return n1 - n2
def mutiply(n1, n2):
   return n1 * n2
def divide(n1, n2):
   return n1 / n2

operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide,
              }

num1 = int(input("What's the first number?: "))

for symbol in operations:
   print(symbol)

operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number?: "))
calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1, num2)

print(f"{num1} {operation} {num2} = {answer}")

operation_symbol = input("Pick another operation: ")
num3 = int(input("What's the next number?: "))
calculation_function = operations[operation_symbol]
second_answer = calculation_function(calculation_function(num1, num2), num3)

print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")

# -----------------------------------------------------------------------------
# introducing a while loop into the code, flags, recursion, and general debugging:
# this allows users to use a while loop to complete as any operations as they desire:
# must create should_continue variable default set to true to continue the loop until the user doesn't want to continue with new operation.


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

# recursion is a function that calls itself, like the function calculator(): for the entire process. 
# in this case, a user entering y makes sure that the code reruns the calculator function to call it once more.
# there needs to be some kind of condition that ensures that the function doesnt recall itself in an infinite loop.

# bug was fixed so that calculator can handle floats (non-integer number, that have decimal places).
# this was fixed by replacing "int" in num1 = int(input("What's the first number?: ")) with "float", along with the line for num2.

# square root and exponent capabilities can be added to the program as well for more functionality.


   