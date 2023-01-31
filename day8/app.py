import random

from game_data import data
import art


def format_data(account):
    """format the obj in printable format"""
    account_name = accont_f["name"]
    account_desc = accont_f["description"]
    account_country = accont_f["country"]
    return f"{account_name}, a{account_desc}, from {account_country}"


# display art
print(art.logo)

# generate random data from array
accont_f = random.choice(data)
accont_s = random.choice(data)
# print(accont_s, accont_f)
# if accont_f == accont_s:
#     accont_s = random.choice(data)

# format the obj in printable format
print(f"Compare A: {format_data(account = accont_f)}")
print(art.vs)
print(f"Against B: {format_data(account = accont_s)}")
# ask user guess
# check if user is correct
# give feedback user
# update score
# if wins continue game

# making the object b become next account at position a
