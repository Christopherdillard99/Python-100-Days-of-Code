# Day 21: Inheritance, Slicing, and Finishing the Snake Game

# NOTE: Important Concept for Object Oriented Programming, being: Class Inheritance

# Class Inheritance is the idea that classes can inherit from other classes.
#           - classes can inherit things like methods, attributes
#           - makes it simpler to modify and give them more capabilities


# Also, Python allows you to slice lists and dictionaries

# ------------------------------------------------------------------------------------

# What is on the agenda today to complete the Snake Game?

        # 1. Detect collision with food
        # 2. Create a scoreboard
        # 3. Detect collision with wall 
        # 4. Detect collision with tail

# ------------------------------------------------------------------------------------

# Class Inheritance:

# Ex: Imagine you are creating a restaurant and need to make a class called Chef

# Chef needs methods to bake() stir() and measure()

# then, you decide you also need a Pastry Chef at one point:
# this Pastry Chef needs same things as normal chef PLUS some others like knead() and whisk()

# so, this idea of taking some of the same functionality and appearance from one class to create another is called Class Inheritance
# you can inheritant appearance (attributes) and behavior (methods)

# Ex: Creating a Fish class that needs to inherit some attributes and methods from the Animal class:
# need to add the original class that want to inherit from after the new Class name like so:
# in this example using super().__init__() within the Fish class init line:
# this means that all the attributes and methods are passed down to the new Fish class.

class Fish(Animal):
    def __init__(self):
        super().__init__()

# ------------------------------------------------------------------------------------
# real code example of this concept:
# creating Animal class with initializer to define some methods and attributes:
# Fish class now has all the inited methods and attributes from the Animal super class

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("moving in the water.")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)

# now, let's say I wanted to modify one of the methods that I am inheriting from the Animal class
# in this case I want the change the breathing since it would be a little different under water
# here the breathe method with keep the original functionality, WITH AN ADDED print statement.

class Fish(Animal):
    def __init__(self):
        super.__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in the water.")

# ------------------------------------------------------------------------------------

# Small 3-Question Quiz on Class Inheritance:

# 1. Given the following:

    class Dog:
        def __init__(self):
            self.temperament = "loyal"
    
        def bark(self):
            print("Woof, woof!")

#  How do you create a class called Labrador (the subclass) that inherits from the Dog class (the superclass)?

    class Labrador(Dog):
        def __init__(self):
            self.temperament = "friendly"
# NOTE: The call to super() in the initialiser is recommended, but not strictly required.

# 2. Given this:

    class Dog:
        def __init__(self):
            self.temperament = "loyal"
    
    class Labrador(Dog):
        def __init__(self):
            super().__init__()
            self.temperament = "gentle"

# What will this code print?

    doggo = Dog()
    print(f"A dog is {doggo.temperament}")
    
    sparky = Labrador()
    print(f"Sparky is {sparky.temperament}")

# Answer:
# a dog is loyal
# Sparky is gentle

# 3. Given this code:

    class Dog:
        def __init__(self):
            self.temperament = "loyal"
    
        def bark(self):
            print("Woof, woof!")
    
    class Labrador(Dog):
        def __init__(self):
            super().__init__()
            self.is_a_good_boy = True
    
        def bark(self):
            super().bark()
            print("Greetings, good sir. How do you do?")


# What will this print?

sparky = Labrador()
sparky.bark()

# Answer:
# Woof, woof!
# Greetings, good sir. How do you do?

# ------------------------------------------------------------------------------------

# Next Step in Snake game:

# Detect collision with food
# I need a new food symbol to spawn on the screen once the head of the game touches the food

# Remember: everything to do with snake appearance and behavior is captured inside a class "Snake"
# what i want to do is create a new food.py file that contains it's own Food class
# it will render itself as a small dot on the screen (that is a turtle object that looks like food) and then randomize a spawn location if the snake touches it

# I want the new Food class to inherit all the capabilities of the Turtle class from the turtle module like so
# in the new food.py file:
# I want the shape to be circular,
#  the object will be stretched along it's length and width by 0.5 to make it smaller 
# and the pen will be up to not trace a line as it moves.
# color will be blue 
# speed will be fastest
# use goto to make it go to random location using the random module
# x axis goes from -300 to +300 and y axis goes from -300 to +300.
# don't want the food to spawn right next to the wall since that would be wayyyyy too difficult
# so the x and y random.randint ranges will go from (-280, 280)

from turtle import Turtle

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

