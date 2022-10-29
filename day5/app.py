import random
# loops
# fruits = ['apple', 'banana', 'cherry']
# for fruit in fruits:
#   print(fruit)
#   print(fruit + ' pie')

# average Height ❤️
#
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
#
# total = 0
# length = 0
# for i in student_heights:
#   total += i
#   length += 1
#
# avg = round(total / length)
# print(avg)
# print(sum(student_heights))

# Adding Evens ❤️
# total = 0
# for i in range(2, 101, 2):
#   total += i
# print(total)

# Highest Score ❤️
#
# student_score = input("Input a list of student scores ").split()
# for n in range(0, len(student_score)):
#   student_score[n] = int(student_score[n])
#
# helo = 0
# for value in sorted(student_score):
#   helo = value
#
# print(f"The highest score in the class is: {helo}")
#
# high_score = 0
# for score in student_score:
#   if score > high_score:
#     high_score = score
#
# print(f"The highest score in the class is: {high_score}")

# for num in range(1, 11, 3):
#   print(num)
# total of first 100 natural no
# sum = 0
# for num in range(1, 101):
#   sum += num
# print(sum)

# Fizz buzz exercise ❤️

# print('Fizz buzz ✌️')
#
# for number in range(1, 101):
#  if number % 5 == 0 and number % 3 == 0:
#    print('Fizz Buzz')
#  elif number % 3 == 0:
#    print('Fizz')
#  elif number % 5 == 0:
#    print('Buzz')
#  else:
#    print(number)

# Password generator ❤️

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ''
# easy way
for letter in range(nr_letters): # length of letters
  password += letters[(random.randint(0, len(letters) - 1))]
for number in range(nr_numbers):
  password += numbers[(random.randint(0, len(numbers) - 1))]
for symbol in range(nr_symbols):
  password += symbols[(random.randint(0, len(symbols) - 1))]
print(f"Easy to Hack \n{password}")

hard_paw = ''
for paw in range(len(password)):
  hard_paw += password[random.randint(0, len(password) - 1)]

print(f"Hard to crack \n{hard_paw}")

# another way 💗

new_passw = []
for let in range(nr_letters):
  new_passw.append(random.choice(letters))
for num in range(nr_numbers):
  new_passw.append(random.choice(numbers))
for sym in range(nr_symbols):
  new_passw.append(random.choice(symbols))

new_one = ''
random.shuffle(new_passw)
for i in new_passw:
 new_one += i
print(f"new one \n{new_one}")

# another one 💗

limit = int(input(f"enter your password length \n "))
all = numbers + letters + symbols

cryptic_paw = ''
for i in range(limit):
  random.shuffle(all)
  cryptic_paw += random.choice(all)

print(cryptic_paw)