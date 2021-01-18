from turtle import Turtle, Screen
import random

t = Turtle()
t.shape("turtle")
# t.pensize(10)


# TODO: Importing Colors from a Damien  Hirst Sport Painting

# import colorgram
# colors = colorgram.extract('spot_paint.jpg', 30)
# print(colors)
# rgb_color = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_color.append(new_color)
#
# print(rgb_color)

# TODO: Draw Dots using the colors extracted from Damien  Hirst Sport Painting
colors = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162),
          (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90),
          (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48),
          (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]

import turtle as turtle_module
turtle_module.colormode(255)

t.speed("fastest")
t.penup()
t.hideturtle()

t.setheading(225)
t.forward(300)
t.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    t.dot(40, random.choice(colors))
    t.forward(50)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)



# TODO: Draw a Square
# for i in range(4):
#     t.forward(100)
#     t.right(90)

# TODO: Line with Dashes
# for _ in range(10):
#     t.forward(10)
#     t.penup()
#     t.forward(10)
#     t.pendown()

# TODO: Draw a Triangle, Square, Pentagon, Hexagon, ... Decagon


#
# def change_color():
#     r = random.random()
#     g = random.random()
#     b = random.random()
#     t.color(r, g, b)
#
#
# def task(num_sides):
#     change_color()
#     for _ in range(num_sides):
#         t.forward(100)
#         t.right(360 / num_sides)
#
#
# for i in range(3, 11):
#     task(i)

# TODO: Random walk

# def change_color():
#     r = random.random()
#     g = random.random()
#     b = random.random()
#     t.color(r, g, b)
#
#
# directions = [0, 90, 180, 270]
# for _ in range(100):
#     change_color()
#     t.forward(30)
#     t.setheading(random.choice(directions))

s = Screen()
s.exitonclick()
