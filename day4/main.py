# randomisation
import random

# import my_module as pi
# print(pi.pi)
# random integer
# random_int = random.randint(1, 20)
# print(random_int)
#
# # random float
# random_float = random.random() * 5
# print(random_float)
#
# # Heads or Tails ❤️
# heads_tails = random.randint(1, 2)
# if heads_tails != 1:
#   print('Tails')
# else:
#   print('Heads')

#   lists
# planets = ['mercury', 'venus', 'earth', 'mars']
#
# print(planets[0])  # mercury
# print(planets[-1])  # neptune
#
# planets[2] = 'Earth'
# print(planets)
#
# planets.append('jupiter')
#
# planets.extend(['saturn', 'uranus', 'neptune'])
# print(planets)

# Banker Roulette ❤️
# names = input(f"Give me everybody's names, separated by comma. ")
# in_name = names.split(', ')
# print(in_name)
#
# person = random.randint(0, len(in_name) - 1)
# who_pay = in_name[person]
# print(f"{who_pay} is the saint today")
#
# # another method 💗
# who_pay_now = random.choice(in_name)
# print(who_pay_now)

# day = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
#
# month = [ 'january', 'saturday', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
#
# day_month = [day, month]
# print(day_month)

# Treasure map ❤️
# row1 = ["🟩", "🟩", "🟩"]
# row2 = ["🟩", "🟩", "🟩"]
# row3 = ["🟩", "🟩", "🟩"]
# mapp = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
#
# # variables
# position = (input("where do you want to put th treasure? "))
# horizontal = int(position[0])
# vertical = int(position[1])
# show_x = '❌'
# # condition
#
# first = mapp[vertical - 1][horizontal - 1] = show_x
#
# print(f"{row1}\n{row2}\n{row3}")


# Rock Paper Scissors ❤️

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

user = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n '))
if user < 0 or user >= 3:
  print('enter 0, 1,or 2')
else:
  print(user)
  choice = random.randint(0, 2)
  images = [rock, paper, scissors]
  print(images[user])

  print('Computer chose:')
  print(images[choice])
  # decision

  if user == choice:
    print('draw 🏳️')
  elif user == 1 and choice == 0 or user == 0 and choice == 2 or user == 2 and choice == 1:
    print('You Won 🎊')
  else:
    print('You Lose 😑')




