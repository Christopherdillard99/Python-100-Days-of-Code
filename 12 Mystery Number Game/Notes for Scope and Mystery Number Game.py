# Day 12: Scope and Number Guessing Game:
# terms: scope, local scope, global scope, local variable, global variable, namespace.
# there is no such thing as Block Scope in Python.

# ----------------------------------------------------------------------------------------------------------------------

# Scope: 

# Ex below: What is the output for the two print statements (ie how many enemies will each print?)

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# the print statement within the increase_enemies function will print 2, while the second print statement prints 1.

# ----------------------------------------------------------------------------------------------------------------------

# Local Scope: exists within functions:

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
print(potion_strength)

# you cannot call the potion_strength function outisde of the drink_potion() function. 
# potion_strength will be undefined in this case if called outside the function.
# potion_strength can be called a local variable.

# ----------------------------------------------------------------------------------------------------------------------

# Global Scope:

player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion() # this will print 10 in the console.

# now, player_health can be referenced within the drink_potion() because player_health has global scope.
# player_health is called a global variable in this case

# ----------------------------------------------------------------------------------------------------------------------

# Namespace - anything you give a name to is valid within certain scope. a variable's scope is called its namespace.

# ----------------------------------------------------------------------------------------------------------------------

# There is no such thing as Block Scope in Python:

# the a_variable is not limited to the if statement (ie it has global scope):

if 3 > 2:
    a_variable = 10

#ex: 

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy) # this will print Skeleton and is valid code

# but as soon as the if statement and new_enemy variable are embedded within a function, the print statement outside of the function errors out.

game_level = 3
def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]

print(new_enemy) # this print statement would need to indented once to the right to be valid.

# ----------------------------------------------------------------------------------------------------------------------

# if you create a variable within a function, the variable has local scope and is only available within that function.
# if you create a variable within an if statement, a for-loop, or a while-loop then the variable has global scope if the if statement.
# ^ that is, if the if-statement is not within a function.

# ----------------------------------------------------------------------------------------------------------------------

# Modifying Global Scope:
# usually a bad idea to call your local variabls and global vars the same name.

# ex: we need to reference the global variable "enemies" from within the increase_enemies() function.

enemies = 1

def increase_enemies():
    global enemies # must use global + var syntax to be able to locally modify a global variable.
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# often, people are advised to avoid user Global Scope though, because it can lead to bugs or be harder to track after days or hundreds of lines of code.

# take previous code and modify it too be susceptible to bugs:
# in this case, a return statement was places to simply add 1 to enemies.

enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies() #now I can just take a ahold of the function output and save it to the global enemies variable.
print(f"enemies outside function: {enemies}")


# ----------------------------------------------------------------------------------------------------------------------

# Python Constants and Global Scope:

# constants are defined, but never intended to be changed again. Like the value of PI = 3.14159

# the convention in python is to use all upper-case and separate by underscores:
PI = 3.14159
URL = "https://www.google.com"
LINKEDIN_USER = "www.linkedin.com/in/dillardchristopher"

# ----------------------------------------------------------------------------------------------------------------------

# Quick Review:

# 1. what would be printed in the console after running this code?

def a_function(a_parameter):
    a_variable = 15
    return a_parameter
 
a_function(10)
print(a_variable)

# Answer: NameError. a_variable is local to a_function() and is only available inside the function.

# 2. what would be printed in the console after running this code?

i = 50
def foo():
    i = 100
    return i
 
foo()
print(i)

# Answer: 50, the print statement is outside the function foo(), so it can't access the variable i = 100.
# it only sees the global i, which is equal to 50.

# 3. what would be printed in the console after running this code?

def bar():
    my_variable = 9
 
    if 16 > 9:
      my_variable = 16
 
    print(my_variable)
 
bar()

# Answer: 16, since 16 > 9 the conditions are met and my_variable is now 16, which is printed when called the bar() function.

