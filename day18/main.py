from turtle import *
import random

mint = Turtle()
colormode(255)

mint.shape("arrow")
mint.color("red", "black")


# mint.forward(180)
# mint.left(90)
# mint.forward(180)
# square #1
# for _ in range(4):
#     mint.forward(180)
#     mint.left(90)

# dashed line #2
# for _ in range(15):
#     mint.down()
#     mint.forward(10)
#     mint.up()
#     mint.forward(10)
#
#
# shapes #3
def random_color():
    #     color = [
    #          'aliceblue', 'antiquewhite', 'aqua', 'yellowgreen', 'yellow',
    #             'tomato', 'blueviolet', 'deeppink', 'deepskyblue', 'dodgerblue',
    #             'darkseagreen', 'gray', 'chartreuse', 'darkgoldenrod', 'hotpink',
    #             'springgreen']

    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)


#
# no = 3
# run = True
# while run:
#     mint.color(random.choice(color))
#     for _ in range(no):
#         mint.right(360/no)
#         mint.forward(100)
#
#
#     no+=1
#     if no == 11:
#         run = False
#

# def random_len():
#     length = round(random.random()*50)
#     return length


# def random_dir():
#
#     #dir= random.choice([mint.backward(random_len()),mint.right(90),mint.forward(random_len())])
#     directions = [0,90,180,270]
#     return random.choice(directions)
#
#
#
# for _ in range(100):
#     mint.shape('circle')
#     mint.speed(0)
#     mint.color(random_color())
#     mint.width(10)
#     mint.forward(25)
#     mint.setheading(
mint.speed(0)
# spirogram #4


# def draw_sp(size_gap):
#     for _ in range(round(360 / size_gap)):
#         mint.color(random_color())
#         mint.setheading(mint.heading() + size_gap)
#         mint.circle(100)
#
#
# draw_sp(20)


screen = Screen()
screen.exitonclick()
