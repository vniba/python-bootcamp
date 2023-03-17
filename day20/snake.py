from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
SNAKE_SPEED = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

        # 1 snake body

    def create_snake(self):
        for p in STARTING_POS:
            self.add_snake(p)

    def add_snake(self, position):
        turt = Turtle("square")
        turt.color("white")
        turt.penup()
        turt.goto(position)
        self.snake.append(turt)

    def reset(self):
        for seg in self.snake:
            seg.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    def extend(self):
        self.add_snake(self.snake[-1].position())

        # moving snake

    def move(self):
        for snake_no in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[snake_no - 1].xcor()
            new_y = self.snake[snake_no - 1].ycor()
            self.snake[snake_no].goto(new_x, new_y)

        self.head.forward(SNAKE_SPEED)

    # control snake

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