# NOTE: I now need to add a line to initialize the food object in the main.py file right after the line where the snake object is initialized
# NOTE 2: Need to also go a hold of the food class by adding from food import Food at the top of the main.py file
# I will check whether the distance between the head and the food is less than 15 pixels. This is because the head is 10x10 pixels so collision.
# given the head size and screen refresh rate, collision is pretty much guaranteed if the head comes within 15 pixels of the food object.
# Now, I want to detect collision between the snake and food and then generate a new random spot for the food if this condition is met
# this will be done in the main.py within the while loop using a method from the Turtle class called "distance"
# the distance method works by comparing the distance from turtle to whatever it is you point inside the parentheses
# you can either put an x and y coordinates OR you can compare your turtle to another turtle instance, this case being the food object

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        print("nom, nom, nom")


# now, I need to create a new method, called "Refresh"
# this will respawn the food object to a new spot if collision is detected
# this refresh() method also needs to be called when the food is initialized

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

# now, the main.py file will detect collision, but instead of printing "nom, nom, nom",
# if collision is detected, the refresh() method is called to generate a new random spawn point for the blue food object.

# ------------------------------------------------------------------------------------

# Now, Create a Scoreboard and Keep Score

# The scoreboard needs to write some text in the program so that it keeps track of the score for how many pieces of food the snake eats.
# it needs to increase everytime you hit a piece of Food - it will update and keep updating after each impact
# the scroe board also needs to be a turtle object using the write() method from the documentation:

turtle.write(arg,move=False, align="left",font=(Ärial),8,"normal"))

# Parameters:

# arg - object to be written to the TurtleScreen
# move - True/False
# align - one of the strings "left","center", or "right"
# font - a triple - triple tuple ("fontname", fontsize, "fonttype")

# you would call this write method like so:

turtle.write("Home = ", True, align="center")
turtle.write((0,0),True)

# ------------------------------------------------------------------------------------

# We can get the turtle to write a line of text using the write method --> turtle.write(arg, move=False, align="left", font=("Arial",8,"normal"))
# Need to create a new file called scroeboard.py
# create a new scoreboard class that will inherite from the turtle class. 
# it must know how to track the score and increase by one everytime the snack hits the food, as well as display it in the program, each time the turtle objects heads touches the food object, then the score increases by one
# turtle.clear() can be used to clear the write everything the score updates.


# Entered into the scoreboard.py file:

from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup() # this way the object does not trace the movement to the center top of the screen
        self.goto(0, 270)  # this way the scoreboard is at the center top of the screen
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, normal))
        self.hideturtle()

    # Now creating a function to increase the score:
    def increase_score(self):
        self.score += 1
        self.write()

# Now I need to go back into the main.py file and create a scoreboard object from the scoreboard class, after importing it into the main.py file using the following lines where applicable:
# ensure that the color of the scoreboard object is white (or any other visible color) if the background for the game's popup is black

# Modified the piece of the game that detects collision with food to also increase the score (at the very bottom):
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()

# Modified the text so that the scoreboard actually looks good instead of just printing ontop of itself with every increase in the score 
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup() # this way the object does not trace the movement to the center top of the screen
        self.goto(0, 270)  # this way the scoreboard is at the center top of the screen
        self.hideturtle()
        self.update_scoreboard()

    # create function so that the scoreboard object is now just printed on top of itself everytime the score increase
    # this function must delete the previous instance and only show the most recent with the right score
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, normal))

    # Now creating a function to increase the score:
    def increase_score(self):
        self.score += 1
        self.clear() # this will clear the previous instance of the scoreboard
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, normal))

# now instead of hardcoding the inputs for:
self.write(f"Score: {self.score}", align="center", font=("Arial", 24, normal))
#we can set constants at the top and just enter these in the function, so that we can easily change the style across the whole game if these inputs are in multiple functions, instead of searching line-by-line

from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, normal) # as a tuple

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup() # this way the object does not trace the movement to the center top of the screen
        self.goto(0, 270)  # this way the scoreboard is at the center top of the screen
        self.hideturtle()
        self.update_scoreboard()

    # create function so that the scoreboard object is now just printed on top of itself everytime the score increase
    # this function must delete the previous instance and only show the most recent with the right score
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)


# Now I just need to add some code that will detect collision with the walls of the game
# the edge itself is at 300 pixels to the right, bottom, left, and top of the center point,
# So I need to set the boundary to about 280 due to the snake head's size

# in main.py
if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    game_is_on = False

# in the scoreboard.py file, enter this code for a new function:

def game_over(self):
    self.goto(0, 0)  # I don't want this to appear on the same spot as the scoreboard
    self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)


# So far, the code looks like this in the main,py file. All that is left is to add some code to detect when the head of the snake collides with the tail/body:

