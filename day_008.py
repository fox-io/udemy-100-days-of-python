"""
-----
Day 8 Project: Caesar Cipher
-----

(c)2021 John Mann <gitlab.fox-io@foxdata.io>

-----
Required tasks:
-----
1. Ask if user wants to encode or decode.

2. Ask user for offset value.

3. Ask for message to [en/de]code.

4. Display processed message.
"""


class CaesarCipher:
    """
    ------------
    CaesarCipher
    ------------
    This class allows for encrypting and decrypting a string of text using the Caesar cipher.

    -----
    Usage
    -----
    cc = CaesarCipher()

    cc.mode = "encrypt"

    cc.offset = 5

    cc.input_message = "Hello world!"

    print(cc.cipher())

    ---------------
    Class Variables
    ---------------
    self.alphabet - String containing alphabet available to the cipher engine.

    self.output_message - String containing the processed cipher text.

    self.input_message - Set this value to the message to process.

    self.offset - Set this value to the offset to shift our characters by.

    self.mode - Set this to "encrypt" or "decrypt", depending on which direction you want.

    ---------------
    Class Functions
    ---------------
    self.cipher(self) - Uses the variables set to encrypt or decrypt self.input_message
    """
    # String containing available characters and ordering
    alphabet = "abcdefghijklmnopqrstuvwxyz '\".,!?@#$%^&*()+-_=0123456789<>/\\;:{}[]`~ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Will contain our
    output_message = ""
    input_message = ""
    offset = 0
    mode = "encrypt"

    def __init__(self):
        pass

    def cipher(self):
        # Clear any previous message output
        self.output_message = ""

        # If we are decrypting, our offset needs to be inverted
        if self.mode == "decrypt" and self.offset > 0:
            self.offset = self.offset * -1

        # Split message into individual characters.
        character_list = [character for character in self.input_message]

        # Loop through character list
        for current_character in range(0, len(character_list)):
            # Get current character position in our alphabet set
            current_position = self.alphabet.index(character_list[current_character])

            # Calculate new character position using offset value
            new_position = current_position + self.offset

            # If our new position is out of bounds of our alphabet,
            # we need to offset our offset by the alphabet length.
            if new_position < 0:
                new_position = new_position + len(self.alphabet)
            elif new_position > len(self.alphabet) - 1:
                new_position = new_position - len(self.alphabet)

            # Add the processed character to our output message
            self.output_message = self.output_message + self.alphabet[new_position]

        # Return the completed output message
        return self.output_message


def main():
    # Create instance of CaesarCipher
    cc = CaesarCipher()
    while True:
        # Present choice to user for mode or to quit the program
        menu_command = input("[encrypt] a message\n[decrypt] a message\n[quit]\n: ").lower()
        if menu_command == "encrypt" or menu_command == "decrypt":
            # Set cipher mode
            cc.mode = menu_command
            # Get text from user
            cc.input_message = input(f"Enter the message to {cc.mode}.\n: ")
            # Get offset from user
            cc.offset = int(input("Enter the cipher offset.\n: "))
            # Output the result of the cipher
            print(f"Your result is: {cc.cipher()}")
        elif menu_command == "quit":
            # Exit main()
            return
        else:
            # Invalid user input
            print("Please choose a function to continue.")


# Main program
if __name__ == "__main__":
    main()
