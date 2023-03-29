# name = 'Angela'
# new_list = [letter + '🔥' for letter in name]
# print(new_list)

# new_l = [n * 2 for n in range(1, 7) if n % 2 == 0]
# print(new_l)

# names = ["Beth", "Alex", "Caroline", "Dave", "Freddie"]
# uper_n = [name.upper() for name in names if len(name) > 5]
# print(uper_n)

# coding challenge #1
number = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n**2 for n in number]
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
# print(results)ś
