import random

from game_data import data
from art import logo, vs


def format_data(account):
    """format the obj in printable format"""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"

def check_ans(guess,a_foll,b_foll):


# display art
print(logo)

# generate random data from array
accont_f = random.choice(data)
accont_s = random.choice(data)
if accont_f == accont_s:
    accont_s = random.choice(data)

# format the obj in printable format
print(f"Compare A: {format_data(account = accont_f)}")
print(vs)
print(f"Aganist B: {format_data(account = accont_s)}")

# ask user guess
user_guess = input(f"who has more followers? 'A' or 'B' ").lower()
# check if user is correct
f_follower_count = accont_f["follower_count"]
s_follower_count = accont_sś["follower_count"]

# give feedback user
# update score
# if wins continue game

# making the object b become next account at position a
