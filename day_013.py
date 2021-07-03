"""
Day 13: Debugging

There was no project to create this day. Rather, we used
deduction skills to remove the bugs in the following code.

"""
# number = int(input("Which number do you want to check?"))
#
# if number % 2 = 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

# number = int(input("Which number do you want to check?"))
#
# if number % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

# year = input("Which year do you want to check?")
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")

# year = int(input("Which year do you want to check?"))
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
