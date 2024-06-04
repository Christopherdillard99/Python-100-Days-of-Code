
# this is just the code file, please find the end of the notes file for this folder to see my detailed explanation for each step to understand functionality and purpose.


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
turtle_module.colormode(255)
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1,number_of_dots + 1):
   tim.dot(20, random.choice(color_list))
   tim.forward(50)

   # this next step with a modulo sign check wether the dot count is 10, 20, 30, 40, etc. to then start on the next row until 100.
   if dot_count % 10 == 0:
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()