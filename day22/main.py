from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
screen = Screen()
score = Score()
# create screen
screen.bgcolor('black')
screen.title('Pong')
screen.screensize(800, 600)
screen.tracer(0)

screen.listen()

screen.onkey(r_paddle.move_up, 'Up')
screen.onkey(r_paddle.move_down, 'Down')
screen.onkey(l_paddle.move_up, 'w')
screen.onkey(l_paddle.move_down, 's')

game_is = True
while game_is:
    time.sleep(ball.speed_b)
    screen.update()
    ball.move()

    #     detecting coalition with wall
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()

    # collision with  paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(
        l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # left p miss
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # right r miss
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
