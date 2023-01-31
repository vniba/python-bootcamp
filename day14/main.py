# lowerHigher game
import game_data
import art
import random


def show_details():
    """return random object form game_data array"""
    return random.choice(game_data.data)


def show():
    """display logo and game information"""
    print(art.logo)
    print(
        f"Compare A: {first['name']}, a {first['description']}, from {first['country']} "
    )
    print(art.vs)
    print(
        f"Against b: {second['name']}, a {second['description']}, from {second['country']}"
    )


# global variables
game = True
current_score = 0
answer = False
swap = False
third = {}

while game:
    # generate random data from array
    if not swap:
        first = show_details()
        second = show_details()
        if first == second:
            second = show_details()
    else:
        first = third
        second = show_details()
        if first == second:
            second = show_details()
    # format the obj in printable format
    show()

    # ask user guess
    user_inp = (input("Who has more followers type? 'A' or 'B' ")).lower()

    # check if user is correct
    if first["follower_count"] > second["follower_count"] and user_inp == "a":
        answer = 1
    elif first["follower_count"] < second["follower_count"] and user_inp == "b":
        answer = 2
    else:
        answer = 0

    # give feedback user
    if answer == 1 or answer == 2:
        # update score
        current_score += 1
        # if wins continue game
        print(f"you're right! Current score:{current_score}")
        # making the object b become next account at position a
        swap = True
        third = first
        game = True
    else:
        game = False
        print(f"you're wrong! Final score:{current_score}")
