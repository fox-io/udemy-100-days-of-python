"""
Day 4 Project: Rock-Paper-Scissors

(c)2021 John Mann <gitlab.fox-io@foxdata.io>
"""


import random


print("Rock, Paper, Scissors")

user_choice = int(input("Rock, Paper, Scissors? [1, 2, or 3]"))

pc_choice = random.randint(1, 3)

if user_choice == 1:
    print("You chose: Rock")
elif user_choice == 2:
    print("You chose: Paper")
elif user_choice == 3:
    print("You chose: Scissors")

if pc_choice == 1:
    print("Computer chose: Rock")
elif pc_choice == 2:
    print("Computer chose: Paper")
elif pc_choice == 3:
    print("Computer chose: Scissors")

if user_choice == 1:
    if pc_choice == 1:
        print("Tie!")
    elif pc_choice == 2:
        print("You lose!")
    else:
        print("You win!")
elif user_choice == 2:
    if pc_choice == 1:
        print("You win!")
    elif pc_choice == 2:
        print("Tie!")
    else:
        print("You lose")
elif user_choice == 3:
    if pc_choice == 1:
        print("You lose!")
    elif pc_choice == 2:
        print("You win!")
    else:
        print("Tie!")
