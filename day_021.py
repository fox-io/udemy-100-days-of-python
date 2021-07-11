"""
-----
Day 21 Project: Snake Game, pt 2
-----

Day 1:
1. Create snake body
2. Move the snake
3. Control the snake

Day 2:
1. Detect collision with food
2. Create scoreboard
3. Detect collision with wall
4. Detect collision with self

Classes: Snake, Food, Score

(c)2021 John Mann <gitlab.fox-io@foxdata.io>
"""
from turtle import Turtle, Screen
from random import randint
from time import sleep


class Snake:
    body = []
    speed = 0.1

    def __init__(self):
        for starting_position in [(0, 0), (-20, 0), (-40, 0)]:
            self.add_segment(starting_position)

    def add_segment(self, pos):
        t = Turtle("square")
        t.penup()
        t.color("white")
        t.setpos(pos)
        self.body.append(t)

    def grow(self):
        self.add_segment(self.body[-1].position())

    def update(self):
        for segment in range(len(self.body) - 1, 0, -1):
            new_x = self.body[segment - 1].xcor()
            new_y = self.body[segment - 1].ycor()
            self.body[segment].goto(new_x, new_y)

    def move(self, f):
        self.body[0].forward(20)
        turtle_x = self.body[0].xcor()
        turtle_y = self.body[0].ycor()

        # Detect collision
        distance_from_food = self.body[0].distance(f)
        if distance_from_food < 20:
            return 1
        if turtle_x < -290 or turtle_x > 290 or turtle_y < -290 or turtle_y > 290:
            return 3
        for segment in self.body[1:]:
            if self.body[0].distance(segment) < 15:
                return 2
        return 0

    def head_north(self):
        if self.body[0].heading() == 0.0 or self.body[0].heading() == 180.0:
            self.body[0].setheading(90.0)

    def head_west(self):
        if self.body[0].heading() == 90.0 or self.body[0].heading() == 270.0:
            self.body[0].setheading(180.0)

    def head_south(self):
        if self.body[0].heading() == 180.0 or self.body[0].heading() == 0.0:
            self.body[0].setheading(270.0)

    def head_east(self):
        if self.body[0].heading() == 270.0 or self.body[0].heading() == 90.0:
            self.body[0].setheading(0.0)


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("green")
        self.speed("fastest")

        self.respawn()

    def respawn(self):
        """Generating random coordinates for the food location.

        * 280 is the min/max playing area in which the turtle will be fully visible.
        """
        pos_x = randint(-280, 280)
        pos_y = randint(-280, 280)
        self.goto(pos_x, pos_y)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.goto(0, 280)
        self.score = 0
        self.update_text()

    def add_point(self):
        self.score += 1
        self.update_text()

    def update_text(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align="center", font=("Arial", 14, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, align="center", font=("Arial", 14, "normal"))


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake")
    screen.tracer(0)
    snake = Snake()
    score = Score()
    food = Food()

    screen.onkeypress(snake.head_north, "w")
    screen.onkeypress(snake.head_west, "a")
    screen.onkeypress(snake.head_south, "s")
    screen.onkeypress(snake.head_east, "d")
    screen.listen()

    power = True
    while power:
        screen.update()
        sleep(snake.speed)
        snake.update()
        nom_nom = snake.move(food)
        if nom_nom == 1:
            # Food collision
            score.add_point()
            snake.grow()
            food.respawn()
        elif nom_nom == 2:
            # Body collision
            score.game_over()
            break
        elif nom_nom == 3:
            # Wall collision
            score.game_over()
            break

    screen.exitonclick()


if __name__ == "__main__":
    main()
