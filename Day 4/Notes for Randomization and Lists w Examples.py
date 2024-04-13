

# Random module is used in Python
# To import this module use:
#       import random
# Now call some of its functions using this code depending on the type of randomness:
#       random.randint(startnumber,endnumber)   This is an inclusive range spanning the starting number and ending, ex. 0-5, only integers
#       random.float()                          This is a non-inclusive range between 0 and 1.
#       random.float() * 5                      By multiplying this random float by 5 we not have random floats between 0 and 5. Can substitute with any number for different range.
# Ex:   random_num = random.randint(1,10)
# ---------------------------------------------------------------------------------------------------------------

#1. Simple Heads or Tails Program:

import random

result = random.randint(0,1)
if result == 1:
  print("Heads")
else:
  print("Tails")

# Lists:
# Ex: fruits = [item1, item2, ..., itemN]  lists are enclosed in square brackets in Python.

# ---------------------------------------------------------------------------------------------------------------

# 2. Now take this list of all US states in order of when they joined the union, where the order is important:
States_US = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# To identify the first state that joined the union I can use the code below:

print(States_US[0])

# To count from the END  of the list to the front use the negative sign:
# Ex:    
   
print(States_US[-1])
# ^ This yields Hawaii as opposed to one over from the end, since -0 is non-existent in math.

# Manipulating item names in a list:
# Ex: Changing spelling of state name like so:
States_US[1] = "Pencilvania"

# Adding single item to end of the list, like a new state:

States_US.append("Chrisland")

# Extending the list by several items at the end:

States_US.extend(["Washington, D.C", "Puerto Rico"])

# Insert item at specified location in list:

States_US.insert(0,"Newland")

# Remove item in list that's equal to specific value:

States_US.remove("Texas")
# ^ This returns ValueError if no such value exists in the list.

# ---------------------------------------------------------------------------------------------------------------

# 3. Banker Roulette: Who's paying for dinner tonight?
# Given a list of names, separated by a comma and space.
names = names_string.split(", ")

# Need to calculate number of items in the list of names using the len() function and storing result in new variable:
num_items = len(names)

import random
random_choice = random.randint(0, num_items - 1)
# the total is subtracted by 1 since lists start at 0 in python. ie you have 5 names in total, but 0 corresponds to the 1st name in the list OR [0,1,2,3,4]. The len or length function would be 5, thus we need random.randint(0, num_items -1)

# Now that the random number is selected, we need to identify who in the list correponds to that random number:
who_pays = names[random_choice]
# ^ this works because we are looking for the number position in the list of the names variable that matches the random number.

print(who_pays + " is going to buy the meal today!")

# ---------------------------------------------------------------------------------------------------------------

# Calculate length of list:
print(len(States_US))

num_states = len(States_US)

print(States_US[num_states -1])

# ^ This is important because the length of list is 50 states, but if you want to print the last you need to do the name -1, in case you don't know how many items are in the list.

# 12 fruits determined to be the worst for having pesticides:

dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# Now, separate fruits from veggies, while still keeping the relation? Create a nested list like so:

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)
# ^ This will show double square brackets to seperate the two categories.

# What would be printed out?
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])

# Answer: Kale, think order of operations from left to right, looking in nested list "1" ie the second list, then looking at the second item in that nested list (think 0, 1).
# In short, first Python identifies the nested list that is 1 over from 0 (ie vegetables), now it looks to the vegetable that is 1 over from the start of that list, being Kale.

# ---------------------------------------------------------------------------------------------------------------

# 4. Create a trasure map, creating a map in cordinates with numbers along one axis and letters along the other so that each tiles has an exact id (letter + number)
# The code will mark the map with an X where the treasure is buried given the users input.
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?

letter = position[0]
# ^ get letter from first index of the input ex B3, position 0 returns a B.
# now turn letter into lowercase incase the user used a capital so it is consistent, alternatively could make it .upper as long as everything is consistent.
letter = position[0].lower()

abc = ["a", "b", "c"]

letter_index = abc.index(letter) #index 1 = B in this case, .index() checks the value in the list.
number_index = int(position[1]) - 1 # number is -1 in this case.

# Now bring up map and insert the coordinates for letter and number:

map[number_index][letter_index] = "X" # Number comes first based on the map, since numbers go across in the list and each number contains the same letters, A, B, and C here. So we first search the number index, then the letter within that number.

print(f"{line1}\n{line2}\n{line3}")

# ---------------------------------------------------------------------------------------------------------------

# 5. Rock, Paper, Scissors Proram
# Rules: Rock + Rock , Paper + Paper , or Scissors + Scissors = rematch

# You win if you choose Rock vs Scissors or Paper vs Rock or Scissors vs Paper
# You lose if you choose Rock vs Paper or Scissors vs Rock or Paper vs Scissors

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
game_images = [rock, paper, scissors]

# ^ make a list for the images.

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[player_choice])

# print the corresponding image that matches the playes choice.

if player_choice >= 3 or player_choice < 0: 
  print("You typed an invalid number, you lose!") 
else:
  computer_choice = random.randint(0, 2)
  print("Computer chose:")
  print(game_images[computer_choice])

# ^ before anything else, the program can only work if the player enters a valid input (0-2 in this case).
  
# below are some conditional statements that lay out the game rules with the programmed response: 

if player_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and player_choice == 2:
  print("You lose")
elif computer_choice > player_choice:
  print("You lose")
elif player_choice > computer_choice:
  print("You win!")
elif computer_choice == player_choice:
  print("It's a draw")





