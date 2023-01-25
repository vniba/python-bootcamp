#  Describe the Problem🤍
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You gotee")


# Reproduce the Bug 🤍
# my_function()
from random import randint

dice_imgs = ["1", "2", "3", "4", "5", "6"]
dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

#   Fixing Errors and Watching for Red Underlines 🤍
# year = int(input("what's your year of birth? "))
# if 1980 < year < 1994:
#     print("You are a millenial")
# elif year >= 1994:
#     print("you are a 2k kid ")


#  Squash bugs with a print() Statement 🤍
pages = 0
words_per_page = 0
# pages = int(input("number of pages: "))
# words_per_page = int(input("Number of words per page: "))
# total_words = pages * words_per_page
# print(total_words)

#   Using a Debugger 🤍
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append((new_item))
    print(b_list)


# mutate([1, 2, 3, 4, 5])

# Debugging Odd or Even 🤍
# number = int(input("which number do you want to check? "))
#
# if number % 2 == 0:
#     print("this is an even number")
# else:
#     print("this is and odd number")

# Leap Year 🤍

# year = int(input("which year do you want to check? "))
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("leap Year")
#         else:
#             print("not leap year")
#     else:
#         print("leap Year")
# else:
#     print("not leap year")

# FizzBuzz 🤍

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
