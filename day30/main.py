# try:
#     file = open('error.txt')
#     a = {'k': 'v'}
#     print(a['k'])
# except FileNotFoundError:
#     file = open('error.txt', mode = 'w')
#     file.write('error is error')
# except KeyError as error:
#     print('key not valid', error)
# else:
#     co = file.read()
#     print(co)
# finally:
#     file.close()
#     raise TypeError('fk')
import json

# height = float(input('height'))
# weight = float(input('height'))
#
# if height > 3:
#     raise ValueError('enter a valid height')
# bmi = weight / height ** 2
# print(bmi)
fruits = ['apple', 'peach', 'orange']


# catch the exception
# Index error handling #1

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print('fruit pie')
    else:
        print(fruit + ' pie')


# make_pie(3)

# challenge #2
facebook_posts = [
    {'likes': 21, 'Comments': 2},
    {'likes': 12, 'Comments': 8},
    {'likes': 33, 'Comments': 10, 'Shares': 20},
    {'Comments': 89},
    {'Comments': 100, 'Shares': 20},
]
total_likes = 0
for post in facebook_posts:
    try:
        total_likes += post['likes']
    except KeyError:
        pass

# print(total_likes)
