# with open('new.txt', mode = 'a') as file:
#     file.write('1')

# with open('new.txt') as file:
#     contents = file.read()
#     print(contents)

# with open('../day20/data.txt') as data:
#     contents = data.read()
#     print(contents)

# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3scho

PLACEHOLDER = '[name]'

with open('./Input/Names/invited_names.txt') as name:
    names = name.readlines()

with open('./Input/Letters/starting_letter.txt') as letter:
    let = letter.read()


def strip_str(text):
    """
    :param text:
    :return: striped text
    """
    return text.strip("\n")


def replace_str(txt, old, new):
    """
    :param txt:
    :param old:
    :param new:
    :return: replaced txt
    """
    return txt.replace(old, new)


for name in names:
    new_name = (strip_str(name))
    with open(f"./Output/ReadyToSend/Letter_for_{new_name}.txt", "x") as out:
        out.write(replace_str(let, PLACEHOLDER, new_name))
