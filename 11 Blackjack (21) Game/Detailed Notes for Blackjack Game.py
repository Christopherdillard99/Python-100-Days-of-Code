# Day 11: Creating a Blackjack Game (aka 21)

# using cards, add up nuber closest to 21 but not over 21. 
# if player's cards surpass 21, that is a "bust", they are disqualified and automatically lose

# in the game, you are dealt two cards, the first card for both teams is revealed. Then the player is dealt one that only they know. 
# they can either select y for another card or n to pass before the dealer's second card is revealed.
# y is also "hit", and n is "stand" in blackjack terminology.

# cards 2-10 count as their face values.
# jack, queen, and king each count as 10.
# ace can either count as 1 or 11 towards your total depending on which scenario best fits your hand to win.

# if both the player and dealer have the same value (like 20 and 20) there is a "draw".

# also if the dealer ends up with a hand where the two cards' value is less than 17, then the dealer must pick up another card.

# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# assumption that each of the cards have the same chance of being drawn. 
# 11 is ace, and the 10s are of course 10, jack, queen, and king.

# ---------------------------------------------------------------------------------------------
# provided resources to understand the game and project:
# online game example of blackjack:  https://games.washingtonpost.com/games/blackjack/
# flowchart for the project: https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt


                    # house rules and assumptions in this program:
                    # the deck is unlimited in size.
                    # there are no jokers.
                    # the jack/queen/king all count as 10.
                    # the ace can count as 11 or 1.
                    # the list of cards is as follows: cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
                    # there is an equal probability that each card will be drawn.
                    # cards are not removed from the deck as they are drawn.
                    # the computer is the dealer.


# Step-by-step walkthrough of the game rules with notes.

#------------------------------------------------------------------------------------------------------------------------------------

# 1. Creating a deal_card() function that uses the card list to return a random card.
# first, cards are chosen at random, so I needed to import the random module to use the random.choice() function on the cards list.
# this is saves to the card variable, so that the deal_card function return the random choice from the list.

import random

