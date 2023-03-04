from turtle import Turtle, Screen
from random import *
# squid = Turtle()
screen = Screen()

# 
# def move_f():
#     squid.forward(20)
    
screen.listen()
# screen.onkey(key="space",fun = move_f)

#Etch-a-Sketch #1

# def move_b():
#     squid.backward(20)
#     
# def move_l():
#     squid.left(10)
#     
#                   
# def move_r():
#     squid.right(10)
#     
# def clear_s():
#     squid.clear()
#     squid.penup()
#     squid.home()
#     squid.pendown()
#     
# def control():
#     screen.onkey(key='w',fun = move_f)
#     screen.onkey(key='s',fun = move_b)
#     screen.onkey(key='a',fun = move_l)
#     screen.onkey(move_r,"d")
#     screen.onkey(clear_s,"c")
#     
#      
# 
# control()

# Turtle Race
is_race_on = False
screen.setup(width = 500,height = 500)
user_input = screen.textinput(title='who win the race',prompt='enter a color?')
color=["red","green","yellow","orange","blue","purple"]

all_turtle = []
y_p = [-100,-60,-20,20,60,100]
for i in range(0,6):
    y= -200
    new_turtle = Turtle('turtle')
    new_turtle.penup()
    new_turtle.color(color[i])
    new_turtle.goto(x=-240,y=y_p[i])
    all_turtle.append(new_turtle)
   

if user_input:
    is_race_on = True

while is_race_on:
    
    for t in all_turtle:
        if t.xcor() > 220:
            is_race_on = False
            winning_color = t.pencolor()
            if winning_color == user_input:
                print(f"you've won! {winning_color} turtle is the winner")
            else:
                print(f"you've lose! {winning_color} turtle is the winner")
        rand_d = randint(0,10)
        t.forward(rand_d)

    

screen.exitonclick()