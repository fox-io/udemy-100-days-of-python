"""
Practice projects for Day 2

(c)2021 John Mann <gitlab.fox-io@foxdata.io>

1. BMI Calculator metric/imperial
"""


def bmi_calculator():
    """
    BMI Calculator

    Calculates the BMI of a person based on their height and weight.

    We can calculate using either metric or imperial systems as follows:
    BMI = kg/m^2
    BMI = 703(lb/in^2)
    """

    number_system = int(input("Enter 1 for metric and 2 for imperial: "))
    weight = float(input("What is the weight? "))
    height = float(input("What is the height? "))
    bmi = weight / (height * height)
    if number_system == 2:
        bmi = bmi * 703
    print(f"Your BMI is: {bmi:.2f}")


bmi_calculator()
