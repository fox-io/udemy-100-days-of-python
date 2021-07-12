"""
-----
Day 22 Project: Pong
-----

Two scores - left and right player
Two paddles - left and right player
    Paddle can go up and down only
Dashed line across middle
Ball that bounces back and forth (bounces from paddle and top/bottom of screen.
    If paddle misses ball, it returns to center and point scored
        Which direction to send it after scoring?
Need a final score situation to get winner

"""
from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self, player_num):
        super().__init__("square")
        self.setup(player_num)

    def setup(self, player_num):
        # No drawing
        self.penup()

        # White paddle
        self.color("white")

        # Make shape as rectangle
        self.shapesize(3, 1)

        # Send player 1 left and 2 right
        self.goto(player_num == 1 and -380 or 380, 0)


class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.setup()

    def setup(self):
        self.penup()
        self.shapesize(0.75, 0.75)
        self.color("white")


class Score(Turtle):
    def __init__(self, player_num, screen_height):
        super().__init__()
        self.score = 0
        self.setup(player_num, screen_height)

    def setup(self, player_num, screen_height):
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(player_num == 1 and -50 or 50, screen_height/2 - 50)
        self.write(f"{self.score}", False, align="center", font=("Consolas", 32, "normal"))


class DMZ(Turtle):
    def __init__(self, screen_height):
        super().__init__("square")
        self.setup()
        self.draw(screen_height)

    def setup(self):
        # Small square shape
        self.color("white")
        self.shapesize(0.25, 0.25, 0)
        self.pensize(5)

        # We don't need visible animation. Make it fastest.
        self.speed("fastest")

    def draw(self, screen_height):
        # Go to top of screen, center
        self.penup()
        self.goto(0, screen_height / 2)

        # Create dashed line from top to bottom of play area
        while self.ycor() > -(screen_height / 2):
            # Draw 10px
            self.pendown()
            self.goto(0, self.ycor() - 10)
            # Move 10px
            self.penup()
            self.goto(0, self.ycor() - 10)


def main():
    # Play area will be 800x600
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    # Readable headings
    NORTH = 90.0
    EAST = 0.0
    SOUTH = 270.0
    WEST = 180.0

    # Create play area
    s = Screen()
    s.title("Pong")
    s.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    s.bgcolor("black")

    # Make scores
    player_1_score = Score(1, SCREEN_HEIGHT)
    player_2_score = Score(2, SCREEN_HEIGHT)

    # Make DMZ line
    dmz = DMZ(SCREEN_HEIGHT)

    # Create paddles
    player_1 = Paddle(1)
    player_2 = Paddle(2)

    # Create ball
    ball = Ball()

    s.exitonclick()


if __name__ == "__main__":
    main()
