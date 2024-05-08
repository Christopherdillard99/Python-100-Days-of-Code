# Code for Blackjack Game:
# in art.py file import the logo, after creating the art.py file:
# adding some print statements with dashes to make sure the user can easily read the output in the console.

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

# import necessary modules and functions:

import random
from replit import clear
from art import logo


# define key variables used in the code:

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
    
# create play_game() variable which will repeat itself after clearing the console based on user input in the final lines of code: 


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
        print("-----------------------------")

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
    print("-----------------------------")

    
    print(compare(user_score, computer_score))



# prompt user to play game again, trigger the play_game() function after clearing the console if the user enters a y. 

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()