# ----------------------------------------------------------------------------------------------------------------------

# Project: The Number Guessing Game:

# two modes Easy and Hard
# random number needs to be guessed ie random
# each wrong guess decreases the number of attempts -= 1
 #Number Guessing Game Objectives:

# I created my own version here without cross referencing the professor's notes:
# My version is shown immmediately below while the professor's version is shown last. They both produce the same result with some differences.

# i wanted the easy version to have random integer between 1-50 with 5 attempts, while the difficult version is 1-100 with 15 attempts. 
# this way the odds are slightly harder but not too hards, so its still reasonably challenging for the user.

import random
import replit
from replit import clear

logo = '''
.88b  d88. db    db .d8888. d888888b d88888b d8888b. db    db     d8b   db db    db .88b  d88. d8888b. d88888b d8888b. 
88'YbdP`88 `8b  d8' 88'  YP `~~88~~' 88'     88  `8D `8b  d8'     888o  88 88    88 88'YbdP`88 88  `8D 88'     88  `8D 
88  88  88  `8bd8'  `8bo.      88    88ooooo 88oobY'  `8bd8'      88V8o 88 88    88 88  88  88 88oooY' 88ooooo 88oobY' 
88  88  88    88      `Y8b.    88    88~~~~~ 88`8b      88        88 V8o88 88    88 88  88  88 88~~~b. 88~~~~~ 88`8b   
88  88  88    88    db   8D    88    88.     88 `88.    88        88  V888 88b  d88 88  88  88 88   8D 88.     88 `88. 
YP  YP  YP    YP    `8888Y'    YP    Y88888P 88   YD    YP        VP   V8P ~Y8888P' YP  YP  YP Y8888P' Y88888P 88   YD 
'''

def mystery_number_start():
  print(logo)

  difficulty_level = input("Select a difficulty: type 'hard' or 'easy': ").lower()

  while difficulty_level != "easy" and difficulty_level != "hard":
    difficulty_level = input("Check your spelling. Please type either 'easy' or 'hard': ")
    
  if difficulty_level == "hard":
    guesses_left = 15
    number = random.randint(1,100)
    print("I'm thinking of a number between 1 and 100...")
    print(f"You have {guesses_left} total guesses.")
  else:
    guesses_left = 5
    number = random.randint(1,50)
    print("I'm thinking of a number between 1 and 50...")
    print(f"You have {guesses_left} total guesses.")

  while guesses_left > 0:
    user_guess = int(input("What's your guess?: "))
    if user_guess > number:
      guesses_left -= 1
      print(f"Too high. You have {guesses_left} remaining guesses.")
    elif user_guess < number:
      guesses_left -= 1
      print(f"Too low. You have {guesses_left} remaining guesses.")
    else:
      print(f"Congrats! You guessed the mystery number {number}")
      return

  if guesses_left == 0:
    print("Game over. You ran out of guesses!")
    print(f"The mystery number was {number}")
    return

mystery_number_start()

play_again = input("Would you like to play again? Type 'y' or 'n': ")
if play_again == "y":
  clear()
  mystery_number_start()



# ----------------------------------------------------------------------------------------------------------------------

# THE PROFESSOR'S VERSION IS BELOW WHICH INCORPORATES SOME OTHER CONCEPTS TO ACHIEVE THE SAME RESULT:

# in this alternative version, number of turns for difficulty levels are written as constants (global variables in all-caps with underscores replacing spaces)
# the check_answer variable have parameters guesses, answer, turns that take the arguments of the user inputs, random generated number, and the running number of turns after each guess for the difficulty level.
# similarly to my version, an empty return statement was added to ensure that the function is done running after the game ends, so that the console can be clears and everything resets to default values.
# unlike my version, the professor opted to keep the random number as always an integer between (1,100), where I made the difference of easy (1,50) and hard (1,100)
# there is also no option to play again for the user.

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}") 

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()


