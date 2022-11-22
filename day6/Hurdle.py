def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if front_is_clear():
        move()
        if right_is_clear():
            turn_right()
    else:
        turn_left()


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
black
