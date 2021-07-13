"""
-----
Day 22 Project: Pong
-----
Paddle can go up and down only
Ball that bounces back and forth (bounces from paddle and top/bottom of screen.
    If paddle misses ball, it returns to center and point scored
        Which direction to send it after scoring?
Need a final score situation to get winner
"""
from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self, player_num, screen, x_loc, y_loc, key_up, key_down):
        super().__init__("square")

        # No drawing
        self.penup()

        # White paddle
        self.color("white")

        # Make shape as rectangle and rotate it correctly
        self.shapesize(1, 5)
        self.setheading(90.0)

        # Assign event handlers
        screen.onkey(self.move_up, key_up)
        screen.onkey(self.move_down, key_down)

        # Move paddle to start location
        self.goto(x_loc, y_loc)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)


class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.setup()

    def setup(self):
        self.speed("fastest")
        self.penup()
        self.shapesize(0.75, 0.75)
        self.color("white")

    def move(self):
        # TODO
        pass


class Score(Turtle):
    def __init__(self, player_num, screen_height):
        super().__init__()
        self.score = 0
        self.setup(player_num, screen_height)

    def setup(self, player_num, screen_height):
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.goto(player_num == 1 and -50 or 50, screen_height/2 - 50)
        self.write(f"{self.score}", False, align="center", font=("Monospace", 24, "normal"))

    def add_point(self, player_num):
        # TODO
        pass


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
    # Turn off animation
    s.tracer(0)
    s.listen()

    # Make scores
    player_1_score = Score(1, SCREEN_HEIGHT)
    player_2_score = Score(2, SCREEN_HEIGHT)

    # Make DMZ line
    dmz = DMZ(SCREEN_HEIGHT)

    # Create paddles
    player_1_paddle = Paddle(1, s, -350, 0, "w", "s")
    player_2_paddle = Paddle(2, s, 350, 0, "Up", "Down")

    # Create ball
    ball = Ball()

    # Manually update animation
    game = True
    while game:
        s.update()

    s.exitonclick()


if __name__ == "__main__":
    main()
