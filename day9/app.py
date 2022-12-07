# # dictionary
#
# user = {
#     "name": "jon",
#     "age": 20,
#     "is_ace": True,
# }
#
# # Retrieving data from dictionary
# user_name = user["name"]
# print(user_name)
#
# # adding new item to dictionary
# user["loop"] = False
# print(user)
#
# # create empty dic
# empty_dic = {}
#
# # Edit an item in dic
# user["name"] = "euen"
# print(user)
#
# # Looping through dictionary
# for data in user:
#     print(user[data])
#


# Grading program ❤️

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for name in student_scores:
    score = student_scores[name]
    if score > 90:
        student_grades[name] = "Outstanding!"
    elif score > 80:
        student_grades[name] = "Exceeds Expectations"
    elif score > 70:
        student_grades[name] = "Acceptable"
    else:
        student_grades[name] = "Fail!"

# print(student_grades)

# Nesting
capitals = {"France": "Paris", "England": "London"}

travel_log = {
    "Earth": {
        "Places": ["Arctica", "Antarctic", "Challenger deep"],
        "year": 2340,
    },
    "PlanetB": {
        "Places": ["Alviune", "Braiones", "fleesoc"],
        "year": 2289,
    },
}

# Dic in list
travel = [
    {
        "country": "utopia",
        "places": ["etuma", "saliven", "nodipe"],
        "Rank": 320,
    },
    {
        "country": "lipi",
        "places": ["euma", "saln", "odpe"],
        "Rank": 191,
    },
]

# Dictionary in List ❤️

vlog = [
    {
        "country": "France",
        "Cities": ["Paris", "Lille", "Dijon"],
        "visits": 10,
    },
    {
        "country": "Germany",
        "Cities": ["Berlin", "Hamburg", "Stuttgart"],
        "visits": 3,
    },
]


def add_new_country(country, no_visits, cities):
    new_country = {}
    new_country["country"] = country
    new_country["Cities"] = cities
    new_country["visits"] = no_visits

    vlog.append(new_country)


add_new_country("Russia", 4, ["moscow", "Saint Petersburg"])
print(vlog)


# Blind-auction ❤️
import art as art

print(art.logo)
print("Welcome to the secret auction program...")
auction = {}
auction_is = True


def find_highest(bidding_record):
    highest_amount = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_amount:
            highest_amount = bid_amount
            winner = bidder
        if bid_amount == highest_amount:
            print(f"the winner is know one")

    print(f"the winner is {winner} with a bid of {highest_amount}")


while auction_is:
    name = input("what is your name?:  ")
    bid = int(input("what is your bid? : $"))
    auction[name] = bid
    other_bidders = input("are any other bidders? 'y' or 'n'")
    if other_bidders == "n":
        auction_is = False
        find_highest(auction)
    elif other_bidders == "y":
        auction_is = True