from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        scoreboard.game_over()


screen.exitonclick()

# Now to detect head collision with tail/body. Upon collision, the game is over. A new segment will be added to the snake after each point is score (ie the head of the snake collide with the good object):
# add this chunk in the snake.py file

# Ehances this:
 def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("green")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)


# Changing that ^ to:

# create a function called add_segment and modify the code chunk from before with the for loop:

def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

def add_segment(self, position):
    new_segment = Turtle("square")
    new_segment.color("green")
    new_segment.penup()
    new_segment.goto(position)
    self.segments.append(new_segment)

def extend(self):
    #add a segment to the snake
    self.add_segment(self.segment[-1].position()) #this will add a segment to the last one in the tail, essentially starting backwards, hence the negative sign, getting the position of the last segment

# now, this extend() function needs to be added to the main.py file for the chunk that deals with detecting collision with food

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()


# Now to detect any collision with the tail
# Day 21: Inheritance, Slicing, and Finishing the Snake Game

# NOTE: Important Concept for Object Oriented Programming, being: Class Inheritance

# Class Inheritance is the idea that classes can inherite from other classes.
#           - classes can inheritance things like methods, attributes
#           - makes it simpler to modify and give them more capabilities


# Also, Python allows you to slice lists and dictionaries

# ------------------------------------------------------------------------------------

# What is on the agenda today to complete the Snake Game?

        # 1. Detect collision with food
        # 2. Create a scoreboard
        # 3. Detect collision with wall 
        # 4. Detect collision with tail

# ------------------------------------------------------------------------------------

# Class Inheritance:

# Ex: Imagine you are creating a restaurant and need to make a class called Chef

# Chef needs methods to bake() stir() and measure()

# then, you decide you also need a Pastry Chef at one point:
# this Pastry Chef needs same things as normal chef PLUS some others like knead() and whisk()

# so, this idea of taking some of the same functionality and appearance from one class to create another is called Class Inheritance
# you can inheritant appearance (attributes) and behavior (methods)

# Ex: Creating a Fish class that needs to inherit some attributes and methods from the Animal class:
# need to add the original class that want to inherit from after the new Class name like so:
# in this example using super().__init__() within the Fish class init line:
# this means that all the attributes and methods are passed down to the new Fish class.

class Fish(Animal):
    def __init__(self):
        super().__init__()

# ------------------------------------------------------------------------------------
# real code example of this concept:
# creating Animal class with initializer to define some methods and attributes:
# Fish class now has all the inited methods and attributes from the Animal super class

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("moving in the water.")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)

# now, let's say I wanted to modify one of the methods that I am inheriting from the Animal class
# in this case I want the change the breathing since it would be a little different under water
# here the breathe method with keep the original functionality, WITH AN ADDED print statement.

class Fish(Animal):
    def __init__(self):
        super.__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in the water.")

# ------------------------------------------------------------------------------------

# Small 3-Question Quiz on Class Inheritance:

# 1. Given the following:

    class Dog:
        def __init__(self):
            self.temperament = "loyal"
    
        def bark(self):
            print("Woof, woof!")

#  How do you create a class called Labrador (the subclass) that inherits from the Dog class (the superclass)?

    class Labrador(Dog):
        def __init__(self):
            self.temperament = "friendly"
# NOTE: The call to super() in the initialiser is recommended, but not strictly required.

# 2. Given this:

    class Dog:
        def __init__(self):
            self.temperament = "loyal"
    
    class Labrador(Dog):
        def __init__(self):
            super().__init__()
            self.temperament = "gentle"

# What will this code print?

    doggo = Dog()
    print(f"A dog is {doggo.temperament}")
    
    sparky = Labrador()
    print(f"Sparky is {sparky.temperament}")

# Answer:
# a dog is loyal
# Sparky is gentle

# 3. Given this code:

    class Dog:
        def __init__(self):
            self.temperament = "loyal"
    
        def bark(self):
            print("Woof, woof!")
    
    class Labrador(Dog):
        def __init__(self):
            super().__init__()
            self.is_a_good_boy = True
    
        def bark(self):
            super().bark()
            print("Greetings, good sir. How do you do?")


# What will this print?

sparky = Labrador()
sparky.bark()

# Answer:
# Woof, woof!
# Greetings, good sir. How do you do?

# ------------------------------------------------------------------------------------

# Next Step in Snake game:

# Detect collision with food
# I need a new food symbol to spawn on the screen once the head of the game touches the food

