"""
-----
Day 15 Project: Coffee Machine
-----
Coffee Machine Program Requirements

1.Prompt user by asking "What would you like? (espresso/latte/cappuccino): "
    a.Check the user’s input to decide what to do next.
    b.The prompt should show every time action has completed, e.g. once the drink is dispensed.
      The prompt should show again to serve the next customer.
2.Turn off the Coffee Machine by entering "off" to the prompt.
    a.For maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine.
      Your code should end execution when this happens.
3.Print report.
    a.When the user enters “report” to the prompt, a report should be generated that shows the current resource values.
      e.g. Water: 100ml Milk: 50ml Coffee: 76g Money: $2.5
4.Check resources sufficient?
    a.When the user chooses a drink, the program should check if there are enough resources to make that drink.
    b.E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make
      the drink but print: "Sorry there is not enough water."
    c.The same should happen if another resource is depleted, e.g. milk or coffee.
5.Process coins.
    a.If there are sufficient resources to make the drink selected, then the program should prompt the user to insert
      coins.
    b.Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    c.Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2pennies =
      0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
6.Check transaction successful?
    a.Check that the user has inserted enough money to purchase the drink they selected.
      E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the program should say
      "Sorry that's not enough money. Money refunded.".
    b.But if the user has inserted enough money, then the cost of the drink gets added to the machine as the profit
      and this will be reflected the next time “report” is triggered. E.g.Water: 100mlMilk: 50mlCoffee: 76gMoney: $2.5
    c.If the user has inserted too much money, the machine should offer change. E.g. “Here is $2.45 dollars in change.”
      The change should be rounded to 2 decimal places.
7.Make Coffee.
    a.If the transaction is successful and there are enough resources to make the drink the user selected, then the
      ingredients to make the drink should be deducted from the coffee machine resources.E.g. report before
      purchasing latte: Water: 300ml Milk: 200ml Coffee: 100g Money: $0 Report after purchasing latte: Water: 100ml
      Milk: 50ml Coffee: 76g Money: $2.5
    b.Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If latte was their choice
      of drink.

(c)2021 John Mann <gitlab.fox-io@foxdata.io>
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

profits = 0.0


def show_coffee_menu():
    menu_item = input("What would you like? (espresso/latte/cappuccino): ")
    if menu_item == "off" or menu_item == "report" or COFFEE_MENU[menu_item]:
        return menu_item
    else:
        return False


def power_off():
    print("Powering down...")


def generate_report():
    print(f"""
    Water: {resources["water"]}
    Milk: {resources["milk"]}
    Coffee: {resources["coffee"]}
    Profits: {profits}
    """)


def make_coffee(menu_item):
    resources["water"] = resources["water"] - COFFEE_MENU[menu_item]["ingredients"]["water"]
    if not menu_item == "espresso":
        resources["milk"] = resources["milk"] - COFFEE_MENU[menu_item]["ingredients"]["milk"]
    resources["coffee"] = resources["coffee"] - COFFEE_MENU[menu_item]["ingredients"]["coffee"]
    print(f"Here is your {menu_item}.")


def has_resources(menu_item):
    can_make = True
    milk_needed = 0
    water_needed = COFFEE_MENU[menu_item]["ingredients"]["water"]
    if not menu_item == "espresso":
        milk_needed = COFFEE_MENU[menu_item]["ingredients"]["milk"]
    coffee_needed = COFFEE_MENU[menu_item]["ingredients"]["coffee"]

    if resources["water"] < water_needed:
        can_make = False
    if resources["milk"] < milk_needed:
        can_make = False
    if resources["coffee"] < coffee_needed:
        can_make = False

    if can_make:
        return menu_item
    else:
        print(f"There is not enough resources to make {menu_item}")
        return can_make


def accept_money(menu_item):
    global profits
    inserted_money = 0
    print(f"The price is ${COFFEE_MENU[menu_item]['cost']}")
    num_quarters = int(input("How many quarters to insert? "))
    num_dimes = int(input("How many dimes to insert? "))
    num_nickels = int(input("How many nickels to insert? "))
    num_pennies = int(input("How many pennies to insert? "))
    inserted_money = inserted_money + (num_quarters * 0.25)
    inserted_money = inserted_money + (num_dimes * 0.10)
    inserted_money = inserted_money + (num_nickels * 0.05)
    inserted_money = inserted_money + (num_pennies * 0.01)
    item_price = COFFEE_MENU[menu_item]["cost"]
    if item_price > inserted_money:
        print("You did not insert enough money. You will be refunded.")
        return False
    elif item_price < inserted_money:
        profits = profits + COFFEE_MENU[menu_item]["cost"]
        print(f"Dispensing ${inserted_money - item_price:.2f} in change.")
        return True
    else:
        profits = profits + COFFEE_MENU[menu_item]["cost"]
        print("Exact change accepted.")
        return True


def main():
    while True:
        while True:
            menu_item = show_coffee_menu()
            if not menu_item:
                print("Invalid option. Try again.")
            elif menu_item == "off":
                power_off()
                return
            elif menu_item == "report":
                generate_report()
            else:
                can_make = has_resources(menu_item)
                if not can_make:
                    print("Error. Not enough resources to make drink.")
                    break
                else:
                    transaction_successful = accept_money(menu_item)
                    if transaction_successful:
                        make_coffee(menu_item)
                    else:
                        break


if __name__ == "__main__":
    main()
