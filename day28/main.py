import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timers = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timers)
    timer.config(text = 'TIMER')
    canvas.itemconfig(timer_text, text = '00:00')
    ticks.config(text = '')
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_update(text, color):
    timer.config(text = text, fg = color)


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # if 8 long break
    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_update('BREAK', RED)
        # if 2/4/6 short
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_update('BREAK', PINK)


    # if 1/3/5/7 work
    elif reps % 2 != 0:
        countdown(work_sec)
        timer_update('WORK', GREEN)


# ---------------------------- COUNTDOWN MECHANISM
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = (count % 60)
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        global timers
        timers = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ''
        for _ in range(math.floor(reps / 2)):
            marks += "✓"
        ticks.config(text = marks)


# ---------------------------- UI SETUP
window = Tk()
window.title('Pomodoro')
window.minsize(width = 500, height = 400)
window.config(pady = 50, padx = 100, bg = YELLOW)

canvas = Canvas(width = 210, height = 230, bg = YELLOW, highlightthickness = 0)
tomato_img = PhotoImage(file = 'tomato.png')
canvas.create_image(105, 115, image = tomato_img)
timer_text = canvas.create_text(105, 135, text = '00:00', fill = '#fff',
                                font = (FONT_NAME,
                                        34,
                                        'bold'))
canvas.grid(column = 1, row = 1)

timer = Label(text = 'Timer', fg = GREEN, font = (FONT_NAME, 30, 'bold'), bg = YELLOW)
timer.grid(column = 1, row = 0)

start = Button(text = 'Start', width = 8, highlightthickness = 0, command = start_timer)
start.grid(column = 0, row = 2)

reset = Button(text = "reset", width = 8, highlightthickness = 0, command = reset_timer)
reset.grid(column = 2, row = 2)

ticks = Label(fg = GREEN, bg = YELLOW, font = (FONT_NAME, 20, 'bold'))
ticks.grid(column = 1, row = 3, )

window.mainloop()
