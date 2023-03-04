import random
import turtle
# import colorgram
from turtle import Turtle, Screen

# colors = colorgram.extract('spot.jpg', 20)
# color = []
# for c in colors:
#     color.append((c.rgb.r, c.rgb.g, c.rgb.b))
#
# print(color)

screen = Screen()
screen.colormode(255)


def random_color():
    color_list = [(253, 251, 248), (254, 250, 252), (232, 251, 242), (198, 12, 32),
                  (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5),
                  (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16),
                  (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121),
                  (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61)]

    return random.choice(color_list)


# 10 - 10 row
# 20 width , space 50

spot = Turtle()
spot.penup()
spot.speed(0)

x_pos = -200
y_pos = -200

for i in range(1, 101):
    spot.goto(x_pos, y_pos)
    spot.dot(20, random_color())
    x_pos += 50

    if i % 10 == 0:
        x_pos = -200
        y_pos += 50

screen.exitonclick()
