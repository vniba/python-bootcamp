import random
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
words_to_learn = {}
card = {}

try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    o_data = pd.read_csv('data/french_words.csv')
    words_to_learn = o_data.to_dict(orient = 'records')
else:
    words_to_learn = data.to_dict(orient = 'records')


def clear_delay():
    window.after_cancel(delay)


def show_word():
    global card, delay
    window.after_cancel(delay)
    print(words_to_learn)
    card = random.choice(words_to_learn)

    canvas.itemconfig(card_title, text = 'French', fill = 'black')
    canvas.itemconfig(card_body, text = card['French'], fill = '#000')
    canvas.itemconfig(canvas_img, image = img_front)
    delay = window.after(3000, show_english)


def show_english():
    global card
    canvas.itemconfig(card_title, text = 'English', fill = '#fff')
    canvas.itemconfig(card_body, text = card['English'], fill = '#fff')
    canvas.itemconfig(canvas_img, image = back_img)


def know_the_word():
    words_to_learn.remove(card)
    datas = pd.DataFrame(words_to_learn)
    datas.to_csv('data/words_to_learn.csv', index = False)
    show_word()


window = Tk()
window.title('Who is me')
window.config(pady = 50, padx = 50, bg = BACKGROUND_COLOR)

delay = window.after(3000, show_english)

canvas = Canvas(width = 800, height = 530, bg = BACKGROUND_COLOR, highlightthickness = 0)
img_front = PhotoImage(file = 'images/card_front.png')
back_img = PhotoImage(file = 'images/card_back.png')
canvas_img = canvas.create_image(400, 265, image = img_front)
card_title = canvas.create_text(400, 150, text = 'Title', font = ('arial', 40, 'italic'))
card_body = canvas.create_text(400, 265, text = 'body', font = ('arial', 60, 'bold'))
canvas.grid(row = 0, column = 0, columnspan = 2)

cross_img = PhotoImage(file = './images/wrong.png')
unknown_btn = Button(image = cross_img, highlightthickness = 0, bg = BACKGROUND_COLOR,
                     command = show_word)
unknown_btn.grid(column = 0, row = 1)

check_img = PhotoImage(file = './images/right.png', )
known_btn = Button(image = check_img, highlightthickness = 0, bg = BACKGROUND_COLOR,
                   command = know_the_word)
known_btn.grid(row = 1, column = 1)

show_word()

# @formatter:off

window.mainloop()
