
# files in the Snake Game:
# main.py , scoreboard,py , food.py , snake.py


# main.py (where the game to actually execute the game is)
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



