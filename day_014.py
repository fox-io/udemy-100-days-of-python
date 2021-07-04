"""
-----
Day 14 Project: Higher or Lower
-----
Using a list of personalities and their follower counts,
Offer two random entries and ask user to choose the one
that has more followers. If they get it right, then use
the second person as the first person and compare to a
new random person. If they get it wrong, then game over.
Present a count of how many they got right and ask if
they would like to play again.

(c)2021 John Mann <gitlab.fox-io@foxdata.io>
"""
from random import randint

PRESS_ENTER = "Press enter to continue..."
MENU = "[1] Play\n[0] Quit\n: "
INVALID_INPUT = "Please choose a menu option to continue."
PLAY_GAME = 1
QUIT_GAME = 0


class HigherLowerGame:
    # Reference consts
    UNUSED_PERSONALITIES = 0
    USED_PERSONALITIES = 1
    SCORE = 2
    PERSONALITY_A = 3
    PERSONALITY_B = 4
    USER_GUESS = 5
    IS_WINNER = 6
    PROMPT_WHICH_IS_HIGHER = "Which of these two personalities have more followers? (A or B)\n: "
    LOGO = """
    ╦ ╦┬┌─┐┬ ┬┌─┐┬─┐
    ╠═╣││ ┬├─┤├┤ ├┬┘
    ╩ ╩┴└─┘┴ ┴└─┘┴└─
        ┌─┐┬─┐      
        │ │├┬┘      
        └─┘┴└─      
    ╦  ┌─┐┬ ┬┌─┐┬─┐ 
    ║  │ ││││├┤ ├┬┘ 
    ╩═╝└─┘└┴┘└─┘┴└─ 
    """

    data = [
        # UNUSED_PERSONALITIES
        [
            {
                'name': 'Instagram',
                'follower_count': 346,
                'description': 'Social media platform',
                'country': 'United States'
            },
            {
                'name': 'Cristiano Ronaldo',
                'follower_count': 215,
                'description': 'Footballer',
                'country': 'Portugal'
            },
            {
                'name': 'Ariana Grande',
                'follower_count': 183,
                'description': 'Musician and actress',
                'country': 'United States'
            },
            {
                'name': 'Dwayne Johnson',
                'follower_count': 181,
                'description': 'Actor and professional wrestler',
                'country': 'United States'
            },
            {
                'name': 'Selena Gomez',
                'follower_count': 174,
                'description': 'Musician and actress',
                'country': 'United States'
            },
            {
                'name': 'Kylie Jenner',
                'follower_count': 172,
                'description': 'Reality TV personality and businesswoman and Self-Made Billionaire',
                'country': 'United States'
            },
            {
                'name': 'Kim Kardashian',
                'follower_count': 167,
                'description': 'Reality TV personality and businesswoman',
                'country': 'United States'
            },
            {
                'name': 'Lionel Messi',
                'follower_count': 149,
                'description': 'Footballer',
                'country': 'Argentina'
            },
            {
                'name': 'Beyoncé',
                'follower_count': 145,
                'description': 'Musician',
                'country': 'United States'
            },
            {
                'name': 'Neymar',
                'follower_count': 138,
                'description': 'Footballer',
                'country': 'Brazil'
            },
            {
                'name': 'National Geographic',
                'follower_count': 135,
                'description': 'Magazine',
                'country': 'United States'
            },
            {
                'name': 'Justin Bieber',
                'follower_count': 133,
                'description': 'Musician',
                'country': 'Canada'
            },
            {
                'name': 'Taylor Swift',
                'follower_count': 131,
                'description': 'Musician',
                'country': 'United States'
            },
            {
                'name': 'Kendall Jenner',
                'follower_count': 127,
                'description': 'Reality TV personality and Model',
                'country': 'United States'
            },
            {
                'name': 'Jennifer Lopez',
                'follower_count': 119,
                'description': 'Musician and actress',
                'country': 'United States'
            },
            {
                'name': 'Nicki Minaj',
                'follower_count': 113,
                'description': 'Musician',
                'country': 'Trinidad and Tobago'
            },
            {
                'name': 'Nike',
                'follower_count': 109,
                'description': 'Sportswear multinational',
                'country': 'United States'
            },
            {
                'name': 'Khloé Kardashian',
                'follower_count': 108,
                'description': 'Reality TV personality and businesswoman',
                'country': 'United States'
            },
            {
                'name': 'Miley Cyrus',
                'follower_count': 107,
                'description': 'Musician and actress',
                'country': 'United States'
            },
            {
                'name': 'Katy Perry',
                'follower_count': 94,
                'description': 'Musician',
                'country': 'United States'
            },
            {
                'name': 'Kourtney Kardashian',
                'follower_count': 90,
                'description': 'Reality TV personality',
                'country': 'United States'
            },
            {
                'name': 'Kevin Hart',
                'follower_count': 89,
                'description': 'Comedian and actor',
                'country': 'United States'
            },
            {
                'name': 'Ellen DeGeneres',
                'follower_count': 87,
                'description': 'Comedian',
                'country': 'United States'
            },
            {
                'name': 'Real Madrid CF',
                'follower_count': 86,
                'description': 'Football club',
                'country': 'Spain'
            },
            {
                'name': 'FC Barcelona',
                'follower_count': 85,
                'description': 'Football club',
                'country': 'Spain'
            },
            {
                'name': 'Rihanna',
                'follower_count': 81,
                'description': 'Musician and businesswoman',
                'country': 'Barbados'
            },
            {
                'name': 'Demi Lovato',
                'follower_count': 80,
                'description': 'Musician and actress',
                'country': 'United States'
            },
            {
                'name': "Victoria's Secret",
                'follower_count': 69,
                'description': 'Lingerie brand',
                'country': 'United States'
            },
            {
                'name': 'Zendaya',
                'follower_count': 68,
                'description': 'Actress and musician',
                'country': 'United States'
            },
            {
                'name': 'Shakira',
                'follower_count': 66,
                'description': 'Musician',
                'country': 'Colombia'
            },
            {
                'name': 'Drake',
                'follower_count': 65,
                'description': 'Musician',
                'country': 'Canada'
            },
            {
                'name': 'Chris Brown',
                'follower_count': 64,
                'description': 'Musician',
                'country': 'United States'
            },
            {
                'name': 'LeBron James',
                'follower_count': 63,
                'description': 'Basketball player',
                'country': 'United States'
            },
            {
                'name': 'Vin Diesel',
                'follower_count': 62,
                'description': 'Actor',
                'country': 'United States'
            },
            {
                'name': 'Cardi B',
                'follower_count': 67,
                'description': 'Musician',
                'country': 'United States'
            },
            {
                'name': 'David Beckham',
                'follower_count': 82,
                'description': 'Footballer',
                'country': 'United Kingdom'
            },
            {
                'name': 'Billie Eilish',
                'follower_count': 61,
                'description': 'Musician',
                'country': 'United States'
            },
            {
                'name': 'Justin Timberlake',
                'follower_count': 59,
                'description': 'Musician and actor',
                'country': 'United States'
            },
            {
                'name': 'UEFA Champions League',
                'follower_count': 58,
                'description': 'Club football competition',
                'country': 'Europe'
            },
            {
                'name': 'NASA',
                'follower_count': 56,
                'description': 'Space agency',
                'country': 'United States'
            },
            {
                'name': 'Emma Watson',
                'follower_count': 56,
                'description': 'Actress',
                'country': 'United Kingdom'
            },
            {
                'name': 'Shawn Mendes',
                'follower_count': 57,
                'description': 'Musician',
                'country': 'Canada'
            },
            {
                'name': 'Virat Kohli',
                'follower_count': 55,
                'description': 'Cricketer',
                'country': 'India'
            },
            {
                'name': 'Gigi Hadid',
                'follower_count': 54,
                'description': 'Model',
                'country': 'United States'
            },
            {
                'name': 'Priyanka Chopra Jonas',
                'follower_count': 53,
                'description': 'Actress and musician',
                'country': 'India'
            },
            {
                'name': '9GAG',
                'follower_count': 52,
                'description': 'Social media platform',
                'country': 'China'
            },
            {
                'name': 'Ronaldinho',
                'follower_count': 51,
                'description': 'Footballer',
                'country': 'Brazil'
            },
            {
                'name': 'Maluma',
                'follower_count': 50,
                'description': 'Musician',
                'country': 'Colombia'
            },
            {
                'name': 'Camila Cabello',
                'follower_count': 49,
                'description': 'Musician',
                'country': 'Cuba'
            },
            {
                'name': 'NBA',
                'follower_count': 47,
                'description': 'Club Basketball Competition',
                'country': 'United States'
            }
        ],
        # USED_PERSONALITIES
        [],
        # SCORE
        0,
        # PERSONALITY_A
        [],
        # PERSONALITY_B
        [],
    ]
    current_score = 0

    def __init__(self):
        """
        -----
        Day 14 Project: Higher or Lower
        -----
        Using a list of personalities and their follower counts,
        Offer two random entries and ask user to choose the one
        that has more followers. If they get it right, then use
        the second person as the first person and compare to a
        new random person. If they get it wrong, then game over.
        Present a count of how many they got right and ask if
        they would like to play again.

        (c)2021 John Mann <gitlab.fox-io@foxdata.io>
        """
        pass

    @staticmethod
    def move_personality(list_a, list_b, list_index):
        """Moves list_a[list_index] to list_b

        Parameters
        ----------
        list_index : int
            Index of the source list element you want to move.
        list_a : list
            Source list
        list_b : list
            Destination List
        """
        list_b.append(list_a.pop(list_index))

    def new_game(self):
        """Resets any dynamic variables to their original values.

        Sets the current player's score to 0. Moves all used personalities back to the unused list. Moves any currently
        being used personalities back to the unused list.
        """
        # Clear current score
        self.data[self.SCORE] = 0

        # Move all personalities from used to unused.
        while len(self.data[self.USED_PERSONALITIES]) > 0:
            self.move_personality(self.data[self.USED_PERSONALITIES], self.data[self.UNUSED_PERSONALITIES], 0)

        # Move any current personalities to unused.
        while len(self.data[self.PERSONALITY_A]) > 0:
            self.move_personality(self.data[self.PERSONALITY_A], self.data[self.UNUSED_PERSONALITIES], 0)
        while len(self.data[self.PERSONALITY_B]) > 0:
            self.move_personality(self.data[self.PERSONALITY_B], self.data[self.UNUSED_PERSONALITIES], 0)

    def pick_random_personality(self):
        """Assigns random personalities from the unused list to lists A and B.

        Randomly chooses a personality in the unused personality list to list A, then does the same for list B. In the
        event that we are already playing a game and there is personalities contained in list A, we move it to our used
        personality list. We then move list B's personality to list A, and finally assign a random personality to list
        B.
        """
        if self.data[self.PERSONALITY_A]:
            # If we already have a set of personalities in play,
            # We need to move A to used and B to A, then get a new B
            self.move_personality(self.data[self.PERSONALITY_A], self.data[self.USED_PERSONALITIES], 0)
            self.move_personality(self.data[self.PERSONALITY_B], self.data[self.PERSONALITY_A], 0)
            random_index = randint(0, len(self.data[self.UNUSED_PERSONALITIES]) - 1)
            self.move_personality(self.data[self.UNUSED_PERSONALITIES], self.data[self.PERSONALITY_B], random_index)
        else:
            # If we do not have any personalities in play yet, just select 2 random ones for A and B.
            random_index = randint(0, len(self.data[self.UNUSED_PERSONALITIES]) - 1)
            self.move_personality(self.data[self.UNUSED_PERSONALITIES], self.data[self.PERSONALITY_A], random_index)
            random_index = randint(0, len(self.data[self.UNUSED_PERSONALITIES]) - 1)
            self.move_personality(self.data[self.UNUSED_PERSONALITIES], self.data[self.PERSONALITY_B], random_index)

    def show_gameboard(self):
        name_a = self.data[self.PERSONALITY_A][0]['name']
        description_a = self.data[self.PERSONALITY_A][0]['description']
        location_a = self.data[self.PERSONALITY_A][0]['country']
        # followers_a = self.data[self.PERSONALITY_A][0]['follower_count']

        name_b = self.data[self.PERSONALITY_B][0]['name']
        description_b = self.data[self.PERSONALITY_B][0]['description']
        location_b = self.data[self.PERSONALITY_B][0]['country']
        # followers_b = self.data[self.PERSONALITY_B][0]['follower_count']

        print(f"(A) {name_a} ({description_a} from {location_a})")
        print("└─────╢vs╟─────┐")
        print(f"(B) {name_b} ({description_b} from {location_b})")

    def get_user_guess(self):
        self.data[self.USER_GUESS] = input(self.PROMPT_WHICH_IS_HIGHER).lower()

    def check_for_winner(self):
        self.data[self.IS_WINNER] = False
        if self.data[self.USER_GUESS] == "a":
            if self.data[self.PERSONALITY_A][0]['follower_count'] > self.data[self.PERSONALITY_B][0]['follower_count']:
                self.data[self.IS_WINNER] = True
            else:
                self.data[self.IS_WINNER] = False
        else:
            if self.data[self.PERSONALITY_B][0]['follower_count'] > self.data[self.PERSONALITY_A][0]['follower_count']:
                self.data[self.IS_WINNER] = True
            else:
                self.data[self.IS_WINNER] = False

    def show_game_end(self):
        name_a = self.data[self.PERSONALITY_A][0]['name']
        name_b = self.data[self.PERSONALITY_B][0]['name']
        followers_a = self.data[self.PERSONALITY_A][0]['follower_count']
        followers_b = self.data[self.PERSONALITY_B][0]['follower_count']
        print("Wrong answer!")
        print(f"{name_a} had {followers_a}M followers and {name_b} had {followers_b}M followers!")
        print(f"Your score was: {self.data[self.SCORE]}")

    def show_game_win(self):
        name_a = self.data[self.PERSONALITY_A][0]['name']
        name_b = self.data[self.PERSONALITY_B][0]['name']
        followers_a = self.data[self.PERSONALITY_A][0]['follower_count']
        followers_b = self.data[self.PERSONALITY_B][0]['follower_count']
        print("Correct!")
        print(f"{name_a} had {followers_a}M followers and {name_b} had {followers_b}M followers!")
        self.data[self.SCORE] += 1
        print(f"Your score is now: {self.data[self.SCORE]}")
        self.pick_random_personality()


def main():
    hilo = HigherLowerGame()
    print(hilo.LOGO)
    while True:
        menu_command = int(input(MENU))
        if menu_command == PLAY_GAME:
            hilo.new_game()
            hilo.pick_random_personality()
            while True:
                hilo.show_gameboard()
                hilo.get_user_guess()
                hilo.check_for_winner()
                if not hilo.data[hilo.IS_WINNER]:
                    hilo.show_game_end()
                    break
                else:
                    hilo.show_game_win()
                input(PRESS_ENTER)
        elif menu_command == QUIT_GAME:
            return
        else:
            print(INVALID_INPUT)


if __name__ == "__main__":
    main()
