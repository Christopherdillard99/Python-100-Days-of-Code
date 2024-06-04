# Day 18: Turtle Graphics, Tuples, and Importing Modules:
# writing code to generate artwork (in a very modern, minimalist sense)
# creating randomized artwork with random colors dots.

# ----------------------------------------------------------------------------------

# Turtle Graphics Module: turtle
# this module is a way to add graphics onto a screen


# start with importing the Turtle class from the turtle module

from turtle import Turtle

# creating new object from the Turtle class

timmy_the_turtle = Turtle()

# creating a screen object from the Screen class to display new timmy_the_turtle object
# must also import Screen, modifying the previous code

from turtle import Turtle, Screen

screen=Screen()
screen.exitonclick() # existonclick() 

# learn how to use a module by reading the documentation. 
# using the shape() method to change to specified shape of "circle"

timmy_the_turtle.shape("circle")

# if I'm unsure about what each function does after reading the documentation, consult stackoverflow with a google search with some relevant terms
# the color() method is useful

timmy_the_turtle.color("red")
# t k color specification string with corresponding rgb number values. Tkinter tk for a Graphical User Interface (GUI).
# Tkinter color names here:
# https://trinket.io/docs/colors
# https://cs111.wellesley.edu/reference/colors

# for movement methods:
timmy_the_turtle.backward(200)
timmy_the_turtle.right(90) #takes a number between 0-360 to specify the angle it turns to. 
timmy_the_turtle.left(180)

# ----------------------------------------------------------------------------------

# Challenge 1: Creating a square using Turtle
# the long way:

from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")
timmy_the_turtle.forward(50)
timmy_the_turtle.left(90)
timmy_the_turtle.forward(50)
timmy_the_turtle.left(90)
timmy_the_turtle.forward(50)
timmy_the_turtle.left(90)
timmy_the_turtle.forward(50)
timmy_the_turtle.left(90)

screen = Screen()
screen.exitonclick()

# alternatively, and much simpler way using a for loop and range operator

for _ in range(4):
    timmy_the_turtle.forward(50)
    timmy_the_turtle.left(90)

# refactor and rename the turtle to tim so as not to type out timmy_the_turtle with each line of code.


# ----------------------------------------------------------------------------------

# Importing Modules:
# Basic imports
import turtle
# create object like:
tim = turtle.Turtle() # advantage more expressive, but more typing

from turtle import Turtle # this way you don't have to type turtle.Turtle() everytime

tim = Turtle()
tom = Turtle()
terry = Turtle()

# import everything by using the asterisk:
from turtle import *

# disadvantage can make it a little harder to see where every method comes from in isolation, which becomes more obvious when you import a specific class with from module import Class method.
# so, typically amazing code does not use the *

# how to alias module, 
# import turtle module as t that user defines
import turtle as t
tim = t.Turtle() # very helpful if the module's name is really long

# Some modules can't just be imported 
# turtle is a module that's packaged in the standard Python library

# if you want to access the whole world of python packages and libraries - go to the python library website to install module as needed

import heroes # this would show a squiggly red underline which alerts you that the module isn't install yet, or not part of the standard preloaded packages

print(heroes.gen()) # for reference, it generates a random hero name

# note, a package is only installed into your local environment and NOT global (ie not accessible across entire computer like a program)
# python 3.12 is not backward compatible with python 2.7
# virtual environments allow you to use certain package in little "sandboxes" for compatibility sake to freee a project in time and continue to run the program even if python changes version

# pip install is riskier since you might install the package into the wrong folder.

# ----------------------------------------------------------------------------------

# Draw a dashed line:
# line and gap for distance of 5 each, 10 times in total for the loop - essentially draw/no-draw
# penup() and pendown() to control whether the movement leaves a trail across the screen as the object moves. 
# these methods are in the "drawing control" section of the documentation

from turtle import Turtle,Screen

tim = Turtle()

tim.shape("turtle")
tim.color("green")

for _ in range(10):
  tim.forward(5)
  tim.penup()
  tim.forward(5)
  tim.pendown()

screen=Screen()
screen.exitonclick()

# ----------------------------------------------------------------------------------
# draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, and decagon. 
# each shape in a random color and overlayed ontop of each other. 
# each side will have a length of 100
# turn the direction (angle) of the pen by taking 360 degrees divided by the total number of sides for each shape:
# ie a square is 360 / 4 = 90 degree angles. Pentagon is 360 / 5 = 72 degree angles

