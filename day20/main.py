from turtle import Screen
from snake import Snake
from food import Food
from scorecard import Score_card
import time

# => setting up the screen
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("snake Game")
screen.tracer(0)

# snake
snake = Snake()
food = Food()
score = Score_card()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # collition with food
    if snake.head.distance(food) < 13:
        food.refresh()
        snake.extend()
        score.increase_score()

    # detect collition with wall
    if (
        snake.head.xcor() > 380
        or snake.head.xcor() < -380
        or snake.head.ycor() > 380
        or snake.head.ycor() < -380
    ):
        game_is_on = False
        score.game_over()

    # detect collition with tail

    for sn in snake.snake[1:]:
        if snake.head.distance(sn) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()
