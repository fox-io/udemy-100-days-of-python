"""
Day 23: Turtle Crossing
(c)2021 John Mann <gitlab.fox-io@foxdata.io>
"""
from turtle import Turtle, Screen
from random import randint
from time import sleep


class TurtleCrossing:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(600, 600)
        self.screen.tracer(0)

    def update(self):
        self.screen.update()
        return False


def main():
    game = TurtleCrossing()
    running = True
    while running:
        sleep(0.1)
        running = game.update()
    game.screen.exitonclick()


# Main program
if __name__ == "__main__":
    main()
