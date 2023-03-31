# name = 'Angela'
# new_list = [letter + '🔥' for letter in name]
# print(new_list)
import random

# new_l = [n * 2 for n in range(1, 7) if n % 2 == 0]
# print(new_l)

names = ["Beth", "Alex", "Caroline", "Dave", "Freddie"]
# uper_n = [name.upper() for name in names if len(name) > 5]
# print(uper_n)

# coding challenge #1
number = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n ** 2 for n in number]
# print(squared_numbers)

# coding challenge #2
result = [num for num in number if num % 2 == 0]
# print(result)

# coding challenge #3
# todo: new list result that are common in both files
# todo: output in int

with open("file1.txt") as f1:
    res = f1.readlines()

with open("file2.txt") as f2:
    res2 = f2.readlines()

results = [int(num) for num in res if num in res2]
# print(results)

student_score = {student: random.randint(1, 100) for student in names}
# print(student_score)

passed_students = {name: score for (name, score) in student_score.items() if score > 70}
# print(passed_students)

# dictionary comprehension #1
sentence = "What is the airspeed Velocity of an Unladen Swallow?"
new = sentence.split()

s_result = {word: len(word) for word in new}
# print(s_result)

# dictionary comprehension #2
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: temp * 9 / 5 + 32 for (day, temp) in weather_c.items()}
# print(weather_f)


import pandas as pd

student_dict = {
    "student": ["apple", "banana", "cherry"],
    "score": [40, 50, 10]
}

df = pd.DataFrame(student_dict)

for (index,row) in df.iterrows():
    print(row)


