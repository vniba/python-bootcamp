import pandas as pd

# todo:create dict key:letter->value:value
data = pd.read_csv("nato_phonetic_alphabet.csv")

nato_dic = {row.letter: row.code for (i, row) in data.iterrows()}

# todo:add to a list where user input == code
while True:
    user_input = input("Enter a word? ").upper()
    user_list = []
    if user_input != "":
        user_list = [nato_dic[char] for char in user_input]
    else:
        exit("empty!")
    print(user_list)
