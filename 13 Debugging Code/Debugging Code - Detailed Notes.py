# Day 13: Debugging - How to Find and Fix Errors in your Code:

# Debugging:
# Grace Hopper found one of the first to find "bugs":
# found a moth in a relay that was preventing her program from running.


# Tips to quickly identify bug:

            # 1. Describe the problem - untangle it in your head.
            # 2. Reproduce the Bug.
            # 3. Play Computer.
            # 4. Fix the Errors (pretty obvious).
            # 5. Print is your friend.
            # 6. Simply use a debugger.
            # 7. Take a break.
            # 8. Ask a Friend/ other developer.
            # 9. Run the code often.
            # 10. Ask question on stack overflow. - when all other resources are exhausted.

# ------------------------------------------------------------------------------------------------------------------------------

# Ex: fix this code so that it actually prints "You got it" in the console.
# what is the for loop doing? What assumptions are made about i and when is the function supposed to print the message?

# the for loop checks whether the i in range of (1,20) is actually equal to 20.
# the range function does not contain the upper limit, it omits 20 from the actually range to check.
# ie the range is non-inclusive of the upper bound.

def my_function():
  for i in range(1, 20):
    if i == 20:
      print("You got it")
my_function()

# this code is fixed this way:

def my_function():
  for i in range(1, 21):
    if i == 20:
      print("You got it")
my_function()

# ------------------------------------------------------------------------------------------------------------------------------

# Reproducing a bug that you encountered.
# this code below, prints a number sometimes, but others it produces an index error.
# now, i want to modify the code to understand this error by making it always produce this error.


from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])

# fixed this code so that the randint is from (0,5). That way it prints the values that correspond with the actual number in the list.
# in a list, 0 is the first number, so that's why this works and the randint needed to be fixed accordingly.

from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

# ------------------------------------------------------------------------------------------------------------------------------

# Play Computer: Imagine what your going to do with each line of code:
# the problem is if you input 1994, absolutely nothing happens.


year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")

# this is a very simple fix. the comparison operator needs to be >= 1994.
# this way, those born in 1994 are classified as millenials and the print statement reflects that.

year = int(input("What's your year of birth?"))
if year > 1980 and year <= 1994:
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")

# ------------------------------------------------------------------------------------------------------------------------------

# Fix the errors:
# this code produces the following error message with the carrot under the p in print:
# File "main.py", line 26
#     print("You can drive at age {age}.")
# this is called an IndentationError.

# So, we know that we just need to indent the print statement since it follow a colon within an if statement.


age = input("How old are you?")
if age > 18:
    print("You can drive at age {age}.")

# Once that problem is fixed, we notice that the comparison operators are not supported between instances of str and the input.
# the input must be converted to an integer.
# this is called a TypeError

age = int(input("How old are you?"))
if age > 18:
    print("You can drive at age {age}.")

# now the issue is that the print statement does not return the age over 18, but rather "You can drive at age {age}."
# this print statement needs to be converted into an f string.

age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")

# Now, what is someone is exactly 18 or under 18?
# I want someone exactly 18 to print that they can in fact drive, and those under to print that these users cannot drive.
# I simply use the >= 18 comparison operator for the first if statement for those that can drive.
# all other ages are handled with an else: statement and a print statement of print(f"You cannot drive at age {age}")
# I also added a colon and a space to the "How old are you?" input question so it looks better in the console.

age = int(input("How old are you?: "))
if age >= 18:
  print(f"You can drive at age {age}.")
else:
  print(f"You cannot drive at age {age}")

# ------------------------------------------------------------------------------------------------------------------------------

# Print is your friend:
# since it can easily reveal the value of a variable or the output of a function.

pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

# when I run this code, it prompts me to input the Number of pages: and the Number of words per page: 
# I entered 10 pages and 100 words per page. The print statement printed zero though after this instead of 1000 total_words

# my logic debugging this is that the double equal sign is throwing off the code.
# the input for words_per_page needs to be assigned to the value, not compared.
# the first two instances of pages = 0 and word_per_page are superfluous as well in my opinion.

# ------------------------------------------------------------------------------------------------------------------------------

# Use a debugger:
# pythontutor.com and thonny python editor are great debugger tools.
# this function should mutate a list so that it takes the list as an input then multiplies each one of the items in the list by 2.
# this way the final output should be [2,4,6,10,16,26]

# follow this link for python tutor debugger tool: https://pythontutor.com/visualize.html#mode=edit

def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])

# in python tutor, you can paste the code ansd then click non visualize execution to get step-by-step instructions on what each code line does.

# so, first the list [1,2,3,5,8,13] which is our argument for the function is passed through the mutate function for the a_list parameter.
# now, b_list is created as an empty list.
# for item in a_list: the code will loop through each item in the a_list and save result of multiplying this item by 2 into a new variable called new_item.
# the issue though is that each result is replacing the first result in the list, so that the output only reveals 26 (13 * 2), thus leaving us with one item in b_list.

# this is fixed by indenting the b_list.append(new_item) line.
# so that running this code prints b_list into the console as [2,4,6,10,16,26]

# ------------------------------------------------------------------------------------------------------------------------------

# Debugging previous code in the course with some forced changes:

# 1. Debugging Odd or Even Excercise:
# remember even is anynumber divisible by two with no remainder, ie num % 2 == 0
# % is called a modulo.

number = int(input()) # Which number do you want to check?

if number % 2 = 0:
  print("This is an even number.")
else:
  print("This is an odd number.")

# clearly the if statement needs to be == not = since this is checking for a condition, not assigning a value.


number = int(input()) # Which number do you want to check?

if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")

# -------------------------------------------------

# 2. Debugging the Leap Year Problem:
# number year is divisible by 4 AND 400 with no remainder is a leap year.
# the logic is also that if year is divisible by 4 AND 100 w/o remainder then it is NOT a leap year.

# Which year do you want to check?
year = input()

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")

# the issue here is that the input (year) is not converted to an integer like so:

# Which year do you want to check?
year = int(input())

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")


# other examples of this code:

def is_leap_year(year):
    """Determine whether a year is a leap year."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# -------------------------------------------------

# 3, Debugging the FizzBuzz problem:
# remember: 
# The code needs to print the solution to the FizzBuzz game.
# Your program should print each number from 1 to x where x is the input number.
# However when the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz".

# buggy code:

target = int(input())
for number in range(1, target + 1):
  if number % 3 == 0 or number % 5 == 0:
    print("FizzBuzz")
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print([number])

# fixed version:
# corrected by removing the square brackets in the print statement string so that the output does not place numbers in square brackets.
# alternatively an f string could have been used here in the print statement.
# I made sure that checking for clean divisibility by 15 came first in the if, elif, else statements.
# this first condition could also be written as if number % 3 == 0 and number % 5 == 0: 
# this way, 15 was correctly printing FizzBuzz instead of either Fizz or Buzz depending on whether the % 5 or % 3 statements preceeded it.

target = int(input())
for number in range(1, target + 1):
  if number % 15 == 0:
    print("FizzBuzz")
  elif number % 5 == 0:
    print("Buzz")
  elif number % 3 == 0:
    print("Fizz")
  else:
    print(number)


