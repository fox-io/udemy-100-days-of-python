"""
-----
Day 18 Project: Turtle
-----

(c)2021 John Mann <gitlab.fox-io@foxdata.io>
"""
from turtle import Turtle, Screen
import random


# Shapes with 3-10 sides, random colors
# def main():
#     t = Turtle()
#     for sides in range(3, 11):
#         t.color((random.random(), random.random(), random.random()))
#         for _ in range(0, sides):
#             t.forward(100)
#             t.right(360/sides)
#
#     screen = Screen()
#     screen.exitonclick()

# # Random Walk
# def main():
#     t = Turtle()
#     t.width(5)
#     t.speed(0)
#
#     # Do 100 walks
#     for walk_num in range(200):
#
#         # Face random direction
#         turns = random.randint(1, 4)
#         # print(f"{walk_num}/100: Turning {turns} times.")
#         for _ in range(turns):
#             t.right(90)
#
#         # Pick random color
#         t.color((random.random(), random.random(), random.random()))
#
#         # Draw walk
#         t.forward(20)
#
#     s = Screen()
#     s.exitonclick()

# # Spirograph
# def main():
#     t = Turtle()
#     t.speed(0)
#
#     # Make 36 circles, 10 degrees
#     for deg in range(0, 360, 5):
#         t.color((random.random(), random.random(), random.random()))
#         t.setheading(float(deg))
#         t.circle(100)
#
#     s = Screen()
#     s.exitonclick()

# Hirst Painting
def main():
    start_row = 300
    start_col = 300
    circle_size = 10
    circle_distance = 40
    t = Turtle()
    t.speed(0)

    for row in range(10):
        for col in range(10):
            t.penup()
            t.goto(((row + 1) * circle_distance) - start_row, ((col + 1) * circle_distance) - start_col)
            r_color = (random.random(), random.random(), random.random())
            t.color(r_color)
            t.fillcolor(r_color)
            t.setheading(180.0)
            t.pendown()
            t.begin_fill()
            t.circle(circle_size)
            t.end_fill()
            t.penup()

    s = Screen()
    s.exitonclick()


if __name__ == "__main__":
    main()
