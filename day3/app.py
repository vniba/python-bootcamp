# if / else
# print("welcome to the rollercoastr!")
# height = int(input("what is your height in cm? "))
#
# if 120 <= height:
#  print("you can ride")
# else:
#   print("you can't ride")

# odd or even ❤
# number = int(input("whit number do you want to change? "))
#
# if number % 2 == 0:
#   print("Even")
# else:
#   print("odd")

# print('welcome to the new tintin hierarchy')
# age = int(input('wht ur age ? '))
# height = int(input('what ur height? '))
#
# if height >= 120:
#   if age <= 18:
#     print('you can ride, fee $12')
#   elif age > 12:
#     print('you can ride, fee $7')
#   else:
#     print('you can ride, fee $5')
# else:
#   print('you cannot ride')

# BMI calculator 2.0 ❤️
#
# print('welcome to BMI calculator')
# weight = float(input('enter ur weight in kg? '))
# height = float(input('enter ur height in m? '))
# bmi = round(weight / (height ** 2))
# print('welcome to the new tintin hierarchy')
# age = int(input('wht ur age ? '))
# height = int(input('what ur height? '))
#
# if height >= 120:
#   if age <= 18:
#     print('you can ride, fee $12')
#   elif age > 12:
#     print('you can ride, fee $7')
#   else:
#     print('you can ride, fee $5')
# else:
# #   print(f'Your bmi is {bmi}, you are clinically obese')
# elif bmi > 30:
#   print(f'Your bmi is {bmi}, you are obese')
# elif bmi > 25:
#   print(f'Your bmi is {bmi}, you are overweight')
# elif bmi > 18.5:
#   print(f'Your bmi is {bmi}, you have normal weight')
# else:
#   print(f'Your bmi is {bmi}, yor are underweight')

# multiple if
# print('welcome to the new tintin hierarchy')
# height = int(input('what ur height? '))
# bill = 0
#
# if height >= 120:
#   print('you can ride the tintin')
#   age = int(input('wht ur age ? '))
#   if age <= 18:
#     bill = 12
#     print('you can ride, fee $12')
#   elif age > 12:
#     bill = 7
#     print('you can ride, fee $7')
#   else:
#     bill = 5
#     print('you can ride, fee $5')
#   photo = str(input('do yo need photos? y / n '))
#   if photo == 'y':
#     print(f'yor ticket fee ${bill + 3}')
#   else:
#     print('yor ticket fee {bill}')
# else:
#   print('you cannot ride')

# pizz order  ❤️

# print('welcome to pizza mansion')
# size = input('What size of pizza do u want? S, M, L ')
# add_pepperoni = input('Do you want pepperoni? Y / N ')
# extra_cheese = input('Do you need extra cheeze? Y/N ')
#
# pizza_bill = 0
# pepperoni_s = 2
# pepperoni_m_l = 3
# ex_cheese = 1

# if size == 'S':
#   if add_pepperoni == 'Y':
#     if extra_cheese == 'Y':
#       pizza_bill += 15 + ex_cheese + pepperoni_s
#       print(f"Your final bill is: ${pizza_bill}")
#     else:
#       pizza_bill += 15 + pepperoni_s
#       print(f"Your final bill is ${pizza_bill}")
#   else:
#     pizza_bill += 15
#     print(f"Your final bill is ${pizza_bill}")
# elif size == 'M':
#   if add_pepperoni == 'Y':
#     if extra_cheese == 'Y':
#       pizza_bill += 20 + ex_cheese + pepperoni_m_l
#       print(f"Your final bill is: ${pizza_bill}")
#     else:
#       pizza_bill += 20 + pepperoni_m_l
#       print(f"Your final bill is ${pizza_bill}")
#   else:
#     pizza_bill += 20
#     print(f"Your final bill is ${pizza_bill}")
# elif size == 'L':
#   if add_pepperoni == 'Y':
#     if extra_cheese == 'Y':
#       pizza_bill += 25 + ex_cheese + pepperoni_m_l
#       print(f"Your final bill is: ${pizza_bill}")
#     else:
#       pizza_bill += 25 + pepperoni_m_l
#       print(f"Your final bill is ${pizza_bill}")
#   else:
#     pizza_bill += 25
#     print(f"Your final bill is ${pizza_bill}")
# else:
#   print('write S / L / M')
#
# other version 💗

