"""
-----
Day 11 Project: Blackjack
-----

(c)2021 John Mann <gitlab.fox-io@foxdata.io>
"""
import random

# Reference variables for our card_deck
FULL = 0
DRAW = 1
DISCARD = 2
PLAYER = 3
DEALER = 4
# ♠♥♦♣


class Blackjack:
    deck = [
        {"A♠", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠",
         "A♥", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥",
         "A♦", "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦", "K♦",
         "A♣", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣"},
        [],
        [],
        [],
        [],
    ]

    def __init__(self):
        self.reset_deck()

    def reset_deck(self):
        self.deck[DRAW] = list(self.deck[FULL])
        self.deck[DISCARD] = []
        self.deck[PLAYER] = []
        self.deck[DEALER] = []

    def draw_card(self, hand):
        card_index = random.randint(0, len(self.deck[DRAW]) - 1)
        if hand == "player":
            self.deck[PLAYER].append(self.deck[DRAW].pop(card_index))
        elif hand == "dealer":
            self.deck[DEALER].append(self.deck[DRAW].pop(card_index))

    def visible_hand(self, hand):
        visible = ""
        for card_position in range(0, len(self.deck[PLAYER]) if hand == "player" else len(self.deck[DEALER])):
            if hand == "dealer" and card_position > 0:
                visible = visible + "[?] "
            elif hand == "dealer" and card_position == 0:
                visible = visible + self.deck[DEALER][card_position] + " "
            elif hand == "player":
                visible = visible + self.deck[PLAYER][card_position] + " "
        return visible

    def hand_total(self, hand):
        num_aces = 0
        total = 0

        for card_position in range(0, len(self.deck[PLAYER]) if hand == "player" else len(self.deck[DEALER])):

            # Make reference to current card
            if hand == "dealer":
                current_card = self.deck[DEALER][card_position]
            else:
                current_card = self.deck[PLAYER][card_position]

            # Determine value of current card
            if current_card[0] == "A":
                # We use 11 for aces, but save a counter in case we need to convert them to 1 based on hand total
                card_value = 11
                num_aces += 1
            elif current_card[0] == "J" or current_card[0] == "Q" or current_card[0] == "K":
                card_value = 10
            else:
                card_value = int(current_card[:-1])
            total += card_value

        if total > 21 and num_aces > 0:
            # Reduce total if we have aces and are over 21.
            while total > 21 and num_aces > 0:
                total -= 10
                num_aces -= 1

        return total

    def print_hands(self):
        print(f"Player Hand: {self.visible_hand('player')}")
        print(f"Dealer Hand: {self.visible_hand('dealer')}")


def main():
    # Loop until player chooses to quit.
    while True:

        # Present choice to user for mode or to quit the program.
        print("Blackjack\n---------")
        menu_command = int(input("[1] Play\n[0] Quit\n: "))

        # If user selects play, start main game loop.
        if menu_command == 1:

            # Create Blackjack object
            bj = Blackjack()

            # Set flags for player and dealer turns.
            player_done = False
            dealer_done = False

            # Draw 2 cards each
            for drawing in range(0, 2):
                bj.draw_card("player")
                bj.draw_card("dealer")

            # Inner game loop.
            while not player_done and not dealer_done:

                # Player goes first.
                while not player_done:
                    bj.print_hands()

                    # If we hit 21 or busted, exit player and dealer turns to process game end.
                    if bj.hand_total("player") >= 21:
                        player_done = True
                        dealer_done = True
                    else:
                        # Offer play menu to player.
                        game_command = int(input("[1] Draw Card\n[2] Stay\n: "))

                        if game_command == 1:
                            bj.draw_card("player")
                        elif game_command == 2:
                            player_done = True

                    # Exit player turn if they are done
                    if player_done:
                        break

                # Handle dealer turn
                while not dealer_done:
                    bj.print_hands()

                    # If we hit 21 or busted, exit dealer turn to process game end.
                    if bj.hand_total("dealer") >= 21:
                        dealer_done = True
                    # Dealer must draw if total is under 17
                    elif bj.hand_total("dealer") < 17:
                        bj.draw_card("dealer")
                    # Dealer stays otherwise
                    else:
                        dealer_done = True

                    # Exit dealer turn when they are done
                    if dealer_done:
                        break

            # Handle the scoring
            if bj.hand_total("player") == 21:
                print("Blackjack! You Win!")
            elif bj.hand_total("player") > 21:
                print("You Busted!")
            elif bj.hand_total("dealer") == 21:
                print("Blackjack! Dealer Wins!")
            elif bj.hand_total("dealer") > 21:
                print("Dealer Busted!")
            else:
                if bj.hand_total("player") > bj.hand_total("dealer"):
                    print("Higher Score. You Win!")
                elif bj.hand_total("dealer") > bj.hand_total("player"):
                    print("Lower Score. Dealer Wins!")
                else:
                    print("Push! No one wins!")

        # If user selects quit, quit program.
        elif menu_command == 0:
            return

        # Invalid input handler
        else:
            print("Please choose a menu option to continue.")


# Main program
if __name__ == "__main__":
    main()
