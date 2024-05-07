# Notes for Functions with Inputs
# Creating a Cipher program: "Caesar Cipher" type of encription.
# encoding message so that each letter would be shifted a certain number of letters over from its place in the alphabet.

# using functions to have multiple lines of code packaged under a single name, creating using this syntax:

def my_function():
    #Do this
    #then do this
    #finally do this

# call the function by simply typing its name

def greeting():
    print("Hey")
    print("What's up?")
    print("What's your name?")

# now function that allows for input
# assuming name is already known or user was previously prompted

def greeting_with_name(name): # the name enclosed within parentheses describes the name we want to use
    print(f"Hello {name}")
    print(f"What's up, {name}?")


# when calling the function, we can enter the user name like so:

greeting_with_name("Chris")

def my_function(something):
    #do this with something

something = 123
# something is the parameter
# 123 is the argument

# the argument is the actual piece of data (the actual value of the data) that will be passed over to the function when its being called
# the parameter is the name of that data, used within the function to be referred to and used

# -------------------------------------------------------------------------------------------------

# functions with more than one input:

def greet_with(name, location):
    print(f"Hello, {name}.")
    print(f"What is it like in {location}?")

# QUICK TIP: highlight text you want to wrap in quotes or parentheses, just highlight and press the desired key to wrap on both sides of the highlight, as many times as desired.


# ex: name is Chris, location is Wilmington

def greet_with(name, location):
    print(f"Hello, {name}")
    print(f"What is it like in {location}?")


# now run the function so that Chris and Wilmington are in the right spot 
# in other words, the two arguments are (Chris, Wilmington) which correspond to the two parameters of (name, location)
# these are positional arguments

greet_with("Chris","Wilmington")

# to absolutely make sure that there is no problem with positioning of the arguments, you can use Keyword Arguments

# Keyword Arguments ensure that name="Chris" and location = "Wilmington", so that order when calling the function does not matter

greet_with(location="Wilmington", name="Chris")


#------------------------------------------------------------------------------------------------------

# 2. Writing a function that calculates how many cans of paint I'll need to buy give a random height and width of wall, given that 1 can can cover 5 square meters.

# here the logic is that the total number of cans = (wall height x wall width) / coverage per can.

# e.g. Height = 2, width = 4, coverage = 5

# number of cans = (2 * 4) / 5 = 1.6 
# now, since i can buy 0.6 cans, the result needs to be rounded up the the next number for any answer that isn't a perfect integer.

# Write your code below this line 👇
import math

def paint_calc(height, width, cover):
    num_cans = (height * width)/cover
    roundup_num_cans = math.ceil(num_cans)
    print(f"You'll need {roundup_num_cans} cans of paint.") 

# the math module cas a ceil (ceiling) function that can be called like math.ceil(variableName) to round up to the nearest whole number.
# REMEMBER  to import the module whose function you want to use in the enwly created function, like import math preceding the rest of the code in this case.


# below was the given information for the assignment:
# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

# -----------------------------------------------------------------------------------------------------------------

# 2. Write a function that checks whether an input is a prime number. 
# i.e. numbers that can ONLY be cleanly divided by themselves and 1.

# logic thinking: every number can be divided by itself, but I want to ensure that any number besides 1 would produce a non-integer
# I can use modulo or remainder operator % somehow in this code?

# Write your code below this line 👇


def prime_checker(number):
  is_prime = True # this is set to True by default, will become False if number does not meet the defined criteria
  for i in range(2, number): # create a range here to check if number is prime. starting at 2 with not need to increase range to number + 1 either since prime is already numbers cleanly divisible by 1 and itself, thus we check for every number in between.
      if number % i == 0: # if our number divided by any other number in this range produces a remainder of zero (cleanly divisible) then our number is not prime.
        is_prime = False
  if is_prime:
      print("It's a prime number.")
  else:
      print("It's not a prime number.")

            
# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)

# ---------------------------------------------------------------------------------------------

# Caesar Cipher Project:

# top secret messages would have letters shifted over a certain number of letters.

# shifts are defined as shift = 0 being non, while shift = 1 is one over to the left (A becomes B), etc. 


# Step 1: Encryption:

# run program typing "encode"
# type in shift number
# type in message


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛


def encrypt(plain_text, shift_amount):
    cipher_text = "" #starts out as an empty string
    for letter in plain_text:
        position = alphabet.index(letter) # here I am searching for each letter in the alphabet list where it match the letter in the plain_text input. the position is the number in the alphabet list that the letter falls in (i.e. 0, 1, ..., 25)
        new_position = position + shift_amount # shifting by the specified amount.
        new_letter = alphabet[new_position] # brackets here returns the item in the list that matches the value for the number of the new_position. i.e if new position had a shift of 6 and the original letter was A, then the new letter is G. 
        cipher_text += new_letter # adding new letters to the cipher_text string as the for loop continues to run.
    print(f"The encoded text is {cipher_text}")

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

encrypt(plain_text = text, shift_amount = shift) # using Keyword Arguments (as opposed to just positional arguments) call the new function and make sure that the arguments align with the right parameters in the function.


# to ensure that words that include letters closer to the end of the alphabet do not produce an error when shifting over, I simply duplicated the alphabet list so that a new A comes after Z in the first alphabet of the list.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# this works since the the index function will only return the letter as it first occurs so it will never shift over from any of the letters in the second alphabet in the list. 



# -------------------------------------------------------------------------------------------


# Step 2: Decryption:

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

def decrypt(cipher_text, shift_amount):
  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"
  plain_text = ""
  for letter in cipher_text:
    position = alphabet.index(letter)
    new_position = position - shift_amount # since we're moving backwards in the alphabet, there needs to be a - sign preceding the shift_amount
    plain_text += alphabet[new_position]
  print(f"The decoded text is {plain_text}")


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == "encode":
  encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
  decrypt(cipher_text=text, shift_amount=shift)



# ------------------------------------------------------------------------------------------------

# Step 3: Reorganize the Code:

# there are a lot of similarities between the code for encoding and decoding, I need to combine these two functions into a single function called Caeser that eliminates the need for the if elif statements 

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

# def encrypt(plain_text, shift_amount):
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     cipher_text += alphabet[new_position]
#   print(f"The encoded text is {cipher_text}")

# def decrypt(cipher_text, shift_amount):
#   plain_text = ""
#   for letter in cipher_text:
#     position = alphabet.index(letter)
#     new_position = position - shift_amount
#     plain_text += alphabet[new_position]
#   print(f"The decoded text is {plain_text}")

# if direction == "encode":
#   encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#   decrypt(cipher_text=text, shift_amount=shift)

def caesar(start_text, shift_amount, cipher_direction): # need three inputs for text, shift, and direction
   end_text = "" # need to start with empty string again
   if cipher_direction == "decode": # this part NEEDS to come before the for loop
      shift_amount *= -1 # here the shift amount is set to be multiplied by negative 1 when we need to decode a message, otherwise a encoded message would just be the position in the alphabet plus the positive shift amount in for each letter.
   for letter in start_text:
      position = alphabet.index(letter) # this line was identical in both original functions
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    print(f"The {cipher_direction}d coded text is {end_text}") # this is a dynamic text so that the code will return both encoded and decoded depending on user specified cipher direction.


#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

caesar(start_text = text, shift_amount=shift, cipher_direction=direction)


