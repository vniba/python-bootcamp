from tkinter import *

PADX = 15
PADY = 10

FONT = ('monospace', 20)


def convert():
    miles = text.get()
    kms = round(float(miles) * 1.609)
    outputs.config(text = f"{kms}")


window = Tk()
window.title('MIle to Km')
window.minsize(width = 500, height = 400)
window.config(padx = 50, pady = 50)

# labels
mile = Label(text = 'Miles', font = FONT)
mile.grid(column = 2, row = 0, pady = PADY, padx = PADX)

equal = Label(text = 'is equal to', font = FONT)
equal.grid(column = 0, row = 1, padx = PADX, pady = PADY)

km = Label(text = 'Km', font = FONT)
km.grid(column = 2, row = 1, padx = PADX, pady = PADY)

out = 0
outputs = Label(text = out, font = FONT)
outputs.grid(column = 1, row = 1, padx = PADX, pady = PADY)

text = Entry(font = FONT, width = 6, )
text.grid(column = 1, row = 0, padx = PADX, pady = PADY)

btn = Button(text = 'Calculate', font = FONT, bg = 'deeppink', command = convert)
btn.grid(column = 1, row = 2, padx = PADX, pady = PADY)
window.mainloop()
