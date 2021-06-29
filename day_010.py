class Date:
    """
    Created with enough functionality to determine the number
    of days in a month of a certain year.
    """
    year = 0
    month = 0
    day = 0

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def is_leap_year(self):
        if self.year % 4 == 0:
            if self.year % 100 == 0:
                if self.year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def max_days_in_month(self):
        days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.is_leap_year():
            days_per_month[1] = 29
        else:
            days_per_month[1] = 28
        return days_per_month[self.month - 1]


class Calculator:
    """
    Day 10 Project: Calculator

    enter a number
    loop:
        enter an operator
        enter second number
        show result
        continue y/n
    """

    result = 0
    left_number = 0
    right_number = 0
    operator = ""

    def clear(self):
        self.result = 0

    def calculate(self):
        if self.operator == "-":
            self.result = self.left_number - self.right_number
        elif self.operator == "+":
            self.result = self.left_number + self.right_number
        elif self.operator == "*":
            self.result = self.left_number * self.right_number
        elif self.operator == "/":
            if self.right_number == 0:
                # Prevent division by zero error.
                self.result = 0
            else:
                self.result = self.left_number / self.right_number
        return self.result


def main():
    while True:
        # Day 10 menu
        menu_choice = int(input("[1] Days per month\n[2] Calculator\n[0] Quit\n: "))
        if menu_choice == 1:
            # Days per month

            # Get the month and year from the user.
            the_month = int(input("Enter the month: "))
            the_year = int(input("Enter the year: "))

            # Create a Date object using these values.
            # Using 1 for the day, as it does not matter for this script.
            date = Date(the_year, the_month, 1)

            # Call our max days in month function.
            print(date.max_days_in_month())

        elif menu_choice == 2:
            # Calculator

            # Create a calculator object
            c = Calculator()

            # Set the left number by asking the user for a number
            c.left_number = float(input("Enter the first number: "))

            # We start a loop, which will continue until the user types 0 to quit.
            # This allows our result to become our new left value.
            while True:
                # Set the operator. The user can also choose to exit the calculator.
                c.operator = input("Enter the operator [-, +, *, /, 0 to quit]: ")

                # Quit if requested
                if c.operator == "0":
                    break

                # Set the right number to our user input
                c.right_number = float(input("Enter the second number: "))

                # Calculate our result and display it to the user.
                c.calculate()
                print(c.result)

                # Set the left number to the result before looping.
                # This allows continued calculation using the previous result.
                c.left_number = c.result

        elif menu_choice == 0:
            # Exits program
            break


# Main program
if __name__ == "__main__":
    main()
