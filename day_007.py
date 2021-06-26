"""
Day 5 Project: Hangman Game

(c)2021 John Mann <gitlab.fox-io@foxdata.io>
"""
import random

# TODO: Expand our word list.
word_list = ["aardvark", "baboon", "camel"]

available_letters = {"a": True, "b": True, "c": True, "d": True, "e": True, "f": True, "g": True, "h": True, "i": True,
                     "j": True, "k": True, "l": True, "m": True, "n": True, "o": True, "p": True, "q": True, "r": True,
                     "s": True, "t": True, "u": True, "v": True, "w": True, "x": True, "y": True, "z": True}

the_hangman = {
    # Dict containing body parts and flags to denote if they are visible or not.
    # We use this to draw the gallows in the function update_gallows
    "head": [False, "o"],
    "arm1": [False, "/"],
    "body": [False, "|"],
    "arm2": [False, "\\"],
    "leg1": [False, "/"],
    "leg2": [False, "\\"]
}


def update_gallows(man):
    # Assembles the gallows, adding in body parts of the hangman if they are flagged as visible.
    new_gallows = " ┌────┐\n"
    new_gallows = new_gallows + " │    "
    if man['head'][0]:
        new_gallows = new_gallows + f"{man['head'][1]}"
    new_gallows = new_gallows + "\n"
    new_gallows = new_gallows + " │   "
    if man['arm1'][0]:
        new_gallows = new_gallows + f"{man['arm1'][1]}"
    else:
        new_gallows = new_gallows + " "
    if man['body'][0]:
        new_gallows = new_gallows + f"{man['body'][1]}"
    else:
        new_gallows = new_gallows + " "
    if man['arm2'][0]:
        new_gallows = new_gallows + f"{man['arm2'][1]}"
    else:
        new_gallows = new_gallows + " "
    new_gallows = new_gallows + "\n"
    new_gallows = new_gallows + " │   "
    if man['leg1'][0]:
        new_gallows = new_gallows + f"{man['leg1'][1]}"
    else:
        new_gallows = new_gallows + " "
    new_gallows = new_gallows + " "
    if man['leg2'][0]:
        new_gallows = new_gallows + f"{man['leg2'][1]}"
    else:
        new_gallows = new_gallows + " "
    new_gallows = new_gallows + "\n │\n─┴─"
    return new_gallows


def mask_random_word():
    """
    mask_random_word()

    Formats and returns the random word with underscores instead of letters for letters which have not yet been guessed.
    """
    masked_word = ""
    # Loop through each letter of random_word
    for position in range(0, len(random_word)):
        # If the current letter is no longer available, the user has guessed it already.
        # For guessed letters, we display the letter, otherwise, we display an underscore.
        if available_letters[random_word[position]]:
            masked_word = masked_word + "_"
        else:
            masked_word = masked_word + random_word[position]
    # Return the masked word.
    return masked_word


def show_available_letters():
    letter_counter = 0
    # Generates a list of the alphabet, striking through any letters that have been used.
    available_letter_string = ""
    for letter in available_letters:
        letter_counter += 1
        if available_letters[letter]:
            available_letter_string = available_letter_string + letter + " "
        else:
            available_letter_string = available_letter_string + '\u0336'.join(letter) + '\u0336' + " "
        # Split the displayed alphabet in half.
        if letter_counter == 13:
            available_letter_string = available_letter_string + "\n"
    print(available_letter_string)


def is_game_over():
    # Check each body part to determine if we have any still left hidden.
    for body_part in the_hangman:
        # If even a single body part is set to False, the game is not over.
        if not the_hangman[body_part][0]:
            return False
    # If all body parts are set to True, then game is over.
    return True


def is_word_guessed():
    for position in range(0, len(random_word)):
        if available_letters[random_word[position]]:
            return False
    return True


# Main Game Loop
# Game Setup
# ----------
# Choose a random word from word_list
random_word = word_list[random.randint(0, len(word_list) - 1)]
while True:
    # Display Game Board
    # ------------------
    # Show game board
    print(update_gallows(the_hangman))
    # Display the available letters
    show_available_letters()
    # Show masked random word
    print(mask_random_word())

    if is_word_guessed():
        print("You win!")
        break
    if is_game_over():
        print("The hangman is hung!")
        break

    # Process User Input
    # ------------------
    while True:
        # Ask user for a letter and check if it is in the random word
        user_choice = input("Guess a letter that you think might be in the word.\n: ").lower()
        # Check that we have not already guessed that letter
        if available_letters[user_choice]:
            # Mark letter as having been used.
            available_letters[user_choice] = False
            # Check to see if the letter is in our word.
            if user_choice in random_word:
                print("Your letter was found in the word!")
            else:
                print("That letter was not in the word.")
                # Add hangman part due to incorrect guess
                while True:
                    for part in the_hangman:
                        if not the_hangman[part][0]:
                            the_hangman[part][0] = True
                            break
                    break
            # Exit input loop
            break
        else:
            print("You have already guessed that letter. Try again!")
