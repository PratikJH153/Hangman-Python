from turtle import Turtle
FONT = ("Arial", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self, lives):
        super().__init__()
        self.speed("fastest")
        self.lives = lives
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=0, y=300)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Lives: {self.lives}", align="center", font=FONT)

    def lives_score(self):
        self.lives -= 1
        self.clear()
        self.write(f"Lives: {self.lives}", align="center", font=FONT)