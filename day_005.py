"""
Day 5 Practice
"""
import random


def for_loop():
    names = ["Karen", "Bob", "Joe"]
    for name in names:
        print(name)


# for_loop()


def average_height():
    total_heights = 0
    heights = input("Enter a list of heights, separated by spaces: ").split()
    for height in range(0, len(heights)):
        # Convert heights from strings to ints
        heights[height] = int(heights[height])
        # Add up the total of all heights
        total_heights = total_heights + int(heights[height])
    print(heights)
    # Calculate average. format as integer
    print(f"Average Height: {int(total_heights/len(heights))}")


# average_height()


def high_score():
    highest_score = 0
    scores = input("Enter a list of scores, separated by spaces: ").split()
    for score in range(0, len(scores)):
        scores[score] = int(scores[score])
        if scores[score] > highest_score:
            highest_score = scores[score]
    print(f"The highest score is: {highest_score}.")


# high_score()


def add_evens():
    evens_total = 0
    for even_number in range(2, 101, 2):
        evens_total = evens_total + even_number
    print(evens_total)


# add_evens()


def fizzbuzz():
    for counter in range(1, 101):
        if not counter % 3 and not counter % 5:
            print("FIZZBUZZ")
        elif not counter % 3:
            print("FIZZ")
        elif not counter % 5:
            print("BUZZ")
        else:
            print(counter)


# fizzbuzz()


"""
Day 5 Project: Password Generator

Asks how many characters do you want in the password.
Asks how many symbols to include.
Asks how many numbers to include.
Prints random password with those characteristics.

(c)2021 John Mann <gitlab.fox-io@foxdata.io>
"""


def generate_password():
    print("Password Generator")
    num_chars = int(input("How many letters in your password?"))
    num_sym = int(input("How many symbols in your password?"))
    num_num = int(input("How many numbers in your password?"))
    characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                  "U", "V", "W", "X", "Y", "Z"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    password = ""
    total_characters = num_chars + num_sym + num_num
    for position in range(0, total_characters):
        position_filled = False
        while not position_filled:
            position_type = random.randint(1, 3)
            # If this position type is a letter, make sure we still need letters, then add it to the password.
            if position_type == 1:
                if num_chars > 0:
                    # Use random upper/lowercase
                    character_case = random.randint(1, 2)
                    if character_case == 1:
                        password = password + characters[random.randint(0, len(characters) - 1)].lower()
                    else:
                        password = password + characters[random.randint(0, len(characters) - 1)]
                    num_chars = num_chars - 1
                    position_filled = True
            elif position_type == 2:
                if num_sym > 0:
                    password = password + symbols[random.randint(0, len(symbols) - 1)]
                    num_sym = num_sym - 1
                    position_filled = True
            elif position_type == 3:
                if num_num > 0:
                    password = password + numbers[random.randint(0, len(numbers) - 1)]
                    num_num = num_num - 1
                    position_filled = True
    print(password)


generate_password()
