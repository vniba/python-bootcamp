import random

import art as art

# ----------- scope ---------

energy = 12


def increase_energy():
    global energy  # don't try
    energy += 10
    # print(f"energy inside fun {energy}")


increase_energy()
# print(f"energy outside fun {energy}")


# no block scope
water_level = 12
fishes = ["tuna", "sardine", "anchovy"]
if water_level > 5:
    new_fishes = fishes[2]

# print(new_fishes)

# Global constants
GR = 1.61
PI = 3.141592

# Guess the number 💙
lifes = 0
EASY = 10
HARD = 5


def check_answer(guess, answer, life):
    """checks answer against guess. return no of lifes"""
    should_game = False
    if guess > answer:
        print("Too High..")
        return life - 1
    elif guess < answer:
        print("Too Low..")
        return life - 1
    elif guess == answer:
        print(f"You made it! the answer is {answer}")


def set_difficulty():
    mode = input("choose the game level, 'easy' or 'hard': ").lower()
    if mode == "easy":
        return EASY
    elif mode == "hard":
        return HARD


def game():
    number = random.randint(1, 100)
    print(number)
    print(art.logo)
    print("welcome to the numbers world!")
    print("you can choose number b/w 1 - 100")

    lifes = set_difficulty()
    user_guess = 0

    while user_guess != number:
        print(f"you have {lifes} lifes remining..")
        user_guess = int(input("enter your number: "))

        lifes = check_answer(guess=user_guess, answer=number, life=lifes)
        if lifes == 0:
            print(f"You ran to to zero, go go...")
            return


game()
