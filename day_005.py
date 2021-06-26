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


class Password:
    # Variables for password construction
    num_letters = 0     # Total letters to generate in the password.
    num_symbols = 0     # Total symbols to generate in the password.
    num_numbers = 0     # Total numbers to generate in the password.
    num_characters = 0  # Total characters in the password

    # Character sets
    allowed_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                       "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                       "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    allowed_symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
    allowed_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # Output placeholder
    generated_password = ""

    def get_password_layout(self):
        # Loop until we get at least one character to generate.
        while self.num_characters == 0:
            # Ask user for how many of each character type to include in the password.
            self.num_letters = int(input("How many letters would you like in your password?\n: "))
            self.num_symbols = int(input("How many symbols would you like in your password?\n: "))
            self.num_numbers = int(input("How many numbers would you like in your password?\n: "))
            # Save the total number of characters to a variable for use during generation.
            self.num_characters = self.num_letters + self.num_symbols + self.num_numbers
            # Give user an informative statement if they tried to allow for a zero-length password.
            if self.num_characters == 0:
                print("Try Again. Please enter at least one character for the password to be generated.")

    def get_random_character(self, character_list):
        return character_list[random.randint(0, len(character_list) - 1)]

    def generate_password(self):
        # Use our length to loop through the password generation.
        for character_position in range(0, self.num_characters):
            # Flag used for continuing to loop until we have chosen a character for the current character position.
            character_position_filled = False
            while not character_position_filled:
                # Randomly choose a character type for the current character position.
                # 1 = letter, 2 = symbol, 3 = number
                character_position_type = random.randint(1, 3)
                if character_position_type == 1:
                    # Only add letters if we still have letters to add.
                    if self.num_letters > 0:
                        # Randomly choose a letter from allowed letters
                        random_letter = self.get_random_character(self.allowed_letters)
                        # Add letter to password
                        self.generated_password = self.generated_password + random_letter
                        self.num_letters -= 1
                        character_position_filled = True
                elif character_position_type == 2:
                    # Add symbols if we still need symbols
                    if self.num_symbols > 0:
                        self.generated_password = self.generated_password + \
                                                  self.get_random_character(self.allowed_symbols)
                        self.num_symbols -= 1
                        character_position_filled = True
                elif character_position_type == 3:
                    # Add numbers if we still need numbers
                    if self.num_numbers > 0:
                        self.generated_password = self.generated_password +\
                                                  self.get_random_character(self.allowed_numbers)
                        self.num_numbers -= 1
                        character_position_filled = True


def generate_password():
    print("Password Generator\n------------------")
    my_password = Password()
    my_password.get_password_layout()
    my_password.generate_password()
    print(my_password.generated_password)


generate_password()
