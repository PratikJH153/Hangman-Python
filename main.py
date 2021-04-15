from turtle import Screen
from brain import Brain
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Hangman")
screen.setup(width=700, height=700)

brain = Brain()

while brain.game_on:
    guess = screen.textinput("Guess a word", None)
    brain.brain_of_game(guess.lower())

    time.sleep(1)


screen.exitonclick()
