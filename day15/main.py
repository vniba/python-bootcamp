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
profit = 0
is_on = True


def is_resources_sufficient(order_ingr):
    for item in order_ingr:
        if resources[item] <= order_ingr[item]:
            print(f"sorry ther not enough money for {item}")
            return False
    return True


def process_coins():
    """returns total of coins inserted"""
    print("please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def transaction_success(mon_receive, drink_cost):
    """return true payment is accepted, or false if money not sufficient"""
    if mon_receive >= drink_cost:
        change = round(mon_receive - drink_cost, 2)
        print(f"here is ${change} in change ")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry that's not enough money. money refunded")
        return False


def make_coffee(drink_name, order_ing):
    for item in order_ing:
        resources[item] -= order_ing[item]
    print(f"here is your {drink_name} 🍵")


while is_on:
    choice = input(f"what would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if transaction_success(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
