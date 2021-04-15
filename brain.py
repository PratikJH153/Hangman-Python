from turtle import Turtle
import random
from hangman import Hangman
from scoreboard import Scoreboard

lives = 6

FONT = ("Arial", 20, "normal")
WORDS = ['Pratik', 'Shreyash', 'Yash', 'Aayush', 'Atharv']

scoreboard = Scoreboard(lives)
hangman = Hangman()


class Brain(Turtle):
    def __init__(self):
        super().__init__()
        self.game_on = True
        self.random_word = random.choice(WORDS).lower()
        self.display = ["_"] * len(self.random_word)
        print(self.random_word)
        self.speed("fastest")
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=0, y=200)
        self.update_display()

    def update_display(self):
        self.goto(x=0, y=200)
        self.write('   '.join(self.display), align="center", font=FONT)

    def display_info(self, text):
        self.goto(x=0, y=150)
        self.write(text, align="center", font=("Arial", 12, "normal"))

    def brain_of_game(self, guess):
        if guess in self.display:
            self.clear()
            self.display_info(f"You've already guessed {guess}.")
            self.update_display()

        elif guess in self.random_word:
            for position in range(len(self.random_word)):
                if guess == self.random_word[position]:
                    self.display[position] = guess
                    self.clear()
                    self.update_display()
                    self.display_info("You've guessed it right!")

        else:
            global lives
            lives -= 1
            self.clear()
            self.update_display()
            self.display_info("You've guessed it wrong.")
            scoreboard.lives_score()
            hangman.man_segments[lives]()

        if lives == 0:
            self.game_on = False
            self.clear()
            self.update_display()
            self.display_info(f"You Lose, The word is {self.random_word}")

        if '_' not in self.display:
            self.clear()
            self.update_display()
            self.display_info("You Won!")
            self.game_on = False
