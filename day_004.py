import random


def show_random_integer():
    # Integers
    random_number = random.randint(1, 5)
    print(random_number)


def show_random_float():
    # Float 0.0 - 0.99999...
    random_float = random.random()
    print(random_float)


def flip_coin():
    coin = ("Heads", "Tails")
    result = random.randint(0, 1)
    print(f"The coin toss is: {coin[result]}")


def list_functions():
    a_list = ["red", "green", "blue"]
    a_list[1] = "orange"
    a_list.append("yellow")
    a_list.extend(["purple", "brown", "pink"])
    print(a_list)


def bankers_roulette():
    name_input = input("Type everyone's name, separated by commas: ")
    bankers = name_input.split(", ")
    # bankers = ["John", "Mary", "Dan", "Angela"]
    random_banker = random.randint(0, len(bankers) - 1)
    print(bankers[random_banker])


def treasure_map():
    my_map = [["🟫", "🟫", "🟫"], ["🟫", "🟫", "🟫"], ["🟫", "🟫", "🟫"]]
    print(f"1 {my_map[0]}\n2 {my_map[1]}\n3 {my_map[2]}\n    1     2     3")
    print("Enter where you would like to place your treasure.")
    treasure_location = input("Enter the location as [row][column] (ie: 12): ")
    my_map[int(treasure_location[0]) - 1][int(treasure_location[-1]) - 1] = "🪙"
    print(f"1 {my_map[0]}\n2 {my_map[1]}\n3 {my_map[2]}\n    1     2     3")


# show_random_integer()

# show_random_float()

# flip_coin()

# list_functions()

# bankers_roulette()

# treasure_map()



"""
Day 4 Project: Rock-Paper-Scissors

(c)2021 John Mann <gitlab.fox-io@foxdata.io>
"""


# import random


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
