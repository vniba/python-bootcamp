import math

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 3,
    },
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# CoffeeMachine 🟢
# TODO 1.print report of all coffee machine resources
money = 0
coffeeLive = True
balance = 0
coffeeRes = True


def inpu():
    """ask for user input"""
    return input(f"what would you like? (espresso/latte/cappuccino): ").lower()


def total(q, d, n, p):
    """return total of all money"""
    quarter = 0.25
    dimes = 0.1
    nickle = 0.05
    pennie = 0.01
    return round(quarter * q + dimes * d + nickle * n + pennie * p, 2)


def AskandSum():
    print("please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    return total(q=quarters, d=dimes, n=nickles, p=pennies)


while coffeeLive:
    user_choice = inpu()

    if user_choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"money: ${money}")

    elif user_choice == "off":
        coffeeLive = False
    elif (
        user_choice == "latte"
        or user_choice == "espresso"
        or user_choice == "cappuccino"
    ):

        # TODO 2. check if enough resources to make drink
        if user_choice in MENU:
            menIng = MENU[user_choice]["ingredients"]
            for ing in menIng:
                if resources.get(ing) >= menIng.get(ing):
                    coffeeLive = True
                else:
                    coffeeRes = False
                    print(f"Sorry there is not enough {ing}")

        if coffeeRes:

            # TODO 3. check there is enough money
            moneySum = AskandSum()

            # TODO 4. check the money enough for drink
            if moneySum > MENU[user_choice]["cost"]:
                coffeeLive = True
                balance = round(moneySum - MENU[user_choice]["cost"], 2)
                money += MENU[user_choice]["cost"]
                print(f"here is ${balance} dollars in change.")
            else:
                print(f"sorry that's not enough money. money refunded ${moneySum}")

            # TODO 5. making coffee
            # deducting resources
            men = MENU[user_choice]["ingredients"]
            for mK in men:
                for rK in resources:
                    if mK == rK:
                        resources[rK] -= men[mK]

            # if coffeeLive:
            print(f"Here is your {user_choice}. Enjoy! 🍵")
        else:
            coffeeLive = False
    else:
        print("did you mean (espresso/latte/cappuccino)")
