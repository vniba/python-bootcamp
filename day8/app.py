import math

# def greet(name):
#     print("hlo,", name)
#     print("how")
#     print("r u")
#
#
# greet("jon")
# greet("max")

# function with more than 1 input


# def greet_with(name, location):
#     print(f"{name} from {location}")
#
#
# greet_with(location="ohio", name="john")

# area ❤️
# test_h = int(input("height of the wall: "))
# test_w = int(input("width of the wall: "))
# coverage = 5
#
#
# def paint_calc(height, width, cover):
#     area = height * width
#     no_of_cans = math.ceil(area / cover)
#     return no_of_cans
#
#
# paint = paint_calc(height=test_h, width=test_w, cover=coverage)
# print(paint)

# Prime number checker ❤️
#
# n = int(input("check the number: "))
#
#
# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print(f"{number} is a prime number")
#     else:
#         print(f"{number} is not a prime number")
#
#
# prime_checker(number=n)

# caesar cipher ❤️
import alphabet as alph
import art as art

print(art.logo)


def caesar(user_text, shift_amount, cipher_direction):
    cipher_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1  # it will subtract
    for char in user_text:
        if char in alph.alphabet:  # if input other than char
            position = alph.alphabet.index(char)
            new_position = position + shift_amount
            cipher_text += alph.alphabet[new_position]
        else:
            cipher_text += char

    print(f"the {cipher_direction} text is {cipher_text}")


should_continue = True  # check  should continue
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    # if direction != "encode" or "decode" != direction:
    #     print("Type 'encode' to encrypt, type 'decode' to decrypt")

    text = input("Type your message:\n").lower()

    # if shift no > alphabet length
    shift = int(input("Type the shift number:\n"))
    if shift > 27:
        shift %= 26

    caesar(user_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input(f"do you wanna play again, y or n \n").lower()
    if restart != "y":
        should_continue = False
        print("goodbye")
