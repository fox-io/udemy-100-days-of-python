"""
Day 23: Turtle Crossing
(c)2021 John Mann <gitlab.fox-io@foxdata.io>
"""
from turtle import Turtle, Screen
from random import randint
from time import sleep


class Car(Turtle):
    colors = ["red", "yellow", "green", "blue", "purple"]

    def __init__(self):
        super().__init__("square")
        self.penup()
        self.speed = 0
        self.shapesize(stretch_wid=2, stretch_len=1)
        self.setheading(90)

        # Activate
        self.respawn(True)

    def move(self, level):
        # Move according to speed
        self.goto(self.xcor() - (self.speed * (1 + (level * 0.1))), self.ycor())

        # If we are off the screen, respawn
        if self.xcor() < -320:
            self.respawn(False)

    def respawn(self, new_level):
        self.color(self.colors[randint(0, 4)])
        self.speed = randint(5, 20)
        if new_level:
            x_spawn = randint(-320, 320)
        else:
            x_spawn = 320
        self.goto(x_spawn, randint(-220, 220))


class Player(Turtle):
    def __init__(self):
        super().__init__("turtle")
        self.setheading(90.0)
        self.penup()
        self.respawn()

    def move_forward(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def respawn(self):
        self.goto(0, -250)


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


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(0, 0)
        self.clear()
        self.write("Game Over", False, align="center", font=("Monospace", 32, "normal"))


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

        # Add cars
        self.cars = {
            Car(),
            Car(),
            Car(),
            Car(),
            Car(),
            Car(),
            Car(),
            Car(),
            Car(),
            Car(),
        }

    def update(self):
        # Process level up
        if self.player.ycor() > 250:
            self.level.set(self.level.get() + 1)
            self.player.respawn()
            for car in self.cars:
                car.respawn(True)

        # Move cars
        for car in self.cars:
            car.move(self.level.get())
            if car.distance(self.player) < 20:
                gg = GameOver()
                self.running = False

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
