# Functions with outputs
# def format_name(f_name, l_name):
#     f_c = f_name.title()
#     l_c = l_name.title()
#     return f"{f_c} {l_c}"
#
#
# print(format_name("elizaBeth", "porcH"))

# # Day in month ❤️
# def is_leap(year):
#     """return whether the year is leap or not in Boolean value"""
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
#
# def days_in_month(y, m):
#     if m > 12 or m < 1:
#         return "invalid Month"
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(y) and m == 2:
#         return 29
#     return month_days[m - 1]
#
#
# year = int(input("enter a year: "))
# month = int(input("enter a month: "))
# day = days_in_month(year, month)
# print(day)

# Calculator ❤️

# adding numbers
def add(n1, n2):
    """addition"""
    return n1 + n2


# subtracting numbers
def sub(n1, n2):
    """subtract"""
    return n1 - n2


# Multiplying numbers
def mul(n1, n2):
    """multiplication"""
    return n1 * n2


# Dividing numbers
def div(n1, n2):
    """dividing"""
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}
# user input for 2 numbers
import art as art


def calculator():
    print(art.logo)
    should_continue = True

    num1 = float(input("what's the first number?: "))
    while should_continue:
        # show each key
        for key in operations:
            print(key)

        # user input
        operation_symbol = input("pick an operation : ")
        num2 = float(input("what's the next number?: "))
        # calculation
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        # check whether continue
        continues = input(
            f"type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: "
        ).lower()
        # to continue or not
        if continues != "y":
            should_continue = False
            calculator()
        else:
            num1 = answer


calculator()