# Remember: everything to do with snake appearance and behavior is captured inside a class "Snake"
# what i want to do is create a new food.py file that contains it's own Food class
# it will render itself as a small dot on the screen (that is a turtle object that looks like food) and then randomize a spawn location if the snake touches it

# I want the new Food class to inherit all the capabilities of the Turtle class from the turtle module like so
# in the new food.py file:
# I want the shape to be circular,
#  the object will be stretched along it's length and width by 0.5 to make it smaller 
# and the pen will be up to not trace a line as it moves.
# color will be blue 
# speed will be fastest
# use goto to make it go to random location using the random module
# x axis goes from -300 to +300 and y axis goes from -300 to +300.
# don't want the food to spawn right next to the wall since that would be wayyyyy too difficult
# so the x and y random.randint ranges will go from (-280, 280)

from turtle import Turtle

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

# NOTE: I now need to add a line to initialize the food object in the main.py file right after the line where the snake object is initialized
# NOTE 2: Need to also go a hold of the food class by adding from food import Food at the top of the main.py file
# I will check whether the distance between the head and the food is less than 15 pixels. This is because the head is 10x10 pixels so collision.
# given the head size and screen refresh rate, collision is pretty much guaranteed if the head comes within 15 pixels of the food object.
# Now, I want to detect collision between the snake and food and then generate a new random spot for the food if this condition is met
# this will be done in the main.py within the while loop using a method from the Turtle class called "distance"
# the distance method works by comparing the distance from turtle to whatever it is you point inside the parentheses
# you can either put an x and y coordinates OR you can compare your turtle to another turtle instance, this case being the food object

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        print("nom, nom, nom")


# now, I need to create a new method, called "Refresh"
# this will respawn the food object to a new spot if collision is detected
# this refresh() method also needs to be called when the food is initialized

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

# now, the main.py file will detect collision, but instead of printing "nom, nom, nom",
# if collision is detected, the refresh() method is called to generate a new random spawn point for the blue food object.

# ------------------------------------------------------------------------------------

# Now, Create a Scoreboard and Keep Score

# The scoreboard needs to write some text in the program so that it keeps track of the score for how many pieces of food the snake eats.
# it needs to increase everytime you hit a piece of Food - it will update and keep updating after each impact
# the scroe board also needs to be a turtle object using the write() method from the documentation:

turtle.write(arg,move=False, align="left",font=(Ärial),8,"normal"))

# Parameters:

# arg - object to be written to the TurtleScreen
# move - True/False
# align - one of the strings "left","center", or "right"
# font - a triple - triple tuple ("fontname", fontsize, "fonttype")

# you would call this write method like so:

turtle.write("Home = ", True, align="center")
turtle.write((0,0),True)

# ------------------------------------------------------------------------------------

# We can get the turtle to write a line of text using the write method --> turtle.write(arg, move=False, align="left", font=("Arial",8,"normal"))
# Need to create a new file called scroeboard.py
# create a new scoreboard class that will inherite from the turtle class. 
# it must know how to track the score and increase by one everytime the snack hits the food, as well as display it in the program, each time the turtle objects heads touches the food object, then the score increases by one
# turtle.clear() can be used to clear the write everything the score updates.


# Entered into the scoreboard.py file:

from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup() # this way the object does not trace the movement to the center top of the screen
        self.goto(0, 270)  # this way the scoreboard is at the center top of the screen
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, normal))
        self.hideturtle()

    # Now creating a function to increase the score:
    def increase_score(self):
        self.score += 1
        self.write()

# Now I need to go back into the main.py file and create a scoreboard object from the scoreboard class, after importing it into the main.py file using the following lines where applicable:
# ensure that the color of the scoreboard object is white (or any other visible color) if the background for the game's popup is black

# Modified the piece of the game that detects collision with food to also increase the score (at the very bottom):
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()

# Modified the text so that the scoreboard actually looks good instead of just printing ontop of itself with every increase in the score 
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup() # this way the object does not trace the movement to the center top of the screen
        self.goto(0, 270)  # this way the scoreboard is at the center top of the screen
        self.hideturtle()
        self.update_scoreboard()

    # create function so that the scoreboard object is now just printed on top of itself everytime the score increase
    # this function must delete the previous instance and only show the most recent with the right score
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, normal))

    # Now creating a function to increase the score:
    def increase_score(self):
        self.score += 1
        self.clear() # this will clear the previous instance of the scoreboard
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, normal))

# now instead of hardcoding the inputs for:
self.write(f"Score: {self.score}", align="center", font=("Arial", 24, normal))
#we can set constants at the top and just enter these in the function, so that we can easily change the style across the whole game if these inputs are in multiple functions, instead of searching line-by-line