# cheking size
# if size == 'S':
#   pizza_bill += 15
# elif size == 'M':
#   pizza_bill += 20
# elif size == 'L':
#   pizza_bill += 25
# # cheking pepperoni
# if add_pepperoni == 'Y':
#   if size == 'S':
#     pizza_bill += 2
#   else:
#     pizza_bill += 3
# # checking cheese
# if extra_cheese == 'Y':
#   pizza_bill += 1
#
# print(f'Your final bill is ${pizza_bill}')

# logical operator using pizza remasterd
#
# print('welcome to pizza mansion')
# size = input('What size of pizza do u want? S, M, L ')
# add_pepperoni = input('Do you want pepperoni? Y / N ')
# extra_cheese = input('Do you need extra cheeze? Y/N ')
#
# pizza_bill = 0
# if size == 'S':
#   pizza_bill += 15
# elif size == 'M':
#   pizza_bill += 20
# elif size == 'L':
#  pizza_bill += 25
#
# if add_pepperoni == 'Y' and size == 'S':
#   pizza_bill += 2
# else:
#   pizza_bill += 3
#
# if extra_cheese == 'Y':
#   pizza_bill += 1
#
# print(f'Yor final bill is ${pizza_bill}')

# Love calculator ❤️

# print('Welcome to the Love ❤️ calculator')
# name1 = input(f"what's your name?\n")
# name2 = input(f"what's your name?\n")
#
# lower_name1 = name1.lower()
# lower_name2 = name2.lower()
# true_count = 0
# true_count += lower_name1.count('t')
# true_count += lower_name1.count('r')
# true_count += lower_name1.count('u')
# true_count += lower_name1.count('e')
#
# true_count += lower_name2.count('t')
# true_count += lower_name2.count('r')
# true_count += lower_name2.count('u')
# true_count += lower_name2.count('e')
#
#
# love_count = 0
#
# love_count += lower_name1.count('l')
# love_count += lower_name1.count('o')
# love_count += lower_name1.count('v')
# love_count += lower_name1.count('e')
#
# love_count += lower_name2.count('l')
# love_count += lower_name2.count('o')
# love_count += lower_name2.count('v')
# love_count += lower_name2.count('e')
#
# score = int(f'{true_count}{love_count}')
#
# if (score < 10) or (score > 90):
#   print(f'Your score  is {score}, You go together like coke and mentos')
# elif (score > 40) and (50 > score):
#   print(f'Your score  is {score}, you are alright together')
# else:
#   print(f'Your score  is {score}')

# treasure island ❤️

print('Welcome to the treasure island, The adventure of life time')
print("Your mission is to find the lost treasure")
first_q = input('You are in the middle of a crossroad at greek, where you wanna go? "left" or "right" \n').lower()

if first_q == "right":
  print("You chose the death, Game over...")
elif first_q == "left":
 second_q = input('You are in the front of a sacred river, what you wanna do? "swim" in a yaht or "wait" in the forest \n').lower()
 if second_q == "swim":
   print("You swum into the mouth of a crocodile, Game over... ")
 elif second_q == "wait":
    third_q = input(
      'You\'ve arrived in the castle of liberty, There are three doors "Red", "Blue", "Yellow" which one you choose for your after life? \n').lower()
    if third_q == "red":
     print("You chosen the place where full of fire and vengeance, Game over..")
    elif third_q == "blue":
      print("You chosen the ultimate sea, Game over...")
    elif third_q == "yellow":
      print("You found the treasure , You won!")
    else:
      print(" you chose wrong door")
 else:
   print("You wanna fly, choose correctly")
else:
  print("there only two way")

