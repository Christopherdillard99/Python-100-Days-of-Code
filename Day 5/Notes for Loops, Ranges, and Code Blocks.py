# Day 5 Notes: For Loops, Ranges, & Code Blocks:

# For Loops:

for item in list_of_items:
    # Do something to each item 

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  print(fruit)

# ^ This is essentially assigning each item in the fruits list to a variable named fruit.
# a loop allows us to execute the same line of code multiple times. In the loop, the code repeat the previous command for each item of the list in order until all items are accounted for.

# Now to modify the code an add more commands in the loop, like the print out the name of the fruit with " pie":
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  print(fruit)
  print(fruit + " Pie")
# ^ This will print out apple, apple pie, banana, banana pie, cherry, cherry pie.

# Indention is very important here, since the loop only repeat actions for line indented to the right of for.
# In the example below, the same loop is ran as before, but now a list of the fruits in order is printed at the end after the loop is finished:

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  print(fruit)
  print(fruit + " Pie")
print(fruits)

# ----------------------------------------------------------------------------------------------------------------------------------------------------

# 1. Program that calculates the total height, number of studetns, and average height for a list of students using for loop without using simpler sum() or len() functions:

student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# Must create variable for total height set to default zero and then add them inputs from the newly created loop (for height in student_heights):

total_height = 0
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")

# repeat this process for the next measure for the sum of students:

number_of_students = 0
for student in student_heights:
  number_of_students += 1 # the code adds 1 to the default 0 for each student in the list
print(f"number of students = {number_of_students}")

# Now, use the values that were just caluclated to find the average of the division of total_height / number_of_students

average_height = round(total_height / number_of_students)
print(f"average height = {average_height}")

# ----------------------------------------------------------------------------------------------------------------------------------------------------

# 2. Program that returns the highest number from a list of student scores, replicating the max() function using a for loop:

student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# create new highest_score variable set to 0:

highest_score = 0

# we need a condtion to check if the next score in the loop is higher than the first/previous score in the each iteration, then that value will replace the previous one, otherwise it stays the same.

for score in student_scores:
  if score > highest_score:
    highest_score = score
print(f"The hightest score in the class is: {highest_score}")

# ----------------------------------------------------------------------------------------------------------------------------------------------------

# Use loop completely independent of a loop:
#       Think adding all the numbers from 1 to 100 ( 1 + 2 + 3 + ... + 100)
#       German mathematician Johann Carl Friedrich Gauss - Gauss Summation:
#       100 + 1 = 101, so does 99 + 2, all the way until 1 + 100. So, there are 50 pairs that equal 101. 50 x 101 = 5050.

# ^ This can be done simply by using for loops with the range() function.
# so, instead of looping in a list, we define a range to do something to each number in that range:

for number in range(a, b):
  print(number)

# Ex: 
for number in range(1, 10):
  print(number)

# ^ by default the range function does not include the last digit in the range. with the print() function range function automatically steps by 1 to show all numbers in the range.
# if you wanted to only show every 3rd number, you need to add another element to the range function at the end, separated by a comma:

for number in range(1, 11, 3):
  print(number)

# ^ this would print 1, 4, 7, 10

# Now, let's try Gauss' problem to sum all the numbers from 1 to 100. 
# we need to define the range as range(1, 101) so that the range stops at 100.

total = 0
for number in range(1, 101):
  total += number

print(total)

# ----------------------------------------------------------------------------------------------------------------------------------------------------

# 3. Program that calculates the sum of all even numbers in a range using a for loop
# There are two methods here:
#           Method 1:

target = int(input())

even_sum = 0
for number in range(2,target + 1,2): # target + 1 because if your target (input value for end value of range) is 100 then the range() only spans from 2 to one number below the input value by default.
  even_sum += number
print(even_sum)

#           Method 2: Using a modulo operator (checking if number is divisible by two with a remainder of 0 to be even):
# This method makes if so the range function doesn't need to be stepped by 2, ie only counting every second number in the specified range not including the end number.
alternative_sum = 0
for number in range(1, target + 1):
  if number % 2 == 0:
    alternative_sum += number
print(alternative_sum)

# ----------------------------------------------------------------------------------------------------------------------------------------------------

# 4. Program to recreate the FizzBuzz game **on interviews a lot**:
# Ex: you have 5 friends and each friends pulls out the next number starting at 1.
# The game stops when you pull out a number that is divisible by three, so nstead you say Fizz.
# if the pulled number is divisible by 5 you say Buzz. 
# if the number is divisible by 15 you say FizzBuzz.

# This program will print out the response based on each number's divisibility by either 3, 5, or 15, if applicable.
# The range is 1 to 100 including 100. Each line of text should be printed on a separate line (keep this statement within the loop?):
# Basically, output is numbers 1 to 100 in their own line, but the number in each line would be replaced by either Fizz, Buzz, or FizzBuzz, if applicable, otherwise is just outputs the number.

number = 0

for number in range(1,101):
  if number % 15 == 0:
    print("FizzBuzz")
  elif number % 5 == 0:
    print("Buzz")
  elif number % 3 == 0:
    print("Fizz")
  else:
    print(number)

# Class example code:

target = 100
for number in range(1, target + 1):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)

# ----------------------------------------------------------------------------------------------------------------------------------------------------

# 5. Project: Password Generator:
# Two different approaches for different levels of difficulty 

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = "" # Start password out as empty string

# for character in range(1, nr_letters + 1):
#   random_char = random.choice(letters)
#   password += random_char # string concatenation of password = password + random_char
# ^ simplify this code like so:

for char in range(1, nr_letters + 1):
  password += random.choice(letters)

for char in range(1, nr_symbols + 1):
  password += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password += random.choice(numbers)

print(f"Your password is: {password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# I need the password to contain all the characters in a random order so that it doesn't start with specified numbers for letters, symbols, and numbers, can be a random combination of all three types with the specified user input.

# Instead of adding the loops in an empty string at the start, I need to code it so that the loops add the characters to a list.
# use .append to add the random character to the end of the password at each iteration of the loop. 

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = [] # Start password out as an empty list.

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list.append(random.choice(symbols))

for char in range(1, nr_numbers + 1):
  password_list.append(random.choice(numbers))

# Now that there's a list, we need to shuffle the order of the items in the list. 
# shuffle function in random module is much easier than using another for loop.

random.shuffle(password_list)

# Now we need to turn this back into a string so that it prints out as a usable password:

password = "" #creating a new variable that is an empty string so that the random items from the list are added after each iteration of the loop. 
for char in password_list:
  password += char
print(f"Your password is: {password}")


  


  