# I created a custom list of color names, barring yellow since it doesn't show up well on the white background.
# I wanted the number of movements to be equal to the number of sides for each shape. 
# Once the number of moves reaches zero, then the number of sides is bumped up by 1 and a new random color is chosen.


from turtle import Turtle,Screen
import random

color_names = ['blue', 'green', 'pink', 'purple', 'chocolate', 'turquoise', 'orange', 'maroon', 'violet', 'magenta', 'cyan', 'navy']

tim = Turtle()
sides = 3
moves = sides
tim.color(random.choice(color_names))

while sides != 11:
  for _ in range(moves):
    tim.forward(100)
    tim.left(360/sides)
    moves -= 1
    if moves == 0:
      sides += 1
      moves = sides
      tim.color(random.choice(color_names))
    
screen=Screen()
screen.exitonclick()


# Angela Yu's version of the code:
import turtle as t
import random

tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 10):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)


# ----------------------------------------------------------------------------------
# Challenge: making the turtle go on a random walk and each time the turtle walks, a new random color will be chosen
# changing the thickness of the path and controlling the speed

import turtle as t
import random

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

directions = [0,90,180,270]


tim = t.Turtle()
tim.pensize(15)
tim.speed("fastest")

for i in range(40):
  tim.color(random.choice(colors))
  tim.forward(random.randint(15,25))
  tim.setheading(random.choice(directions))

# ----------------------------------------------------------------------------------
# now, randomly generate colors instead of selecting named colors from a list:

# this new method generates an RGB color, represented by the tuple r, g, b
# red, green, and blue
# Python Tuples ex:
(1, 3, 8)

# this resembles a list in that:
my_tuple = (1, 3, 8)

my_tuple[0] # can access the index, where 0 is ofc the first item in the tuple

# unlike a list, a tuple's values cannot be altered 
my_tuple[2] = 12 # this would yield a TypeError since 'tuple' object does not support item assignment.

# Immutable - the quality of not being able to be change or mutated. 

# uniform color schemes or things you don't want to be accidentally changed. 
# if you decided you want to edit the tuple, just turn it into a list:
list(my_tuple)

# RGB Calculator

# all colors go from 0 to 255, with 3 primary colors eing red, green, blue.

# tap into turtle module and change the color mode from zero to 255 like so:
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
directions = [0,90,180,270]

def random_color():
   '''generates random number between 0 and 255 for RGB color'''
   r = random.randint(0,255)
   g = random.randint(0,255)
   b = random.randint(0, 255)
   random_color = (r, g, b)
   return random_color
   
for i in range(200):
   tim.color(random_color())
   tim.forward(30)
   tim.setheading(random.choice(directions))

# ----------------------------------------------------------------------------------
# Making a Spirograph
# draw a ton of circles with radii of 180
# random colors for each subsequent circle
# must slightly change the tilt of the circle each time.

# from the documentation:
# turtle.circle(radius, extent=None, steps=None)¶
# Parameters:
# radius – a number

# extent – a number (or None)

# steps – an integer (or None)

# Draw a circle with given radius. The center is radius units left of the turtle; extent – an angle – determines which part of the circle is drawn.
# If extent is not given, draw the entire circle. If extent is not a full circle, one endpoint of the arc is the current pen position. 
# Draw the arc in counterclockwise direction if radius is positive, otherwise in clockwise direction. 
# Finally the direction of the turtle is changed by the amount of extent.

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
directions = [0,90,180,270]

def random_color():
   '''generates random number between 0 and 255 for RGB color'''
   r = random.randint(0,255)
   g = random.randint(0,255)
   b = random.randint(0, 255)
   random_color = (r, g, b)
   return random_color


tim = t.Turtle()
tim.speed("fastest")

for i in range(100):
    tim.circle(100)
    tim.color(random_color())
    current_heading = tim.heading()
    tim.setheading(current_heading + 10)

screen=t.Screen()
screen.exitonclick()


# a spirograph must end eventually
# so, an arbitrary varlue for the range in the for loop could actually be simplified
# by mathematically working out the exact necessary number of new circles using 360 degrees and the size of the gap between each circle's line.
# the size_of_gap is up to the user to decide how closely they want each circle to be drawn.

# this can be done by storing the entire spirograph into a function that takes the size_of_gap as a parameter.
# the for loop in this case take 360 degrees divided by the size_of_gap like so:

