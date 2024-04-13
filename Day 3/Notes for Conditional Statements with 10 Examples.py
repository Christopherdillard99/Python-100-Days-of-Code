# Conditional statments in Python.
# Day 3 Porject "Treasure Island: Choose your destiny" is number 10 at the bottom of this page

# 1. Creating a program that checks whether a number is even or odd based on its divisibility by 2.

number = int(input())

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")


# Modulo (%) is used to determine whether a number is even where any even number divisible by two would leave a remainder of zero.
# Ex: 5 % 2  is 2 x 2 + 1 = 5. So, 5 % 2 = 1. Similarly 14 % 4 is 4 x 3 + 2 and 14 % 4 = 2.
# Logically, any number % 2 should == 0 to be even, otherwise it is odd. 

# 2. Nested if / else statement for ticketing price based on age where riders are atleast 120 cm tall.

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age?\n"))
  if age <= 18:
    print("Please pay $7.")
  else:
    print("Please pay $12.")
else:
  print("Sorry you have to grow taller before you can ride.")

# 3. Revised ticket pricing with multiple conditions.

# Now, let's say there are 3 cost tiers based on whetehr a rider is below 12 yrs old, 12-18, and above 18. 
# Here, we use an If / Elif / Else structure to check multiple conditions. "Elif" is lke Else-if.
# An elif checks if the previous condition was not met and apply another condition ontop. 
# in this example you can continue adding elif statements for as many different age groups as you wish, nested with the first if statement that checked for heigh.

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age?\n"))
  if age <12:
    print("Please pay $5.")
  elif age <= 18:
    print("Please pay $7.")
  else:
    print("Please pay $12.")
else:
  print("Sorry you have to grow taller before you can ride.")

# 4. Program that calculates and interprets BMI, being Weight (kg) / height**2 (m^2).
# The inpretation wil tell the user whether their BMI falls into Underweight, Ideal Weight, Over Weight, Obese, and Clinically Obese.

height = float(input())
weight = int(input())

# Note how weight is an integer, NOT a float.


bmi = weight / height**2

if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")

# Each subsequent elif statement checks if the value is not met by the previous condition and therefore falls within a new range. 

# 5. Prgoram that checks whether a given year is a leap year (i.e. the year has 366 days instead of standard 365 days.)
# This has 3 conditions needing to be met for leap years:
#       1. Any year that is divisible by 4 with no remainder.
#       2. EXCEPT every year that is evenly divisible by 100 with no remainder.
#       3. UNLESS the year is also divisible by 400 with no remainder.
#e.g. for 2000. 
#       2000 / 4 = 500 (Leap)
#       2000 / 100 = 20 (Not Leap)
#       2000 / 400 = 5 (Leap Year!)
# So, 2000 was a leap year, but 2100 will not be one b/c 2000 / 4 = 525 (leap), 2100 / 100 = 21 (not leap), & 2100 / 400 = 5.25 (not leap).

year = int(input())

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")

# 6. Now, along with the previous ticket price conditions, we need to add a surcharge for whether they want a $3 photo ontop of the price.
# This requires multiple if statements, so:
#       1. Rider must be over 120 cm to ride.
#       2. Price based on age group.
#       3. Do they want photos for additional $3?
# New input for photos need to be in the same indentation as but outside of the if, elif, and else block to ask whether they wants photos taken.
# Their response is saved into a new variable called wants_photo
# The new nested if statement needs to align with the if/elif/else statements for where a rider is tall enough.
# A "bill" variable needed to be created and initially set to zero so that the total amount is result of adding price based on age and whether rider wants photo.
# For the total price with the last photo statement you set bill equal to current bill + 3 if they want photo.
#   i.e. if wants_photo == "Yes":
#           bill = bill +3
# HOWEVER, there is a simpler syntax for this, written as bill += 3
# In this case, there is no need for an else statement for if they dont want photos (since the bill remains unchanged) so the next line will print their total bill.

print("Welcome to the rollercoaster!\n")
height = int(input("What is your height in cm?\n"))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age?\n"))
  if age <12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  else:
    bill = 12
    print("Adult tickets are $12.")

  wants_photo = input("Do you want a photo taken? Yes or No.")
  if wants_photo == "Yes":
    bill += 3

  print(f"Your final bill is ${bill}")
  
