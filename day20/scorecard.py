from turtle import Turtle

ALIGN = "center"
FONT = ("monospace", 20, "bold")


class Score_card(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        with open('./data.txt', mode = 'r') as score:
            contents = score.read()
            self.high_score = int(contents)
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
            with open('data.txt', mode = 'w') as score_d:
                score_d.write(str(self.score))

        self.score = 0
        self.update()

    def increase_score(self):
        self.score += 1
        self.update()
