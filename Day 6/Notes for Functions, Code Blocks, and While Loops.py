# Notes for Functions, Code Blocks, and While Loops:

# Defining and Calling Python Functions:

# Functions performs a variety of tasks. They can be built-in functions OR  part of a module.
# a function is identifiable by its name followed by a set of parentheses:
# Think ->     num_char = len("Hello")
#              print(num_char)

# Making your own function:

def # used to make or define the function

def my_function():  # everything indented after the colon belongs to that function
    print("Hello")
    print("Bye")

# Call the function by writting out its name:
# my_function()

# Processing is defining the function using def, then name it and add a colon, the write what you want it to do by writing in the indented text, then call it.

# 1. Carol the robot --- using reeborg's world to nove robot to specific tile on 10 x 10 grid.
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
# give the robot specific instructions grouped under a single function name to carry out all the steps.
# Click on Reborg's ketboard to see all the functions at the top.
# move() moves the robot forward by one step, to move forward three steps just call the function in three consecutive lines of code.

def turn_around():
    turn_left()
    turn_left()

# --------------------------------------------------------------------------------------------------------------

# Challenge 1: create function to turn the robot to the right:

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Challenge 2: function to create a 2 x 2 square:

def create_square():
 turn_left()
 move()
 turn_left()
 turn_left()
 turn_left()
 move()
 turn_left()
 turn_left()
 turn_left()
 move()
 turn_left()
 turn_left()
 turn_left()
 move()

# or we use the newly created turn_around function like so:

def create_square()
   turn_left()
   move()
   turn_around()
   move()
   turn_around()
   move()
   turn_around()
   move()

# --------------------------------------------------------------------------------------------------------------

# Challenge 3:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
# Hurdle's Race:

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
   move()
   turn_left()
   move()
   turn_right()
   move()
   turn_right()
   move()
   turn_left()

move()
jump()
move()
jump()
move()
jump()
move()
jump()
move()
jump()
move()
jump()

# ^this achieves the right movement:
# we could also use a for loop to achieve the same thing starting with a move():

for step in range(6): # here the range is from 0 to 5, which is actually 6 in total hence the range(6)
   jump()

# --------------------------------------------------------------------------------------------------------------

# Indentation matters: Blocks are defined by their indentation:

def my_function():
    if sky == "clear":
      print("blue")
    elif sky == "cloudy":
      print("grey")
    print("Hello")
print("World")


# Spaces vs Tab (4 spaces = a tab): Spaces are the preferred method:

# Which version of the code will print "This will run"

def my_function():
    a =3
    if a > 2:
       print("This will run")
my_function()

# --------------------------------------------------------------------------------------------------------------

# While Loop:
# this checks whether a condition is true:

# think back to the robot hurdle excercise and replace the for loop with a while loop:


number_of_hurdles = 6
while number_of_hurdles > 0:
   jump()
   number_of_hurdles -= 1
   print(number_of_hurdles)

# the number_of_hurdles -= 1 dictates that ofter each subsequent jump we need to decrease the jumps left in the while loop by 1 until it reaches 0 more hurdles since 0 is not > 0.

while something_is_true:
   # Do this
   # Then do this
   # Then do this

# the loop continues to run as long as the specified condition continues to be true.


# Now code to stop while loop at the square with the flag ( the goal) using the pre-defined at_goal() condition.

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
   move()
   turn_left()
   move()
   turn_right()
   move()
   turn_right()
   move()
   turn_left()

while not at_goal():
   jump()

# for loops are good if you need to iterate something an repeat the process at each step of the for loop
# while loop when you dont care about the number you are in within a range, with while loops you just want to repeat the action until the specified condition is not true.

# --------------------------------------------------------------------------------------------------------------

# Infinite Loop: where a condition never becomes false:

# Ex:

while 5 > 3:
   # Do this:
 # 5 is always greated than 3, so this code will run until eternity, or the program crashes or times out.
 # check for this to print out the condition.

# --------------------------------------------------------------------------------------------------------------

# Challenge for while loops using Reborg's World:

# This time around there is a random wall placement each time, as well as random number of walls. 

# must use the preset conditions, front_is_clear() or wall_in_front() or at_goal() and their negation "while not":


# jump() function must be modified to take out the previous nested move() function so that if the robot is in fact approaching a wall, it doesn't start the jump() function by moving forward, but rather begin turning to the left.


def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
   turn_left()
   move()
   turn_right()
   move()
   turn_right()
   move()
   turn_left()


while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

# --------------------------------------------------------------------------------------------------------------

# Final hurdle challenge:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

#  now each wall has a variable height.
 
# this time I can use the pre-set wall_on_right() condition:

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
   turn_left()
   while wall_on_right():
       move()
   turn_right()
   move()
   turn_right()
   while front_is_clear():
       move()
   turn_left()


while not at_goal():
    if wall_in_front():
       jump()
    else:
       move()


# --------------------------------------------------------------------------------------------------------------

# Final Project: Escaping the Maze:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# Using Reborg's World:

# The algorythm (stategy) in this game is to program the robot to follow along the right wall of the maze until it reach the goal tile.
# if you can't go right nor forward, you must turn left as a last resort.
# functions are move() and turn_left()

# testing the conditions of whether front_is_clear(), right_is_clear(), wall_on_right(), and at_goal(). also useful the negation of a test, "not" in Python.

# Think about using a while look and if/elif/else statements. 

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
    
































