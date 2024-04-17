# Day 7: Hangman Project:

# Standard, add an element to the ASCII image if guessed letter is wrong. 
# logic  behind the project:

#           1. Start program - welcome message

#           2. Generate a random word

#           3. Generate corresponding blank letters

#           4. Prompt user to guess a letter

#           5. Is the letter guessed correctly? Yes or No

#               a. Yes? Replace blank with letter.

#                   i. Are all the blanks fills? Yes - outcome

#                                                No  - repeat process at step 4.

#               b. No? lose a life

#                   i. have they lost all lives? Yes - game over

#                                                No  - repeat process at atep 4.



# ---------------------------------------------------------------------------------------------------

# Steps for Hangman:

# Step 1:

#       1. Randomly choose word from list variable:

word_list = ["aardvark", "baboon", "camel"]

import random

chosen_word = random.choice(word_list)

#       2. Prompt user to guess a letter:

guess = input("Guess a letter: ").lower() # assign as lower case to ensure case consistency 

#       3. Classify the user's guess:

for letter in chosen_word:
  if letter == guess:
    print("Right")
  else:
    print("Wrong")

# ---------------------------------------------------------------------------------------------------

# Step 2:

# create a list with as many blanks as in the chosen word, so we can then replace the blanks with the right letter if the user makes a correct guess.
# the code should also print out a list string of underscores with filled-in spaces with the letters, as applicable, with each guess until the word is guessed or unti the user loses all lives.
# the number of underscores needs to match the number of letters in the word.


guess = input("Guess a letter: ").lower()


# display = []
# for _ in chosen_word: # underscore can be replaced with "letter", name it what ever makes the most sense
#   display += "_"
# print(display)

# alternatively you could create this loop with a range:

display = []
word_length = len (chosen_word) # since we are referencing the length of the word often, we can simplify the code by creating this variable.
for _ in range(len(chosen_word)): 
  display += "_"
print(display)

# loop through each position in that chosen word, if there is a match, we replace the underscore with the correctly guessed letter in the right space.

for position in range(word_length): # using new word_length variable instead of placing len(word_choice) inside of the range() function.
  letter = chosen_word[position]
  if letter == guess:
    display[position] = letter


print(display)

# ---------------------------------------------------------------------------------------------------

# Step 3. Checking if the player has won (only if they guess the letter correctly, incorrect letter will be punished in the next step):

# must enable the repeatability of the game, so that the player can keep guessing until they either win or are eliminated.

# use a while loop here, only stopping when all letters are guessed in the chosen word.

# remember the negation factor of whether the condition is not true, basically flipping the logic for the if statement.


end_of_game = False

while not end_of_game:
  guess = input("Guess a letter: ").lower


while not display == list(chosen_word):
  guess = input("Guess a letter: ").lower()
  for position in range(word_length):
    letter = chosen word[position]
    if letter == guess:
      display[position] = letter

# basically using the code from step 2, just repeating until the word is guess, having filled all the blanks in the chosen_word list


end_of_game = False

while not end_of_game:
  guess = input("Guess a letter: ").lower

for position in range(word_length):
  letter = chosen_word[position]
  print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
  if letter == guess:
    display[position] = letter

print(display)

if "_" not in display:
  end_of_game = TRUE 
  print("You won!")

# ---------------------------------------------------------------------------------------------------

# Step 4: Keeping track of player's lives:

# ASCII art needed for the stages of lives left.
# when lives go down to zero the while loop needs to stop and the game ends, printing a you lost! message.

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# creating a variable called lives that'll keep track of the remaining number of lives.
# set lives equal to the number of stages for hangman, being 6 with the selected ASCII 

lives = 6

for position in range(word_length):
  letter = chosen_word[position]
  print(f"Current position: {position}\n Current letter: {leter}\n Guessed letter: {guess}")
  if letter == guess:
    display[position] = letter

if guess not in chosen_word:
  lives -= 1
  if lives == 0:
    end_of_game = True
    print("You lost!")

print(stages[lives]) # this will ensure that the right ascii art is print with each life lost based on the new stage.


# ---------------------------------------------------------------------------------------------------

# Step 5: load in the full word list and ensure that a hangman logo is printed at start of game, make sure that if the user guesses the same letter again it doesnt punish them adn just print a simple phrase to let them know.

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

