"""
Day 23: Turtle Crossing
(c)2021 John Mann <gitlab.fox-io@foxdata.io>
"""
from turtle import Turtle, Screen
from random import randint
from time import sleep


class Player(Turtle):
    def __init__(self):
        super().__init__("turtle")
        self.setheading(90.0)
        self.penup()
        self.goto(0, -250)

    def move_forward(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_left(self):
        self.goto(self.xcor() - 20, self.ycor())

    def move_right(self):
        self.goto(self.xcor() + 20, self.ycor())


class Level(Turtle):
    def __init__(self):
        super().__init__()
        # Default to level 1
        self.level = 1

        # Hide turtle, move to correct location
        self.hideturtle()
        self.penup()
        self.goto(-250, 270)

        # Manually update on creation
        self.update()

    def set(self, new_level):
        # Set new level and update display
        self.level = new_level
        self.update()

    def get(self):
        return self.level

    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", False, align="center", font=("Monospace", 16, "normal"))


class TurtleCrossing:
    """The main game class."""
    def __init__(self):
        # Create and set up the game window.
        self.running = True
        self.screen = Screen()
        self.screen.setup(600, 600)
        self.screen.tracer(0)
        self.screen.title("Turtle Crossing")

        # Add level indicator
        self.level = Level()

        # Add player
        self.player = Player()

        # Add keybinds
        self.screen.listen()
        self.screen.onkey(self.player.move_forward, "w")
        self.screen.onkey(self.player.move_left, "a")
        self.screen.onkey(self.player.move_right, "d")

    def update(self):
        # Update the screen
        self.screen.update()
        # Exit the game
        # self.running = False


def main():
    game = TurtleCrossing()
    while game.running:
        sleep(0.1)
        game.update()
    game.screen.exitonclick()


# Main program
if __name__ == "__main__":
    main()
