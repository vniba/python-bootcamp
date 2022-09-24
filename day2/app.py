# # Data types
# # string
# array = 'hello'[4]
# print(array)
#
# # interger
# num = 124 + 231
# print(num)
# large = 123_456_789
# print(large)
#
# # forat
# pi = 3.1415
# print(pi)
#
# # boolean
# isit = False
# print(isit)
#
# num_char = len(input('what? '))
# print(type(num_char))
#
# # typing conversion
# string = str(num_char)
# # print(string)
#
# nume = '1245'
# print(type(nume))
#
# new_nume = int(nume)
#
# floate = float('3.1415')
# print(type(floate))
# print(floate)
#
# # boolean
# boole = 0
# print(bool(boole))

# enter a two-digit number and return sum of that numbers ❤️

# user_input = input('enter a number \n')
# print(type(user_input))
# first_one = user_input[0]
# second_one = user_input[1]
# output = int(first_one) + int(second_one)
# print(output)

# operators
# sub = 4 - 8
# print(sub)
# div = (type(9 / 3))
# print(div)
# mult = 7 * 7
# print(mult)
# expo = 3 ** 5
# print(expo)

# # PEDMASLR (), ** , * & / ,  + & -, left to right

# print(3 * (3 + 3) / 3 - 3)
# print(3 / 3 + 3 * 3 - 3)

# # BMI calculate ❤️
# height = input('enter your height in m: ')
# weight = input('enter your weight in kg: ')
#
# BMI = (int(weight) / float(height) ** 2)
# bmi_as_int = int(BMI)
# print(int(bmi_as_int))
#
# result = ((8//2))
# result /= 2
# grad = 11
# isWinner = False
# #f string
# print(f'yor score is {result} ur grade {grad} yo winng {isWinner}')
# print('ur result is ' + str(result))

# ask age and print how many day week months untill 90 ❤️
# age = int(input('what is your current age ? '))
#
# years_remaining = 90 - age
# days_remaining = years_remaining * 365
# weeks_remaining = years_remaining * 52
# month_remaining = (years_remaining * 12)
#
# message = f"You have {days_remaining} days, {weeks_remaining} weeks, {month_remaining} months, {years_remaining} years left"
# print(message)

# Tip calculator
print('welcome to the tip calculator.')
bill = float(input('What was the total bill ? $'))
percentage = int(input('What percentage tip would you like to give? 10, 12 or 15? '))
total_people = int(input("How many people to spit the bill? "))

tip_total = ((bill * percentage) / 100)
bill_total = bill + tip_total
each_person = bill_total / total_people
total = round(each_person, 2)
final_total = '{:.2f}'.format(total)
message = f"each person should pay: ${final_total}"
print(message)