def create_spirograph(size_of_gap):
   for i in range(int(360/size_of_gap)):
      tim.color(random_color())
      tim.circle(100)
      tim.setheading(tim.heading() + size_of_gap)

create_spirograph(5)


# so, the final Spirograph code is:

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
directions = [0,90,180,270]

def random_color():
   '''generates random number between 0 and 255 for RGB color'''
   r = random.randint(0,255)
   g = random.randint(0,255)
   b = random.randint(0, 255)
   random_color = (r, g, b)
   return random_color


tim = t.Turtle()
tim.speed("fastest")

def create_spirograph(size_of_gap):
   for i in range(int(360/size_of_gap)):
      tim.color(random_color())
      tim.circle(100)
      tim.setheading(tim.heading() + size_of_gap)

create_spirograph(5)

screen=t.Screen()
screen.exitonclick()

# ----------------------------------------------------------------------------------

# created a modern/contemporary art piece using Python's turtle graphics
# based on how Damien Hirst sold his piece Antipyrylazo III for £1,275,000
# https://www.phillips.com/detail/damien-hirst/UK010120/16

# I will be using the package, colorgram
# https://pypi.org/project/colorgram.py/

# colorgram.py is a Python library that lets you extract colors from an image.
# this way, you get a palette based on the colors in the image.

import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('sweet_pic.jpg', 6)

# colorgram.extract returns Color objects, which let you access
# RGB, HSL, and what proportion of the image was that color.
first_color = colors[0]
rgb = first_color.rgb # e.g. (255, 151, 210)
hsl = first_color.hsl # e.g. (230, 255, 203)
proportion  = first_color.proportion # e.g. 0.34

# RGB and HSL are named tuples, so values can be accessed as properties.
# These all work just as well:
red = rgb[0]
red = rgb.r
saturation = hsl[1]
saturation = hsl.s

colorgram.extract(image, number_of_colors) # the two inputs are the image and number of colors.

# Extract colors from an image. image may be either a path to a file, a file-like object, or a Pillow Image object. The function will return a list of number_of_colors Color objects.

colorgram.Color

# A color extracted from an image. Its properties are:

# Color.rgb - The color represented as a namedtuple of RGB from 0 to 255, e.g. (r=255, g=151, b=210).

# Color.hsl - The color represented as a namedtuple of HSL from 0 to 255, e.g. (h=230, s=255, l=203).

# Color.proportion - The proportion of the image that is in the extracted color from 0 to 1, e.g. 0.34.



# in this project, I'll be taking one of Damien Hirst's art piece from google images and downloading the image to then extract the exact colors.
# simple search of "Damien Hirst Spots"
# https://media.cnn.com/api/v1/images/stellar/prod/200430102527-01-damien-hirst-severed-spots.jpg?q=w_2000,c_fill

# drag and drop the image file into the .venv folder (same indentation level as the main.py file). rename to "image.jpg" if desired.


# 1. install the package in PyCharm. 
# go to settings on top right (windows version). then go down to the name of the project file and select it. then click on the plus button to install the colorgram package after searching for it.

import colorgram

colors = colorgram.extract("image.jpg", 30)

print(colors)

# the list of colors returns different types of colors. need a for loop to tap into each color and create a new list with only rgb colors.

rgb_colors = []
colors = colorgram.extract("image.jpg", 30)
for color in colors:
   rgb_colors.append(color.rgb)

print(rgb_colors)

# ACTUALLY, to be usable for the turtle graphics, each element of the rbg color needs to be stored in its own variable r, g, and b like so:

rgb_colors = []
colors = colorgram.extract("image.jpg", 30)
for color in colors:
   r = color.rgb.r
   g = color.rgb.g
   b = color.rgb.b
   new_color = (r, g, b) #creating new tuple
   rgb_colors.append(new_color) # appending each newly created rgb tuple to the empty list

print(rgb_colors)

[(252, 250, 247), (253, 247, 249), (237, 251, 245), (249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155)]

# colors are sampled by frequency of occurrence in the image.
# note that numbers that closer to 255 tend to be whiter (an rgb of 255,255,255 is completely white), and thus less useful for this project since they are most likely background photos and not spots.

# checked on this website:
# https://www.rapidtables.com/web/color/RGB_Color.html

# these first three initially colors were eliminated from the list:
(252, 250, 247), (253, 247, 249), (237, 251, 245)


# now, the list is saved to the main.py as color_list() and the previous lines of code can be commented out

