"""
-----
Day 22 Project: Pong
-----
"""
from turtle import Turtle, Screen
from time import sleep


class Paddle(Turtle):
    def __init__(self, screen, x_loc, y_loc, key_up, key_down):
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
        self.speed("slow")
        self.penup()
        self.shapesize(1, 1)
        self.color("white")
        self.setheading(45.0)
        self.goto(0, 0)
        self.x_movement = 10
        self.y_movement = 10

    def move(self):
        self.goto(self.xcor() + self.x_movement, self.ycor() + self.y_movement)

    def bounce(self, axis):
        if axis == "y":
            self.y_movement *= -1
        else:
            self.x_movement *= -1

    def respawn(self):
        self.bounce("x")
        self.goto(0, 0)


class Score(Turtle):
    def __init__(self, player_num, screen_height):
        super().__init__()
        self.score = 0
        self.screen_height = screen_height
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.goto(player_num == 1 and -50 or 50, self.screen_height / 2 - 50)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.score}", False, align="center", font=("Monospace", 24, "normal"))

    def add_point(self):
        self.score += 1
        self.update_score()


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 0)
        self.clear()
        self.write("Game Over", False, align="center", font=("Monospace", 32, "normal"))


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


class Pong:
    def __init__(self, width, height):
        # Save these values so we can use them later
        self.screen_width = width
        self.screen_height = height

        # Create play area with proper dimensions, background color and window title.
        self.screen = Screen()
        self.screen.setup(self.screen_width, self.screen_height)
        self.screen.bgcolor("black")
        self.screen.title("Pong")

        # Disable animation updates so we can hide some movements from the player.
        self.screen.tracer(0)

        # Listen for events
        self.screen.listen()

        # Add score objects
        self.score_p1 = Score(1, self.screen_height)
        self.score_p2 = Score(2, self.screen_height)

        # Add DMZ line
        self.dmz = DMZ(self.screen_height)

        # Add player paddles
        self.paddle_p1 = Paddle(self.screen, -350, 0, "w", "s")
        self.paddle_p2 = Paddle(self.screen, 350, 0, "Up", "Down")

        self.ball = Ball()

    def update(self):
        # Set game speed to playable speed
        sleep(0.05)

        # Move the ball to its new location
        self.ball.move()

        # Bounce the ball if it hits the top or bottom of screen.
        # If ball hits left or right of screen, add appropriate points.
        if self.ball.ycor() > 280 or self.ball.ycor() < -280:
            self.ball.bounce("y")
        elif self.ball.xcor() >= 340 and self.ball.distance(self.paddle_p2) < 50:
            self.ball.bounce("x")
        elif self.ball.xcor() >= 380:
            self.score_p1.add_point()
            self.ball.respawn()
        elif self.ball.xcor() <= -340 and self.ball.distance(self.paddle_p1) < 50:
            self.ball.bounce("x")
        elif self.ball.xcor() < -380:
            self.score_p2.add_point()
            self.ball.respawn()

        if self.score_p1.score >= 3 or self.score_p2.score >= 3:
            game_over = GameOver()
            return False

        # Update animation
        self.screen.update()

        return True


def main():
    game = Pong(width=800, height=600)

    running = True
    while running:
        running = game.update()

    game.screen.exitonclick()


if __name__ == "__main__":
    main()
