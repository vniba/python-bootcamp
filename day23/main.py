import time
from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.tracer(0)

player = Player()
manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(fun = player.go_up, key = "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    manager.create_cars()
    manager.move_cars()

    # detect collision
    for car in manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    # success
    if player.is_finished():
        player.reset_pos()
        score.increase_level()

screen.exitonclick()
