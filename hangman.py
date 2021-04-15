from turtle import Turtle


class Hangman(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x=-100, y=-300)
        self.pendown()
        self.color("white")
        self.draw_hangman()
        self.man_segments = [self.r_foot, self.l_foot, self.r_hand,
                             self.l_hand, self.body, self.head]

    def draw_hangman(self):
        self.goto(x=-150, y=-300)
        self.goto(x=-125, y=-300)
        self.goto(x=-125, y=100)
        self.goto(x=30, y=100)
        self.goto(x=30, y=30)

    def head(self):
        self.penup()
        self.goto(x=30, y=-30)
        self.pendown()
        self.circle(30)

    def body(self):
        self.right(90)
        self.forward(120)
        self.left(180)
        self.forward(70)

    def l_hand(self):
        self.left(60)
        self.forward(50)
        self.right(180)
        self.forward(50)

    def r_hand(self):
        self.left(60)
        self.forward(50)
        self.right(180)
        self.forward(50)
        self.left(60)
        self.forward(70)

    def l_foot(self):
        self.right(60)
        self.forward(50)
        self.right(180)
        self.forward(50)

    def r_foot(self):
        self.right(60)
        self.forward(50)
        self.right(180)
        self.forward(50)