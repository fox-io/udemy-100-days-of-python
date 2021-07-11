"""
-----
Day 20 Project: Snake Game, pt 1
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
from random import uniform
import time


class Snake:
    body = []
    speed = 0.1

    def __init__(self):
        for starting_position in range(0, 3):
            t = Turtle("square")
            t.penup()
            t.color("white")
            t.setpos(-20 * starting_position, 0)
            self.body.append(t)

    def update(self):
        for segment in range(len(self.body) - 1, 0, -1):
            new_x = self.body[segment - 1].xcor()
            new_y = self.body[segment - 1].ycor()
            self.body[segment].goto(new_x, new_y)

    def move(self):
        self.body[0].forward(20)

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


class Food:
    def __init__(self):
        self.turtle = Turtle("turtle")
        self.turtle.penup()
        self.turtle.color("green")
        self.respawn()

    def respawn(self):
        """Generating random coordinates for the food location.

        * 280 is the min/max playing area in which the turtle will be fully visible.
        """
        pos_x = uniform(-280, 280)
        pos_y = uniform(-280, 280)
        self.turtle.goto(pos_x, pos_y)


class Score:
    def __init__(self):
        pass


def ontimer():
    pass


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake")
    screen.tracer(0)
    snake = Snake()

    food = Food()

    screen.onkeypress(snake.head_north, "w")
    screen.onkeypress(snake.head_west, "a")
    screen.onkeypress(snake.head_south, "s")
    screen.onkeypress(snake.head_east, "d")
    screen.listen()

    power = True
    while power:
        screen.update()
        time.sleep(snake.speed)
        snake.update()
        snake.move()

    screen.exitonclick()


if __name__ == "__main__":
    main()
