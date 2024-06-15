# Day 20: (First Half of) Building the Snake Game:
# Moving snake controlled by keyboard that goes and get's food (shown by single dots)
# the catch is that the snack cannot run into the wall while chasing the dots.
# the snake's tail lenth also grows with each round, making it harder to play.

# Problem breakdown for both days:

# Day 1:

        # Create snake body: starts out as 3 squares on screen.
        # Move snake body: continuously moves forwards, user just tell the snake to move direction.
        # Control the snake with keyboard controls: up, left, down, and right arrow keys.

# Day 2:

        # Detect collision with food, so that a new random piece is created on the screen.
        # Create a scoreboard 
        # game ends: when snake collides with wall OR if snake has collided with its own tail

#---------------------------------------------------------------------------------------------------------------------------

# import the turtle module with the Screen and Turtle classes
# setup the screen to the desirable dimensions, using the setup() method from the Screen class
# change the screen background color to black
# change the screen's title at the top of the pop-up window.
# as always call the exitonclick() method at the very END of the program.

from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")

# the following line is moved to the very end of the code:
screen.exitonclick()

#---------------------------------------------------------------------------------------------------------------------------

# 1. Creating the Snack's body:
# Asingle square on the screen is 20 pixels tall by 20 pixels wide.
# I need three of these to start out the game
# I need to figure out the right coordinates for these and ensure that the snake's head starts at the center of the screen.
# the snake's body will be white and the first segment is at (0,0) and the next two are placed consecutively 20 pixels behind.
 
# long way:

segment_1 = Turtle(shape="square")
segment_1.color("white")
segment_2 = Turtle(shape="square")
segment_2.color("white")
segment_2.goto(x=-20,y=0)
segment_3 = Turtle(shape="square")
segment_3.color("white")
segment_3.goto(x=-40,y=0)

# simplified version using a for-loop with a list of starting positions containg tuples:

starting_positions = [(0,0),(-20,0),(-40,0)]

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)

#---------------------------------------------------------------------------------------------------------------------------

# 2. Move the Snake automatically across the screen. user changes the direction as they please.

# putting segments into a list, starting as empty list and appending the new segment with each round:

starting_positions = [(0,0),(-20,0),(-40,0)]

segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

# create new variable for with boolean valeu for whether the game_is_on set by default to True

game_is_on = True
while game_is_on:
    for segment in segments:
        segment.forward(20)

# some problems observed in the output behavior: the pen must be up with penup() method and the segment are not moving in synch

# fix this by placing a new_segment.penup() line before each new segment is moved to it's new position.
# now, as for the animation of each segment moving in order (sort of like a caterpiller on the screen) I need to use the turtle.tracer() method:

# the idea is to treat this output (the drawing of the snake) like a GIF in that we can specify when the screen is "refreshed" between each movements. 
# the update() method is going to tell the screen when to update.
# first, turn of the tracer in the screen class at the start of the code by setting it to zero:

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

# if the code is ran with only this additional line, the screen will just show as black and continually run the for loop withing to show for it.
# so, we must call screen.update() after all the segments are added.

# if you ever want to slow down the output to better understand what the code is doing, import the time module and call the time.sleep(1) method.
# this sleep(1) method slows down output by creating a 1 second delay.

import time

# in doing so, I saw that the snake moves one by one. 
# So, I placed the screen.update() line right above the for loop in the while loop so that it move altogether as one.
# also, move the time.delay(1) line to above the for loop and change the delay to 0.2 so that the snake moves a little faster across the screen.

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    for segment in segments:
        segment.forward(20)

screen.exitonclick()

#---------------------------------------------------------------------------------------------------------------------------

# How do we change direction? 

# all the segments of the snake need to be linked in such a way that if we change the argument for the setheading() function,
# only the first segment would be affected while the others would continue in the same direction and replace the segment in front of it.


# this practical solution would require us to rethink the way that the snake moves, 
# that is, the last segment should move to where the next segment is, and so on until the second segment moves to the first one's spot.
# until this design, segments would always turn with the "head" of the snake after each movement direction is triggered by the user key arrow keys.


# this code in the for-loop within the while-loop must be deleted:
for segment in segments:
        segment.forward(20)

# in its place, we need a for-loop that uses the range function with these keyword parameters in the function:
# with a start , stop, and step paraemeters.
# the arguments change based on how large of a range you want by their start and stop value, with the step parameter denote how you go from start to stop.
# ex: range from 3,2,1, would look like:
range(start = 3, stop = 1, step = -1)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    for segment in segments:
        segment.forward(20)

    for segment_number in range(start= 2, stop= 0, step= -1): # stop is 0 since we are stopping at postion 0 within a list (for the first item)

# BUT SURPRIIIIIISE THIS IS technically ACTUALLY C language CODE and not python, so it would yield an arrow. 
# the python version doesn't use these keyword arguments so it usually to write it off for mentally mapping out the code, but must be deleted before running.
# so we need to modify the code in a pretty clever way:

# the starting position, too ensure that the code is "dynamic" as the snake growths in segment count, we set the start the length of the segment list minus 1.
# this is minus one since the of course lists start counting at position 0.

# furthermore, the since the tuple is in a coordinate format, we can retrieve the data within each tuple and pass it as the new position for each segment ...
# by using the [seg_num -1].xcor() for the x and its y equivalent as shown below:
# segments are counting increasing from left to right so the one closest to the head is -1 the number is in the list of the current segment.

    for segment_number in range(len(segments) - 1, 0, -1):
        new_x = segments[segment_number - 1].xcor()
        new_y = segments[segment_number -1].ycor()
        segments[segment_number].goto(new_x, new_y)

