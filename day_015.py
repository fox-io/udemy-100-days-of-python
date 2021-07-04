"""
-----
Day 15 Project: Coffee Maker
-----

(c)2021 John Mann <gitlab.fox-io@foxdata.io>
"""
PRESS_ENTER = "Press enter to continue..."
MENU = "[1] Play\n[0] Quit\n: "
INVALID_INPUT = "Please choose a menu option to continue."
PLAY_GAME = 1
QUIT_GAME = 0
LOGO = """
Coffee Maker
"""
COFFEE_MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def main():
    print(LOGO)
    while True:
        menu_command = int(input(MENU))
        if menu_command == PLAY_GAME:
            pass
        elif menu_command == QUIT_GAME:
            return
        else:
            print(INVALID_INPUT)


if __name__ == "__main__":
    main()
