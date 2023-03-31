from tkinter import *

window = Tk()
window.title("moon")
window.minsize(width = 400, height = 300)
window.config(padx = 45, pady = 45)


def button_clicked():
    label.config(text = inputs.get())


# label
label = Label(text = "dark moon", font = ("calibre", 20, "bold"))
label.grid(column = 0, row = 0, padx = 15, pady = 15)

# button

btn = Button()
btn.config(text = 'run', fg = 'red', bg = 'yellow', width = 10, height = 1,
           command = button_clicked)
btn.grid(column = 2, row = 0)

btn2 = Button()
btn2.config(text = 'run me')
btn2.grid(column = 1, row = 1, )

# entry
inputs = Entry(width = 15)
inputs.grid(column = 0, row = 2)
inputs.grid(column = 3, row = 3)

window.mainloop()
