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
from random import randint
import time


class Snake:
    body = []
    speed = 0.2

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


def ontimer():
    pass


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake")
    screen.tracer(0)
    snake = Snake()

    power = True
    while power:
        screen.update()
        time.sleep(snake.speed)
        snake.update()
        snake.move()

    screen.exitonclick()


if __name__ == "__main__":
    main()
