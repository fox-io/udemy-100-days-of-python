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


# bmi_calculator()

"""
Tip Calculator
--------------
Calculates tip amount for a bill. Allows for splitting the bill.

(c)2021 John Mann <gitlab.fox-io@foxdata.io>
"""


# Unnecessary title
print("Tip Calculator\n")

# Gather input
bill_total = float(input("Bill total: "))
num_shares = float(input("How many shares? (default = 1): ") or "1")
tip_percent = float(input("What percentage to tip? (default = 15%): ") or "15")

# Perform calculations
bill_share = bill_total / num_shares
tip_amount = bill_share * (tip_percent / 100)
total_share = bill_share + tip_amount

# Display information
print(f"\nThe grand total is {(total_share * num_shares):.2f}")
print(f"Each share is ${bill_share + tip_amount:.2f} (${bill_share:.2f} + ${tip_amount:.2f} tip).")