else:
  print("Sorry you have to grow taller before you can ride.")

# 7. Automatic Pizza Order  Program to calculate final bill based on user's order
# size for S, M, L. add_pepperoni Y or N, extra_cheese  Y or N
# Note here that the Thank you line is added to in front of all the code as a default message while the final bill is what changes based on multiple conditions.

# Conditions:
#       1. Small pizza (S): $15
#       2. Medium pizza (M): $20
#       3. Large pizza (L): $25
#       4. Add pepperoni for small pizza (Y or N): +$2
#       5. Add pepperoni for medium or large pizza (Y or N): +$3
#       6. Add extra cheese for any size pizza (Y or N): +$1

price = 0
if size == "S":
  price += 15
elif size == "M": 
  price += 20
else:
  price += 25

if add_pepperoni == "Y":
  if size == "S":
    price += 2
  else:
    price += 3

if extra_cheese == "Y":
  price += 1

print(f"Your final bill is: ${price}.")

# Logical Operators: 
#       Think A and B both has to be True for entire line of code to be True
#       C or D: if only one of the conditions need to be met to be True
#       not E: if true it becomes False, if false it would return True.

# 8. Add condition that people having Mid-life crisis 45-55 yrs old get to ride for free.
# To do so, we add another elif statement with the and logical operation for the range >= 45 and <= 55.
# there is no need to add any else statement since the default bill is already set to 0. They still have to pay $3 for photos.

print("Welcome to the rollercoaster!\n")
height = int(input("What is your height in cm?\n"))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age?\n"))
  if age <12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  elif age >= 45 and age <= 55:
    print("Everything is going to be okay. Have a free ride on us!")
  else:
    bill = 12
    print("Adult tickets are $12.")

  wants_photo = input("Do you want a photo taken? Yes or No.\n")
  if wants_photo == "Yes":
    bill += 3

  print(f"Your final bill is ${bill}")
  
else:
  print("Sorry you have to grow taller before you can ride.")

# 9. Love Calculator to calculate compatibility (love score) between two people.
# Take name and see how many time the letters of words True and Love occur in their names.
# The total scores are than assigned to ranges so that the user gets a personalized message of their compatibility.

# i.e. for random names Logan Scott and Ryley Porter

# T occurs 2 times
# R occurs 3 times
# U occurs 0 times
# E occurs 2 times
# Total = 7
# L occurs 2 times
# O occurs 3 times
# V occurs 0 times
# E occurs 2 times
# Total = 7

#Love Score = 77 (Combine to make two digit number)
# Print: "Your score is 77."

# Logic behind this:
#       1. Combine names into single string so you only check once.
#       2. Now, we need the casing to match so .lower() function is added to put all letters in lower case.
#       3. first_digit is for total of letter occurrences for t, r, u, and e.
#       4. second_digit is for the total of letter occurrences for l, o, v, and e.
#       5. Since we are combining the digits (not adding), we convert them to string with str() for the score variable.
#       6. This combined two digit number score is then converted into an integer.
#       7. Finally, an if, elif, else statement is created to check for the conditions for personalized messages for the user based on their score.

print("The Love Calculator is calculating your score...")
name1 = input() # What is the first name?
name2 = input() # What is the second name?

combined_names = name1 + name2
lower_names = combined_names.lower()

t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))
if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")

# 10. Choose your own destiny on Treasure Island adventure project:
# There is a series of three choices.
# Ascii art is used to display a treasure chest
# find more shapes at https://ascii.co.uk/art and wrap the art in ''' triple single quotes so is prints the entire block of symbols.

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
# \ before the ' in You're tells the computer that is it a apostrophe and not ending the string.
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You've made it unscathed to the island and find a house with three doors. One red, one yellow, and one blue. Which color do you choose? \n").lower()
    if choice3 == "red":
      print("THE ROOM IS FULL OF FIRE! Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! Congratulations, you won!")
    elif choice3 == "blue":
      print("The room is full of beasts. Game Over.")
    else:
      print("This door does not exist. Game Over.")
  else:
    print("You were attacked by a vicious trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")




