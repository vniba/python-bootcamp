from turtle import Turtle

ALIGN = "center"
FONT = ("serif", 40, 'italic')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-75, 300)
        self.write(self.l_score, align = ALIGN, font = FONT)
        self.goto(75, 300)
        self.write(self.r_score, align = ALIGN, font = FONT)

    def l_point(self):
        self.l_score += 1
        self.update()

    def r_point(self):
        self.r_score += 1
        self.update()
