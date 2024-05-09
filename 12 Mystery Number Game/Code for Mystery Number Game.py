#Number Guessing Game Objectives:

# I created my own version here without cross referencing the professor's notes:
# compare with an alternative version that produces the same result (with some game rule differences and style/wording differences at end of the notes file for day 12.)

# two modes: Easy and Hard
# random number needs to be guessed using the random.randint() function for range, either 1-50 or 1-100.
# easy difficulty means there are 5 attempts. Hard difficult = 15 attempts. 
# this way the odds are slightly harder but not too hards, so its still reasonably challenging for the user.
# each wrong guess decreases the number of attempts -= 1

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