word_list = [
'abruptly', 
'absurd', 
'abyss', 
'affix', 
'askew', 
'avenue', 
'awkward', 
'axiom', 
'azure', 
'bagpipes', 
'bandwagon', 
'banjo', 
'bayou', 
'beekeeper', 
'bikini', 
'blitz', 
'blizzard', 
'boggle', 
'bookworm', 
'boxcar', 
'boxful', 
'buckaroo', 
'buffalo', 
'buffoon', 
'buxom', 
'buzzard', 
'buzzing', 
'buzzwords', 
'caliph', 
'cobweb', 
'cockiness', 
'croquet', 
'crypt', 
'curacao', 
'cycle', 
'daiquiri', 
'dirndl', 
'disavow', 
'dizzying', 
'duplex', 
'dwarves', 
'embezzle', 
'equip', 
'espionage', 
'euouae', 
'exodus', 
'faking', 
'fishhook', 
'fixable', 
'fjord', 
'flapjack', 
'flopping', 
'fluffiness', 
'flyby', 
'foxglove', 
'frazzled', 
'frizzled', 
'fuchsia', 
'funny', 
'gabby', 
'galaxy', 
'galvanize', 
'gazebo', 
'giaour', 
'gizmo', 
'glowworm', 
'glyph', 
'gnarly', 
'gnostic', 
'gossip', 
'grogginess', 
'haiku', 
'haphazard', 
'hyphen', 
'iatrogenic', 
'icebox', 
'injury', 
'ivory', 
'ivy', 
'jackpot', 
'jaundice', 
'jawbreaker', 
'jaywalk', 
'jazziest', 
'jazzy', 
'jelly', 
'jigsaw', 
'jinx', 
'jiujitsu', 
'jockey', 
'jogging', 
'joking', 
'jovial', 
'joyful', 
'juicy', 
'jukebox', 
'jumbo', 
'kayak', 
'kazoo', 
'keyhole', 
'khaki', 
'kilobyte', 
'kiosk', 
'kitsch', 
'kiwifruit', 
'klutz', 
'knapsack', 
'larynx', 
'lengths', 
'lucky', 
'luxury', 
'lymph', 
'marquis', 
'matrix', 
'megahertz', 
'microwave', 
'mnemonic', 
'mystify', 
'naphtha', 
'nightclub', 
'nowadays', 
'numbskull', 
'nymph', 
'onyx', 
'ovary', 
'oxidize', 
'oxygen', 
'pajama', 
'peekaboo', 
'phlegm', 
'pixel', 
'pizazz', 
'pneumonia', 
'polka', 
'pshaw', 
'psyche', 
'puppy', 
'puzzling', 
'quartz', 
'queue', 
'quips', 
'quixotic', 
'quiz', 
'quizzes', 
'quorum', 
'razzmatazz', 
'rhubarb', 
'rhythm', 
'rickshaw', 
'schnapps', 
'scratch', 
'shiv', 
'snazzy', 
'sphinx', 
'spritz', 
'squawk', 
'staff', 
'strength', 
'strengths', 
'stretch', 
'stronghold', 
'stymied', 
'subway', 
'swivel', 
'syndrome', 
'thriftless', 
'thumbscrew', 
'topaz', 
'transcript', 
'transgress', 
'transplant', 
'triphthong', 
'twelfth', 
'twelfths', 
'unknown', 
'unworthy', 
'unzip', 
'uptown', 
'vaporize', 
'vixen', 
'vodka', 
'voodoo', 
'vortex', 
'voyeurism', 
'walkway', 
'waltz', 
'wave', 
'wavy', 
'waxy', 
'wellspring', 
'wheezy', 
'whiskey', 
'whizzing', 
'whomever', 
'wimpy', 
'witchcraft', 
'wizard', 
'woozy', 
'wristwatch', 
'wyvern', 
'xylophone', 
'yachtsman', 
'yippee', 
'yoked', 
'youthful', 
'yummy', 
'zephyr', 
'zigzag', 
'zigzagging', 
'zilch', 
'zipper', 
'zodiac', 
'zombie', 
]

# given the new, long list of word I need to modify the line of code from the first steps so that we can reference the new list by creating a module.

import random

# Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]

from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo
print(logo)


#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        # - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # - Import the stages from hangman_art.py and make this error go away.
    from hangman_art import stages
    print(stages[lives])


#Step 5

import random

# Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo
print(logo)

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Import the stages from hangman_art.py and make this error go away.
    from hangman_art import stages
    print(stages[lives])