color_list = [(249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155)]

# ----------------------------------------------------------------------------------

# requirements for the project
# spots will be on a grid of 10 x 10.
# spot size is 20 and distance is 50 paces apart.

import turtle as turtle_module

tim = turtle_module.Turtle()



# creating dot, takes two parameters for sixe and color
# must get the turtle to change its color mode to 255 so that it can interpret correctly the rgb format
turtle_module.colormode(255)

# also, import and use random module to select random color
import random

tim.dot(20, random.choice(color_list))


# always place this next line of code at the end of the program instead of at the top, otherwise it will show a blank screen.
screen = turtle_module.Screen()
screen.exitonclick()

# now, to ensure that the process can be repeated to fill the 10 x 10 requirement:
# we need the starting dot to be in the bottom left of the screen AND there shouldn't be a line tracing between each dot

# by default, the turtle starts in the center of the screen.
# the code must ensure that the turtle moves to a good starting point and doesn't start drawing dots until it is in that spot and facing the right direction

tim.setheading(225) #think 225 out of 360 degrees from a default of facing right on the screen to now facing "south-west"
tim.forward(300) # 300 paces towards the south-west ends up in a good starting point
tim.setheading(0) # now, the turtle is facing right again at 0 degrees. 

# for-loop to place a random-colored spot ever 50 paces heading towards the screen across the screen.

for i in range(10):
   tim.dot(20, random.choice(color_list))
   tim.forward(50)

# once the first row is drawn, the turtle needs to change directions and move back across to align with the very first spot (50 paces above the left-most spot above the first row)
# this way the turtle will draw always from left to right.
# same as saying face up/north, go 50 paces, turn left by facing west and go 500 paces (10 x 50 paces) then turn around to fast east/forward (setheading(0))
# this code block is then placed inside the previous for-loop

tim.setheading(90)
tim.forward(50)
tim.setheading(180)
tim.forward(500)
tim.setheading(0)


# now, instead of a range of 10, the range is form 1 to 100. create a new variable and assign 100.
# replce i in for-loop with something useful like dot_count to keep track until the count reaches 100 loops.

number_of_dots = 100

for dot_count in range(1,100):
   tim.dot(20, random.choice(color_list))
   tim.forward(50)

   # this next step with a modulo sign check wether the dot count is 10, 20, 30, 40, etc. to then start on the next row until 100.
   if dot_count % 10 == 0:
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)


# use penup() to ensure that only the dots are drawn.
# also, control the turtle's (ie the arrow's) visibility with hideturtle()

# ----------------------------------------------------------------------------------

# so, to re-cap. This is the entire code where the first part to extract colors from the image is commented out after colors are saved to a list as rgb tuples:



# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)
# for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b) #creating new tuple
#    rgb_colors.append(new_color) # appending each newly created rgb tuple to the empty list
#
# print(rgb_colors)

import turtle as turtle_module
import random

color_list = [(249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155)]


tim = turtle_module.Turtle()
tim.speed("fastest")
turtle_module.colormode(255) # setting color mode to 255 is necessary to accurately use the rgb tuples
tim.penup() # this makes it so no line is show connecting each shape
tim.hideturtle() # the arrow, or any assigned shape for the turtle, is not shown on the screen

tim.setheading(225) # turtle initially moves away form the exact screen centerpoint towards "south-west", essentially 225 / 360 degrees where 0 is facing forward/east.
tim.forward(300) # 300 paces away from the center in this direction of 225.
tim.setheading(0) # the heading is set back to default, facing forward towards the right of the screen.

number_of_dots = 100 # the artwork is 10 x 10 dots

for dot_count in range(1,number_of_dots + 1): # range must be 1 more than the number of dots to include that number
   tim.dot(20, random.choice(color_list)) # the dot method takes two parameters for size and color.
   tim.forward(50) #the dots in each row should be 50 paces apart

   # this next step with a modulo sign check wether the dot count is 10, 20, 30, 40, etc. to then start on the next row until 100.
   if dot_count % 10 == 0:
    tim.setheading(90) # next 5 lines of code take the turtle back to the left side of the screen to start another row 50 paces above the very first dot.
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

screen = turtle_module.Screen() # these last two lines must be at the end so that the screen playsback happening in the code. If placed at the beginning, it would show a blank screen.
screen.exitonclick() # this way, the screen doesn't automatically dissapear once the drawing is done and also let you quickly exit without having to watch the whole animation if you spot an error.
