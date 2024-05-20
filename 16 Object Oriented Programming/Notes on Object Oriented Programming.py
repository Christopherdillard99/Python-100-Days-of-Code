# Day 16: Object Oriented Programming (OOP):

# Procedural Programming: 
# In an order that sets up functions to do particular things and then one procedure leads to another
# works from top to bottom - one of the earliest paradigms of programming

# Increasing complexity and number ofrelationships to manage can become confusing.
# this is where Object Oriented Programming is handy:
# Think of self driving car. 
# break it into different components and what exactly is a self driving car - cameras, lane detections, some navegation system, some fuel management, etc...

# now think of these different components as "modules". each module fulfills a specific task. 
# best of all is all these module are reusable for future projects.
# so, modularize your code to simplify projects and split larger task into smaller pieces (modules), which become reusable if you need this same functionality in the future.

# manage relationships in the code using module to carry out different tasks.


# --------------------------------------------------------------------------------------------------------------------

# now implement OOP paradigm with the following thought process:

# Think about about in a restaurant, module could be waiter, chef, and bartender.
# now try to imagine what the wait has and what the waiter does.

# has would be:
is_holding_plate = True
tables_responsible = [4, 5, 6]

#now, what doees the waiter do:
def take_order(table, order):
    #takes order to the chef

def take_payment(amount):
    #adds money to the restaurant


# now in programming lingo, the object = waiter, attributes = has, and methods = does.
# a method is a function that a particular moduled object does.

# once a job like a waiter is modules, we can generate multiple versions of the same object blueprint.

# class is the blueprint, and the object are the unique versions of the class.
# the class would be waiter, and then different waiters like "billy" and "bob" would be refered to as objects.

# --------------------------------------------------------------------------------------------------------------------

# syntax for creating objects from classes:
# think of different car modules being created from a car blueprint that contains standard specs for mileage, number of wheels, number of doors...

# classes are typically written with first letter of each word capitalized (Pascal Case):
# ** variable and function names follow the underscore format separating each word, by contrast**
# car is object and CarBlueprint is the class:

car = CarBlueprint()

# --------------------------------------------------------------------------------------------------------------------

# Now lets think about the Turtle Graphics library this is preloaded with Python.
the code used throughout this file while follow the turtle module in Python will some examples spaced in between each step.
# so, it may come off as confusing since I was learning simulaneously within different windows in the PyCharm IDE ... pay careful attention to the comments.
# this link will direct you to the Turtle Graphics Documentation for more info https://docs.python.org/3/library/turtle.html
# also, searching PyPi (the python package index) to find packages written by other developers.

# Procedural Programming: 
# In an order that sets up functions to do particular things and then one procedure leads to another
# works from top to bottom - one of the earliest paradigms of programming

# Increasing complexity and number ofrelationships to manage can become confusing.
# this is where Object Oriented Programming is handy:
# Think of self driving car. 
# break it into different components and what exactly is a self driving car - cameras, lane detections, some navegation system, some fuel management, etc...

# now think of these different components as "modules". each module fulfills a specific task. 
# best of all is all these module are reusable for future projects.
# so, modularize your code to simplify projects and split larger task into smaller pieces (modules), which become reusable if you need this same functionality in the future.

# manage relationships in the code using module to carry out different tasks.


# --------------------------------------------------------------------------------------------------------------------

# now implement OOP paradigm with the following thought process:

# Think about about in a restaurant, module could be waiter, chef, and bartender.
# now try to imagine what the wait has and what the waiter does.

# has would be:
is_holding_plate = True
tables_responsible = [4, 5, 6]

#now, what doees the waiter do:
def take_order(table, order):
    #takes order to the chef

def take_payment(amount):
    #adds money to the restaurant


# now in programming lingo, the object = waiter, attributes = has, and methods = does.
# a method is a function that a particular moduled object does.

# once a job like a waiter is modules, we can generate multiple versions of the same object blueprint.

# class is the blueprint, and the object are the unique versions of the class.
# the class would be waiter, and then different waiters like "billy" and "bob" would be refered to as objects.

# --------------------------------------------------------------------------------------------------------------------

# syntax for creating objects from classes:
# think of different car modules being created from a car blueprint that contains standard specs for mileage, number of wheels, number of doors...

# classes are typically written with first letter of each word capitalized (Pascal Case / Pascal Casing):
# ** variable and function names follow the underscore format separating each word, by contrast**
# car is object and CarBlueprint is the class:

car = CarBlueprint()

# --------------------------------------------------------------------------------------------------------------------

# Accessing the attributes from an object (what the object "has"):
# the syntax here is import as in this case:

# object is named car.
# it has two attributes
speed = 0
fuel = 32

# now to get the speed of the car, I must write:

car.speed

# --------------------------------------------------------------------------------------------------------------------

# Now lets think about the Turtle Graphics library this is preloaded with Python.

import another_module