from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, normal) # as a tuple

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup() # this way the object does not trace the movement to the center top of the screen
        self.goto(0, 270)  # this way the scoreboard is at the center top of the screen
        self.hideturtle()
        self.update_scoreboard()

    # create function so that the scoreboard object is now just printed on top of itself everytime the score increase
    # this function must delete the previous instance and only show the most recent with the right score
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)


# Now I just need to add some code that will detect collision with the walls of the game
# the edge itself is at 300 pixels to the right, bottom, left, and top of the center point,
# So I need to set the boundary to about 280 due to the snake head's size

# in main.py
if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    game_is_on = False

# in the scoreboard.py file, enter this code for a new function:

def game_over(self):
    self.goto(0, 0)  # I don't want this to appear on the same spot as the scoreboard
    self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)


# So far, the code looks like this in the main,py file. All that is left is to add some code to detect when the head of the snake collides with the tail/body:

from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        scoreboard.game_over()


screen.exitonclick()

# Now to detect head collision with tail/body. Upon collision, the game is over. A new segment will be added to the snake after each point is score (ie the head of the snake collide with the good object):
# add this chunk in the snake.py file

# Ehances this:
 def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("green")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)


# Changing that ^ to:

# create a function called add_segment and modify the code chunk from before with the for loop:

def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

def add_segment(self, position):
    new_segment = Turtle("square")
    new_segment.color("green")
    new_segment.penup()
    new_segment.goto(position)
    self.segments.append(new_segment)

def extend(self):
    #add a segment to the snake
    self.add_segment(self.segments[-1].position())

# now, this new function need to be called in the for loop that detects collision with food, to ensure that a
# new segment is added each time the user score a point
# add this to the main.py file:
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

# Detect collision with tail.
# if the head collides with any segment in the tail:
    # trigger the game_over sequence
    for segment in snake.segments:
        # this next line makes sure we are not calculating distance from the head to itself
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

# --------------------------------------------------------------------------------------------------------------

# So far the snake game works as intended, so the next step to improve this game would be to incorporate the concept
# of slicing lists and tuples

# think of slicing for Python like piano keys:

piano_keys = ["a","b","c","d","e","f","g"]

# now what if we just want keys c, d, and e?
piano_keys[2:5]
# and why is this 2-5 and not 2-4? well because it is a range that checks for all items between these markers
# remember list positions start at zero (a is at position 0), where the marks are on the left side of the keys

# now, what if we just want to get everything from the left or right of an item in the list?
print(piano_keys[2:]) # this would print keys c-g (it would exclude the item in the position you specify

print(piano_keys[:5]) # this would print keys a-e

# you can specify a third number after a colon to specify the increment
print(piano_keys[2:5:2]) # this will print ['c', 'e'] in the console

# now let's say you want every second item from the entire list:
print(piano_keys[::2]) # <-- this yields ['a', 'c', 'e', 'g']

# now what if you want to print the list starting from the end?
print(piano_keys[::-1])

piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")

print(piano_tuple[2:5])

# so how would this actually simplify the code block for detecting collision with food in the snake game?

for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10:
        game_is_on = False
        scoreboard.game_over()

# --------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------

# files in the Snake Game:

# main.py
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with tail.
    # if the head collides with any segment in the tail:
        # trigger the game_over sequence
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

    # If the snake head comes too close to the edge of the screen
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()


screen.exitonclick()

# --------------------------------------------------------------------------------------------------------------
# scoreboard.py file:

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal") # as a tuple

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup() # this way the object does not trace the movement to the center top of the screen
        self.goto(0, 270)  # this way the scoreboard is at the center top of the screen
        self.hideturtle()
        self.update_scoreboard()

    # create function so that the scoreboard object is now just printed on top of itself everytime the score increase
    # this function must delete the previous instance and only show the most recent with the right score
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)  # I don't want this to appear on the same spot as the scoreboard
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    # Now creating a function to increase the score:
    def increase_score(self):
        self.score += 1
        self.clear() # this will clear the previous instance of the scoreboard
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))


# --------------------------------------------------------------------------------------------------------------
# food.py file

from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

# --------------------------------------------------------------------------------------------------------------
# snake.py file:
from turtle import Turtle  # needed for the create_snake() method
import random

# starting positions will be stored as a constant, thus requiring its name in ALL_CAPS:
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# another constant needed to define how far the snake moves before the screen refreshes, being 20 paces:
MOVE_DISTANCE = 20
# direction constants:
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
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("green")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        # add a segment to the snake
        self.add_segment(self.segments[-1].position())

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



