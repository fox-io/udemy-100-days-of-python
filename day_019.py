"""
-----
Day 19 Project: Turtle Race
-----

(c)2021 John Mann <gitlab.fox-io@foxdata.io>
"""
from turtle import Turtle, Screen
import random

racing_turtles = {}

turtle_colors = ["red", "yellow", "green", "blue", "purple"]

for num in range(5):
    racing_turtles[num] = Turtle()
    t = racing_turtles[num]
    t.shape("turtle")
    t.color(turtle_colors[num])
    t.penup()
    t.goto(-200.0, -50.0 + (num * 20))
    t.pendown()

s = Screen()
s.setup(width=500, height=400)

bet = s.textinput(title="Bet", prompt="Enter a turtle color: ")


def on_timer():
    random_turtle = random.randint(0, 4)
    rt = racing_turtles[random_turtle]
    rt.forward(10)
    if not rt.xcor() >= 200:
        s.ontimer(fun=on_timer, t=100)
    else:
        print(f"{rt.pencolor()} wins!")
        if bet == rt.pencolor():
            print("You chose the winning turtle!")
        else:
            print("Your turtle didn't win this time.")


s.ontimer(fun=on_timer, t=100)

s.exitonclick()

# Practice Day 19: Etch-A-Sketch
# from turtle import Turtle, Screen
#
# t = Turtle()
# s = Screen()
#
#
# def move_forward():
#     t.forward(10)
#
#
# def move_backward():
#     t.backward(10)
#
#
# def circle_left():
#     t.circle(100, 10)
#
#
# def circle_right():
#     t.circle(-100, 10)
#
#
# def clear_screen():
#     t.penup()
#     t.home()
#     t.pendown()
#     s.clear()
#
#
# s.listen()
# s.onkey(key="w", fun=move_forward)
# s.onkey(key="s", fun=move_backward)
# s.onkey(key="a", fun=circle_left)
# s.onkey(key="d", fun=circle_right)
# s.onkey(key="c", fun=clear_screen)
#
# s.exitonclick()
