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