print(another_module.another_variable)

# so, the module is turtle and the variable Turtle:

import turtle

# timmy = turtle.Turtle()

# alternatively, this code above can be written as

from turtle import Turtle
timmy = Turtle()
print(timmy)

# another class in this turtle module is called Screen
# this represents the window in which the Turtle is going to show up

# so after having imported turtle module by modifying the previous block of code with a comma separator for the additional class:
from turtle import Turtle, Screen

my_screen = Screen()
print(my_screen.canvheight)

# --------------------------------------------------------------------------------------------------------------------

# Now onto what an object does with the car example, its methods:
# functions that are tied to an object are none as the methods.


def move():
    ''' accelerates the car so that is speed rises to 60'''
    speed = 60

def stop():
    ''' stops the car by reducing its speed to 0'''
    speed = 0

# to access a method, tap into the object using a period separator (dot notation) 

car.stop()

# --------------------------------------------------------------------------------------------------------------------

# there is a method (function) available in turtle module that will maintain the window option and only close if it detects a click
# with the create my_screen object I call this method like so:

my_screen.exitonclick() 

# the previously created timmy object can now be change to an actual turtle instead of the default right-facing arrow like so:

timmy.shape("turtle")

# --------------------------------------------------------------------------------------------------------------------

# I can also change the color of the turtle by using the color() method and passing the name of the colors as a string.

# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
timmy.color("chartreuse2", "chocolate4")

# --------------------------------------------------------------------------------------------------------------------

# moving the turtle foward 100 places:
# there are many different functions associated with movement in turtle but use forward(distance) where distance is the parameter as a number (integar or float)

timmy.forward(100) # specify timmy object, call the forward method and enter the parameter for distance of 100.

# --------------------------------------------------------------------------------------------------------------------

# now calling a wide range of packages and libraries already created, read the blueprints and documentations:
# this way I can use code that other developers have written. - adding an external library to the project

# inegrating existing code into my current projects. 
# packages are larger files of modules and files to achieve a purpose.

# search for packages written by other developers on PyPi (the Python Package Index)

# PrettyTable is a library that was created to help display tables in ASCII format.
# on left-hand side click on the project links for the homepage to see more about the project and navegated to the google code archive where the documentation is hosted.
# https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki

# first things first, you must install the packages found on PyPi within PyCharm or whatever IDE I'm using.
# in PyCharm (windows version) this is enabled by going to file and setting.  
# now go to the project and enter the project interpreter.
# click on the plus button to install any package I find within the PyPi, by searching for its name.

# next step is simply importing the table within the code editor pane with all the other code

import prettytable

# to see the source code, right click on the package name from the line above, hover over "go to" and then select "implementation" from the options. 

# --------------------------------------------------------------------------------------------------------------------

from prettytable import PrettyTable

# create an object from the PrettyTable class called "table"

table = PrettyTable()

# a print statement right now will show an empty table: 

print(table)

++
||
++
++

# from documentation on google code archive for prettytable
# add data like columns:
x = PrettyTable() 
x.add_column("City name",["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"]) 
x.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386]) x.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092, 1554769]) 
x.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9, 869.4])

# the add column function allows the user to add a field name for the column header and then enter the data as a string of text, numbers, or floats.

# now using Pokemon theme to create ASCII table:
# reference this data: https://pokemondb.net/pokedex/game/x-y

pokemon_table = PrettyTable() 
pokemon_table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"]) 
pokemon_table.add_column("Type", ["Electric", "Water", "Fire"])

print(pokemon_table)

+--------------+----------+
| Pokemon Name |   Type   |
+--------------+----------+
|   Pikachu    | Electric |
|   Squirtle   |  Water   |
|  Charmander  |   Fire   |
+--------------+----------+

# furthermore, changing the appearance of the table would be done using an attribute 
# alignment with align attribute for "l" left "r" right, center aligned is default in prettytable package

pokemon_table.align = "l"
print(pokemon_table)

+--------------+----------+
| Pokemon Name | Type     |
+--------------+----------+
| Pikachu      | Electric |
| Squirtle     | Water    |
| Charmander   | Fire     |
+--------------+----------+


# --------------------------------------------------------------------------------------------------------------------

# Mini Quiz:

# 1. In OOP (Object-Oriented Programming), what is the name of the blueprint for creating objects?
# correct answer: class

# 2. Given a Class blueprint for a Car has the following attributes and methods, which line of code in the answers will produce an error?
#Attributes:
num_of_seats
speed
# Methods:
drive()
brake()

car.drive()
car.num_of_seats = 2
car.brake() = 0 # this causes an error since the value of 0 must be placed within the parentheses for the brake() methods argument.
print(car.speed) 

# 3. What word would you use to describe what's inside my_toyota and my_fiat?
my_toyota = Car()
my_fiat = Car()

# answer: object. my_toyota and my_fiat are variables and each contains a Car object.