def deal_card():
    ''' Returns a random card from the deck.'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    retrun card

#------------------------------------------------------------------------------------------------------------------------------------

# 2. Deal the user and computer 2 cards using each deal_card() and append().
# start with for loop to run twice to return 2 random cards from the deck
# add a single card from the deal_card random choice, saved into a new_card variable.
# use .append() to add a second random card (ie. saved a second result of the new_card variable after running the deal_card() function again in the loop)
# these two random user cards are added to a user_cards list.

# for _ in range(2):
#     new_card = deal_card()
#     user_cards.append(new_card)

# ^ this is actually redundant and can be simplified using the modified code below for both the user and the computer's decks:

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

#------------------------------------------------------------------------------------------------------------------------------------

# 3. Create function to calculate the score that takes the list of cards as its input.
# must return the score after, using the sum() function.
# sum function can add up an iterable (ie a list) by adding everything left-to-right that is separated by a comma.
# cards[] was a list created previously in the deal_card() function from step one.

def calculate_score():
    ''' Calculates the score, taking the list of cards as its input as a sum.'''
    return = sum(cards)

#------------------------------------------------------------------------------------------------------------------------------------

# 4. Inside calculate_score() the program must check for a blackjack, being a hand with only 2 cards that are ace + 10 (ie 11 + 10). 
# if there is a blackjack detected, then the function return a 0 to indicate a blackjack instead of 21.

# def calculate_score(cards):
#     if 11 in cards and 10 in cards and len(cards) == 2:

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0.
    
#------------------------------------------------------------------------------------------------------------------------------------

# 5. now must check for whether there is an 11 (an ace). if the score is already over 21, we remove the 11 and replace it with a 1.
# think of functions append() and remove().
# this can be done with an if statement.

if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)

#------------------------------------------------------------------------------------------------------------------------------------

# 6. if the computer or the user has a blackjack (ie calculate_score(cards) returns a 0) or the user's score is over 21, then the game ends.
# if the right conditions are met, the game ends. 
# need to create a var for the is_game_over set to the boolean False by default.
# within the if statements, the program checks whether the game conditions will trigger the is_game_over to be set to True.
# add in some print statements to enhance the game and make it playable.
# only the first card from the dealer is revealed to the user, hence the 0 in square brackets to denote the first item in the computer_cards[] list.

user_score = calculate_score(user_cards)

computer_score = calculate_score(computer_cards)

print(f" Your cards: {user_cards}, current score: {user_score}")
print(f" Computer's first card: {computer_cards}[0]")

is_game_over = False

if user_score == 0 or computer_score == 0 or user_score >21:
    is_game_over = True

#------------------------------------------------------------------------------------------------------------------------------------

# 7. If game has not ended, prompt the user to choose whether to draw another card or pass their turn and reveal the dealer's other card.
# so, a 'y' would append another random card to the user_cards[], while 'n' ends the game and compares the sum of the scores to determine a winner.
# edit the if statement from step 6 to include an else that includes this prompt:

if user_score == 0 or computer_score == 0 or user_score >21:
    is_game_over = True
else:
    user_should_deal = input("Type 'y' to receive another card or 'n' to pass: ")
    if user_should_deal == 'y':
        user_cards.append(deal_card())
    else:
        is_game_over = True

#------------------------------------------------------------------------------------------------------------------------------------

# 8. Create a while loop to check everything from step 7 until the game is completed:

is_game_over = False

while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f" Your cards: {user_cards}, current score: {user_score}")
    print(f" Computer's first card: {computer_cards}[0]")

    if user_score == 0 or computer_score == 0 or user_score >21:
        is_game_over = True
    else: 
        user_should_deal = input("Type 'y' to receive another card or 'n' to pass: ")
    if user_should_deal == 'y':
        user_cards.append(deal_card())
    else:
        is_game_over = True

#------------------------------------------------------------------------------------------------------------------------------------

# 9. Once the user is done, the computer needs to "play". The computer will keep drawing cards as long as its score is less than 17.
# the exception is if the computer already has a blackjack represented by a 0 in the program.

while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

#------------------------------------------------------------------------------------------------------------------------------------

# 10. Must create a function called compare() that passes in the user_score and the computer_score.
# If the computer and user both have the same score, it's a draw. 
# if computer has blackjack (0), the user loses, while the computer loses if the user has a blackjack.
# the if elif else statements are returned from top to bottom. 

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw...  o_O"
    elif computer_score == 0:
        return "You lose. Opponent has a blackjack. :-("
    elif user_score == 0:
        return "You won with a blackjack. :^)"
    elif user_score > 21:
        return "You lose. Your score went over 21. :-("
    elif computer_score > 21:
        return "You won! Opponent's score went over 21. :^)"
    elif user_score > computer_score:
        return "You win! :^)"
    else:
        return "You lose :-("
    
# call compare() function at end of game to print the correct messages after the wile loop from step 9.
# add more print statements to make the game better.

while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

    print(f" Your final hand: {user_cards}, final score: {user_score}")
    print(f" Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))



#------------------------------------------------------------------------------------------------------------------------------------

# 11. Ask user if they want to play again. If yes, clear the console and reshow the ASCII art logo.
# indent all code after step 2 to include it within a new function called play_game()
# after while loop if evaluated, a "y" response from the user, trigger the play_game function, essentially all the other code created in this project.
# to clear console, import the clear function from the replit module, from replit import clear.
# the clear function() is placed before the play_game() function in the while loop.
# play_game() is of course defined in the lines before the while loop with the user input, so that is can be correctly called.
# in art.py file import the logo, after creating the art.py file:

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

import random
from replit import clear
from art import logo


def deal_card():
    ''' Returns a random card from the deck.'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
  """Takes a list of cards and returns the score calculated from the cards, using the sum."""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose :-("

    if user_score == computer_score:
        return "It's a draw...  o_O"
    elif computer_score == 0:
        return "You lose. Opponent has a blackjack. :-("
    elif user_score == 0:
        return "You won with a blackjack. :^)"
    elif user_score > 21:
        return "You lose. Your score went over 21. :-("
    elif computer_score > 21:
        return "You won! Opponent's score went over 21. :^)"
    elif user_score > computer_score:
        return "You win! :^)"
    else:
        return "You lose :-("
    

def play_game():

    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your cards: {user_cards}, current score: {user_score}")
        print(f" Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to receive another card or 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f" Your final hand: {user_cards}, final score: {user_score}")
    print(f" Computer's final hand: {computer_cards}, final score: {computer_score}")

    
    print(compare(user_score, computer_score))


# prompt user to play game again, trigger the play_game() function after clearing the console if the user enters a y. 

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()