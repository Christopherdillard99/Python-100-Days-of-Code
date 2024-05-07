# Day 9: Creating a Secret Auction (Silent Auction):
#   1. Prompt user for name and their bid
#   2. Ask if there are any other biders, then hand back the laptop and the previous bid is hidden until there are no more bids.

# The primary focus here is Python Dictionaries and Nesting (lists within lists, dictionaries inside dictionaries, and mixes of both)

# ------------------------------------------------------------------------------------------------------------------------------------

# Dictionaries:

# 1. program instruction for the computer
# but think about these as a table with the following keys and values:
            # Key: equivalent of the word in the dictionary,  Value: each key has an associated value, being its definition.
            # 1. Bug:                                            An error in a program that prevents the program from running as expected.
            # 2. Function:                                       A piece of code that you can easily call over and over again.
            # 3. Loop:                                           The action of doing something over and over again.

# Creating a dictionary:

{Key: Value} # Wrap in curly braces: the key, followed by colon, followed by the value.

# using the keys and values from the example, we have the following code to create a dictionary, separate the key and value pairs with a comma:

dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
 }

# syntax to retrieve the definition (value) of a word/term (key) within a dictionary:

print(dictionary["Bug"]) # ensure that there is no typo, which would yield a KeyError, also need to using quotations for a string because without "" it looks like a variable name.

# adding a new entry later in the code. tap into the dictionary and define the key with an equal sign like below:

dictionary["Debugging"] = "Debugging is the process of identifying and repairing bugs in a program. This task is vital for the deployment of a product."
print(dictionary)


# Creating a nempty dictionary, so that you can continuously add terms later:
empty_dictionary = {}  # here there is clearly no info inside.

# wipe a previously made dictionary:
dictionary = {}
print(dictionary) # this action is helpful if you want to restart a game to wipe player stats.

# edit an item in a dictionary (this example works after commenting out the previous example for wiping the dictionary.)

dictionary["Bug"] = "A moth in your computer."
print(dictionary)

# loop through a dictionary

# 1.  only returning the key names:
for key in dictionary:
    print(key)

# 2. now first print the key name on one line, then print its value on the following line, continuing that loop till there are no more keys and values to display in the dictionary.
for key in dictionary:
    print(key)
    print(dictionary[key])


# ------------------------------------------------------------------------------------------------------------------------------------

# 1. Create a program that grades students' test scores:
# each student's name is a key, while their score is the value in the dictionary.
# the idea is using a loop on the dictionary of student scores.

# the program needs to match the score's with a criteria for ranges like fail for 70 or lower, acceptable for 71-80, exceeds expectations for 81-90, and outstanding for 91-100.

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

# need to create empty dictionary for student grades:
student_grades = {}

# need to write code to add grades to the new dictionary:

for student in student_scores:
  score = student_scores[student]
  if score > 90:
    student_grades[student] = "Outstanding"
  elif score > 80:
    student_grades[student] = "Exceeds Expectations"
  elif score > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"

# print out the student grades

print(student_grades)

# ------------------------------------------------------------------------------------------------------------------------------------

# Nesting Lists & Dictionaries within a Dictionary:

{ 
   Key: [List],
   Key2: {Dict},
}

# Ex: having a simple dictionary wioth country names and capitals, 

#Nesting 
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

# Now wanting a list in the dictionary with cities that I have visited within a country.

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting dictionary within a dictionary to keep track of cities visited and how many times they've been visited

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

# Now nesting a dictionary inside a list - remember that dictionary is enclosed in {} while lists are enclosed in [], now I can interate through each dictionary in the list while runninng a loop:

travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]

# ------------------------------------------------------------------------------------------------------------------------------------

# 2. Create a function that adds countries I've visited into, with the name of the country, name of cities visited, and number of visits.

# Steps needed to follow (with results in the TODO section):
#       1. Create new function
#       2. Create new empty dictionary
#       3. Create a key and value pair to store in the new dictionary, do this 3 times for each variable in the function which must be set equal to vars names for the inputs
#       4. Use travel_log.append[new_country] to add this new country and the 3 infos to the broader dictionary (travel_log) of all the places I've been.

country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

# TODO: Write the function that will allow new countries to be added to the travel_log. 
def add_new_country(country, times_visited, cities_visited):
  new_country = {}
  new_country["country"] = country
  new_country["visits"] = times_visited
  new_country["cities"] = cities_visited 
  travel_log.append(new_country)

# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")

# ------------------------------------------------------------------------------------------------------------------------------------ 

# Blind Auction program notes:

# the inputs are the user's name, bid amount, and whether there are more bids. 
# the bid amount is hidden is the user input is Yes from the next user while they enter their bid.
# this process is repeated until a user enters No more bidders, after which the program works out who has the highest bid and display this user's name and their bid amount.

# need to create a dictionary so that each person's name is the key and their bid is the value.
# at the end of the program, I'll loop through this new dictionary to find the highest bid.


from replit import clear

from art import logo

print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record): #bidding_record is a dictionary of key-value pairs where each key is a name and value is number
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()

# to indent a check of text all at once, highlight text then command + ] for right-side indent or command + [ for left-side indent


