from turtle import Turtle

ALIGN = "center"
FONT = ("monospace", 20, "bold")


class Score_card(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.high_score = 0
        self.penup()
        self.goto(0, 360)
        self.color("aqua")
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"score :  {self.score}  High Score: {self.high_score}", align = ALIGN,
                   font = FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color("red")
    #     self.write("! Game Over", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update()

    def increase_score(self):
        self.score += 1
        self.update()