# so far, all three segment just go to the same position. 
# we need to also move the first segment by 20 paces (across the )
# this line is place outside of the for-loop:

    for segment_number in range(len(segments) - 1, 0, -1):
        new_x = segments[segment_number - 1].xcor()
        new_y = segments[segment_number -1].ycor()
        segments[segment_number].goto(new_x, new_y)

    segment[0].forward(20)

#---------------------------------------------------------------------------------------------------------------------------

# all the code related to the snake's appearance and movement should be stored in its own class.
# by the end of the project, there will be three separate classes:
# 1. Snake 
# 2. Food
# 3. Scoreboard

# furthermore the code for these will be stored in separate files, so that the starting code for the program would look like:
from turtle import Screen
from snake import Snake
import time

# then once I initialize this snake, it will do everything laid out in the Snake class from the snake file:
snake = Snake()

# then the snake just continuous moved with a move() method that we will define 

# the code within the snake.py file looks like this:

from turtle import Turtle # needed for the create_snake() method

# starting positions will be stored as a constant, thus requiring its name in ALL_CAPS:
STARTING_POSITION = [(0,0), (-20, 0), (-40, 0)]

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

        def create_snake(self):
            for position in STARTING_POSITION:
                new_segment = Turtle("square")
                new_segment.color("white")
                new_segment.penup()
                new_segment.goto(position)
                self.segments.append(new_segment) #referring to our attribute "segments"

        def move(self):

            for segment_number in range(len(self.segments) - 1, 0, -1): #within a class,'segments' needs to have 'self.'
                new_x = self.segments[segment_number - 1].xcor()
                new_y = self.segments[segment_number - 1].ycor()
                self.segments[segment_number].goto(new_x, new_y)

            self.segments[0].forward(20)

#---------------------------------------------------------------------------------------------------------------------------

# so far with just the snake movement and appearance within the Snake class, the main.py looks like this:
from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake() # create an instance of snake that creates the initial 3 segments with starting positions and movement


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2) # delay the screen update by this amount of time (in seconds)
    snake.move()

screen.exitonclick()

# and the snake file looks like this:
from turtle import Turtle # needed for the create_snake() method
# starting positions will be stored as a constant, thus requiring its name in ALL_CAPS:
STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
# another constant needed to define how far the snake moves before the screen refreshes, being 20 paces:
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment) #referring to our attribute "segments"

    def move(self):

        for segment_number in range(len(self.segments) - 1, 0, -1): #within a class,'segments' needs to have 'self.'
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)

            self.segments[0].forward(MOVE_DISTANCE) # set to a constant that we can tweak at the top of this code


#---------------------------------------------------------------------------------------------------------------------------

# controling the snake using the up, down, left, and right arrow keys

# use key binding to be able to transalte these inputs into a change of direction

# class the screen.listen() method to listen for these key strokes that wil be describe up a strings

screen.listen()
screen.onkey("Up")
screen.onkey("Down")
screen.onkey("Left")
screen.onkey("Right")

# these need to be bound to a function defined in the snake class however that wil share the same name:

screen.listen()
screen.onkey(snake.up("Up"))
screen.onkey(snake.down("Down"))
screen.onkey(snake.left("Left"))
screen.onkey(snake.right("Right"))

# these newly defined methods for each direction must match the degree out of 360 that would correspond
# thus: up is 90, down is 270, left is 180, and right is 0.

def up(self):
    self.segments[0].setheading(90)

def down(self):
    self.segments[0].setheading(270)

def left(self):
    self.segments[0].setheading(180)

def right(self):
    self.segments[0].setheading(0)

# we need to create a separate attribute for the snake's, so that when it is initialized, the head is defined as being the segment at position 0.
# this way, when the direction of the snake is change, this affect the head of the snake, and the rest will of course follow as they move to where the next segment is.
# this also means that any instance where I used self.segments[0] in the snake file, I can replace those with self.head to make the code easier to read.
def __init__(self):
    self.segments = []
    self.create_snake()
    self.head = self.segments[0]

# and later with these changes:
def up(self):
    self.head.setheading(90)
def down(self):
    self.head.setheading(270)
def left(self):
    self.head.setheading(180)
def right(self):
    self.head.setheading(0)

# one more rule, the snake cnanot move back on its self.
# ie. if the snake is heading right (90) the user can't hit the left key to change direction to 180
# similarly, if going up can't go down and vice-versa, neither left if current direction(heading) is right
# at top of snake file we need more constants for each direction:
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# we also need to change the arguments for the up method and other direction to be set to the values of the direction constants like so:
# but first we need if statements to check our desired conditions
def up(self):
    if self.head.heading() != DOWN:
        self.head.setheading(UP)
def down(self):
    if self.head.heading() != UP:
        self.head.setheading(DOWN)
def left(self):
    if self.head.heading() != RIGHT:
        self.head.setheading(LEFT)
def right(self):
    if self.head.heading() != LEFT:
        self.head.setheading(RIGHT)
#---------------------------------------------------------------------------------------------------------------------------

# end of day 20 code for snake game, to be continued tomorrow:

# main.py file:

from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)

    snake.move()


screen.exitonclick()





# snake.py file (so far for day 20):

from turtle import Turtle 

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

# this is the end of day 20 for the snake game. day 21 will cover how to add the funcitonality of actually chasing the food and keeping score.
# there will also be a way to detect collision with the food AND the walls (border of the screen).




