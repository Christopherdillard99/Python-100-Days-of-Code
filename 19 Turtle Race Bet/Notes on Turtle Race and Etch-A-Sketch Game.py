# Day 19: More Turtle Graphics, Event Listeners, State and Mulitple Instances of an Object

# Creating a Game of Etch-A-Sketch usign Turtle Graphics:
# The turtle (arrow) can be programmed to turn directions with up and down arrows and clockwise/anticlockwise movements.

# Creating a turtle racing game , where you bet on which color turtle you think will win the race.
# once you bet the color, the 6 turtle line up and start moving at a random pace.
# race ends once the first turtle reaches the end of the screen.

# the idea is essentially, listening to key-strokes on the keyboard:
# "Turtle Event Listeners"

# check turtle documentation to read up on screen events.
# particularly the listen function, which waits for events that a user can trigger like taping on a key
# https://docs.python.org/3/library/turtle.html#turtle.listen



# -------------------------------------------------------------------------------------------------------------------

# Higher Order Functions:
# fuctions that can work with other functions as an input to work within the body of the function - example being this calculator:

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator(n1, n2, func):
    return func(n1, n2)

result = calculator(2,3,divide)
print(result)

# higher order functions are VERY useful for when we want to listen to event and trigger certain actions like when a specific key is pressed.

# -------------------------------------------------------------------------------------------------------------------

# basic demo code in Turtle:

from turtle import Turtle, Screen

# create turtle and screen objects after importing the necessary Classes from the turtle module

tim = Turtle()
screen = Screen()

# in order to begin listening to event:

screen.listen()

# bind keystroke to event using an even listener using the onkey() method in the turtle module
# also create function to move forward by 10 paces and use this function as an input, only passing name w/o parentheses.

def move_forwards():
    tim.forward(10)

screen.onkey(key="space", fun=move_forwards) #whenpassing a function as an argument,the function doesn't use parentheses
screen.exitonclick() # so screen doesn't disappear when running code

# -------------------------------------------------------------------------------------------------------------------

# Building an Etch-A-Sketch App using turtle:

# Which keys will do what:
            # W = Forwards
            # S = Backwards
            # A = Counter-Clockwise
            # D = Clockwise
            # C = Clear drawing and set turtle back in center

# 1. Must create fucntions for all 4 movements:

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.listen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
    # alternatively there is a method called as tim.left(10)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
    # also possible to use another method as tim.right(10)

def clear():
    tim.clear() # clears all the drawings
    tim.penup() # so that the turtle doesn't trace it's path back to the center
    tim.home() # moves turtle to origin (ie center of screen)
    tim.pendown() # so that the turtle will start drawning it's path again after returning to the center

screen.onkey(move_forwards,"w")
screen.onkey(move_backwards,"s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
screen.onkey(clear,"c")
screen.exitonclick() 

# -------------------------------------------------------------------------------------------------------------------

# Object State and creating multiple instances of the same object:

# how to create multiple turtle for each color to be bet on?
# remember Turtle Class is like the blueprint, while the object (tim so far) is a single instance of the turtle

# can create multiple turtle object like timmy, tommmy, tammy using same code...
# this way timmy, tommy, and tammy are all "instances" or examples of the turtle object
# they can have different attributes and be doing different things
timmy = Turtle()
tommy = Turtle()

# State = the "state" of Timmy's color attribute is green and the state of Tommy's color attribute is purple
timmy.color = green
tommy.color = purple
# the turtle's can also has have different states in terms of what they are doing, if anything at all.

# -------------------------------------------------------------------------------------------------------------------

# Building the Turtle Race, exemplify States and Instances
# pop up prompting user to enter which color turtle they think will win.
# turtle line up at start line and begin movement at random paces
# once a turtle reaches the end, the game ends
# user then sees a printed message for whether they won or lost and will see which turtle won the game

# dimensions are very crucial, so use the setup() method in Screen class to set up the width and height to 500 and 400, respectively.
# use keyword arguments instead of just positional arguments for width and height ].
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.setup(width = 500, height = 400) # keyword arguments

# use textinput() method to ask user for which turtle color they want to bet on
# if input is a number, then user numinput() 
# turtle.textinput(title, prompt)

screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# now, the turlte need to go to the start of the line or very left of the screen. BUT each individual turtle can't go to the same exact spot
# use method goto(x, y)

# the coordinate system in turtle has (0,0) at the very center.
# remember turtle.heading() E = 0, N = 90, W = 180, S = 270.
# the screen.setup(width = 500, height = 400) code line before means that there are 200 above the center and -200 below, while there are 250 right and -250 left

# turtle all the way to left side of screen: tim.goto(x=-250,y=0)
# -250 x actually makes it impossible to see the turtle, sooooo set the x value to -230 to be slightly away from the edge.

tim.goto(x=-230,y=-100)

# precede the previous line with tim.penup() since we don't want to trace any movement, only move the turtle itself.
# also, change the turtle shape from default arrow to initialize with shape as a "Turtle"

tim.Turtle(shape="Turtle")
tim.penup()
tim.goto(x=-230,y=-100)

screen.exitonclick()

# -------------------------------------------------------------------------------------------------------------------

# Now, the 6 different turtle objects need to be created, which can be done using a for-loop
# additionally, each turtle instance needs to have different states for their color.
# the color will be stored in a list for the main colors of the rainbow.
# each turtle with have the x-value of zero, only the y-value will change, in increments of + 30 for each iteration of the for-loop:
# instead of adding 30 to the y-value from a starting point in the third quadrant of the coordinate plane, each instances starting y-value is contained in a list.

from turtle import Turtle, Screen

screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(0,6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index]) #each subsequent loop indexes its corresponding position in the colors list.
    tim.penup()
    tim.goto(x=-230,y=y_positions[turtle_index]) #each subsequent loop indexes its corresponding item in y_position[]


screen.exitonclick()

# -------------------------------------------------------------------------------------------------------------------
# having the turtle at their starting places now, they need to advance randomly between (0,10) until one of them reaches the right side of the screen.
# in other words, until any turtle's x-value is >= 250. 
# use a while-loop for this. new variable is created called is_race_in_progress set to False.

is_race_in_progress = False

# so the while loop won't start prematurely while the user is prompted to bet on a color:

if user_bet:
    is_race_in_progress = True

while is_race_in_progress:
    rand_distance = random.randint(0,10) # this is inclusive, also MUST import random module now.
    turtle.forward(rand_distance)

screen.exitonclick()

# Must create list of turtles in the for-loop that was created earlier, and append turtle to list of all_turtles:
# NOTE: must refactor all instances of tim to new_turtle, so that the creation of each turtle in all 6 colors is appended to the bigger list:

all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index]) 
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

# each turtle instance has a different state, moving forward by a different amount.

if user_bet:
    is_race_in_progress = True

while is_race_in_progress:

    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# so far, all 6 turtles move forwards at random distances BUT they do so forever. Now, they need to stop once of them reaches to end of the screen.

# stopping condition should be where turtle reach x = 250 in theory, BUT the turtle object is 40 x 40, so the x value needs to be shifted to the left accordingly. 

if user_bet:
    is_race_in_progress = True

while is_race_in_progress:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_in_progress = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)






# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------





