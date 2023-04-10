from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
PADDING = 40
FONT = ("Georgia ", 20, "italic")


class QuizGui:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("The Brain Drain")
        self.up_wind()
        self.score = Label()
        self.text()

        self.canvas = Canvas()
        self.q_text = None
        self.up_canvas()
        self.__green_img = PhotoImage(file="./images/true.png")
        self.__red_img = PhotoImage(file="./images/false.png")
        self.green = Button(
            image=self.__green_img, highlightthickness=0, command=self.true_ans
        )
        self.red = Button(
            image=self.__red_img, highlightthickness=0, command=self.false_ans
        )
        self.get_question()
        self.configs()

        self.window.mainloop()

    def up_wind(self):
        self.window.config(bg=THEME_COLOR, padx=PADDING, pady=PADDING)

    def up_canvas(self):
        self.canvas.config(height=400, width=350, bg="#fff")
        self.q_text = self.canvas.create_text(
            175, 200, text="soda", font=FONT, fill=THEME_COLOR, width=300
        )

    def text(self):
        self.score.config(font=FONT, fg="#fff", bg=THEME_COLOR, text=f"Score : 0")

    def configs(self):
        self.canvas.grid(column=0, row=1, columnspan=2, pady=PADDING)
        self.red.grid(column=1, row=2)
        self.green.grid(column=0, row=2)
        self.score.grid(column=1, row=0)

    def get_question(self):
        self.clear_screen()
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score.config(text=f"score: {self.quiz.score}")
            self.canvas.itemconfig(self.q_text, text=q_text)
        else:
            self.canvas.itemconfig(self.q_text, text="this is it...")
            self.green.config(state="disabled")
            self.red.config(state="disabled")

    def true_ans(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_ans(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        self.window.after(1000, self.get_question)
        if is_right:
            self.canvas.config(bg="#357C3C")
            self.canvas.itemconfig(self.q_text, fill="#fff")
        else:
            self.canvas.config(bg="#F96666")
            self.canvas.itemconfig(self.q_text, fill="#fff")

    def clear_screen(self):
        self.canvas.itemconfig(self.q_text, fill=THEME_COLOR)
        self.canvas.config(bg="#fff")
