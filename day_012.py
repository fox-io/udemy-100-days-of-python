"""
-----
Day 11 Project: Number Guess
-----

(c)2021 John Mann <gitlab.fox-io@foxdata.io>
"""
import random

MSG_INVALID_INPUT = "Please choose a valid menu option."
MSG_ENTER_TO_CONTINUE = "Press enter to continue..."


class NumberGuess:
    # Class Consts
    MSG_LOGO = """
 _   _                 _                  _____                     
| \\ | |               | |                / ____|                    
|  \\| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___  ___ ___ 
| . ` | | | | '_ ` _ \\| '_ \\ / _ \\ '__| | | |_ | | | |/ _ \\/ __/ __|
| |\\  | |_| | | | | | | |_) |  __/ |    | |__| | |_| |  __/\\__ \\__ \\
|_| \\_|\\__,_|_| |_| |_|_.__/ \\___|_|     \\_____|\\__,_|\\___||___/___/
    """
    MSG_WINNER = "You guessed the correct answer!"
    MSG_TOO_LOW = "Your guess was too low. Try again."
    MSG_TOO_HIGH = "Your guess was too high. Try again."
    MSG_ENTER_GUESS = "What is your guess?\n: "
    MSG_MENU = "[1] Play Easy Mode\n[2] Play Hard Mode\n[0] Quit\n: "
    MSG_OUT_OF_GUESSES = "You ran out of guesses!"
    MENU_EASY = 1
    MENU_HARD = 2
    EASY = 10
    HARD = 5

    # Class variables
    lower_bound = 1
    higher_bound = 100
    chosen_number = 0
    guesses_remaining = 0
    is_winner = ""

    def __init__(self):
        # Show logo
        print(self.MSG_LOGO)

    def choose_random_number(self):
        self.is_winner = False
        self.chosen_number = random.randint(self.lower_bound, self.higher_bound)

    def set_difficulty(self, new_difficulty):
        self.guesses_remaining = new_difficulty

    def user_guess(self):
        print(f"The number is between {self.lower_bound} and {self.higher_bound}.")
        print(f"You have {self.guesses_remaining} guesses remaining.")
        the_guess = int(input(self.MSG_ENTER_GUESS))
        self.guesses_remaining -= 1
        if the_guess == self.chosen_number:
            self.is_winner = True
            return self.MSG_WINNER
        elif the_guess < self.chosen_number:
            return self.MSG_TOO_LOW
        elif the_guess > self.chosen_number:
            return self.MSG_TOO_HIGH


def wait_for_user():
    input(MSG_ENTER_TO_CONTINUE)


def main():
    game = NumberGuess()

    while True:
        # Present choice to user for mode or to quit the program
        menu_command = int(input(game.MSG_MENU))
        if menu_command == game.MENU_EASY or menu_command == game.MENU_HARD:
            # Set difficulty
            if menu_command == game.MENU_EASY:
                game.set_difficulty(game.EASY)
            else:
                game.set_difficulty(game.HARD)

            # Choose the random number
            game.choose_random_number()

            # Loop until guesses are exhausted
            while game.guesses_remaining > 0:
                # Get user guess.
                guess_result = game.user_guess()

                # Print result of guess.
                print(guess_result)

                # Exit guessing loop if user guessed correctly.
                if game.is_winner:
                    break

            # Both winners and out of guesses end up here,
            # so we check for which state we are in.
            if not game.is_winner:
                print(game.MSG_OUT_OF_GUESSES)
                print(f"The number was {game.chosen_number}")

            wait_for_user()
        elif menu_command == 0:
            # Exit program
            return
        else:
            # Handle invalid input
            print(MSG_INVALID_INPUT)


# Main program
if __name__ == "__main__":
    main()
