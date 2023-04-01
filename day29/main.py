from tkinter import *
from tkinter import messagebox as mb
from random import *

BLACK = '#fff'
TEXT = '#000'
FONT = ('Arial', 13, 'bold')
PADX = 5
PADY = 13


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
               'p',
               'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E',
               'F',
               'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V',
               'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = ''.join(password_list)
    if len(password_e.get()) <= 0:
        password_e.insert(0, password)
    else:
        password_e.delete(0, END)
        password_e.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# todo:collect user input
# todo:create file data.txt
# todo: add input in file > website | mail | password > next entry in new line

def write_data(web: str, mail: str, password: str):
    if len(web) <= 0 or len(mail) <= 0 or len(password) <= 0:
        mb.showwarning(title = 'Oops!', message = "Please provide all details", )
    else:
        is_ok = mb.askokcancel(title = web,
                               message = f"details \n Email : {mail}\n Password: {password} are u sure?")
        if is_ok:
            with open('data.txt', mode = 'a') as data:
                data.write(f"{web} | {mail} | {password}\n")
            clear_entry()


def user_inputs():
    write_data(website_e.get(), email_e.get(), password_e.get())


def clear_entry():
    website_e.delete(0, END)
    password_e.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.minsize(width = 600, height = 500)
window.config(bg = BLACK, padx = 50, pady = 50)
window.title('Password Manager')
# 200,189


# canvas
canvas = Canvas(width = 210, height = 210)
logo = PhotoImage(file = 'logo.png')
canvas.create_image(105, 105, image = logo, anchor = 'center')
canvas.config(bg = BLACK, highlightthickness = 0, )
canvas.grid(column = 1, row = 0, sticky = NSEW)

# labels
website_l = Label(text = 'Website:', bg = BLACK, fg = TEXT, font = FONT)
website_l.grid(column = 0, row = 1)
email_l = Label(text = 'Email/Username:', bg = BLACK, fg = TEXT, font = FONT)
email_l.grid(column = 0, row = 2)
password_l = Label(text = 'Password:', bg = BLACK, fg = TEXT, font = FONT)
password_l.grid(column = 0, row = 3)

# buttons
generate_p_b = Button(text = 'Generate Password', font = FONT, activebackground =
'darkgreen', activeforeground = BLACK, command = generate_password)

generate_p_b.grid(column = 2, row = 3, pady = PADY)
add_b = Button(text = 'Add', width = 38, font = FONT, command = user_inputs)
add_b.grid(column = 1, row = 4, columnspan = 2, sticky = NSEW, pady = PADY)

# Entry
website_e = Entry(width = 37)
website_e.grid(column = 1, row = 1, columnspan = 2, sticky = NSEW, pady = PADY)
website_e.focus()
email_e = Entry(width = 37)
email_e.insert(END, 'jondoe@moon.mo')
email_e.grid(column = 1, row = 2, columnspan = 2, sticky = NSEW, )
password_e = Entry(width = 21, )
password_e.grid(column = 1, row = 3, sticky = NSEW, pady = PADY)

# @formatter:off




window.mainloop()
