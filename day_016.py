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


class Dispenser:
    resources = {}

    def __init__(self, water, milk, coffee):
        self.resources["water"] = water
        self.resources["milk"] = milk
        self.resources["coffee"] = coffee

    def make_coffee(self, menu, menu_item):
        self.resources["water"] = self.resources["water"] - menu.get_menu_item(menu_item).ingredients["water"]
        if not menu_item == "espresso":
            self.resources["milk"] = self.resources["milk"] - menu.get_menu_item(menu_item).ingredients["milk"]
        self.resources["coffee"] = self.resources["coffee"] - menu.get_menu_item(menu_item).ingredients["coffee"]
        print(f"Here is your {menu_item}.")

    def has_resources(self, menu, menu_item):
        can_make = True
        water_needed = menu.get_menu_item(menu_item).ingredients["water"] or 0
        milk_needed = menu.get_menu_item(menu_item).ingredients["milk"] or 0
        coffee_needed = menu.get_menu_item(menu_item).ingredients["coffee"] or 0

        if self.resources["water"] < water_needed:
            can_make = False
        if self.resources["milk"] < milk_needed:
            can_make = False
        if self.resources["coffee"] < coffee_needed:
            can_make = False

        if not can_make:
            print(f"There is not enough resources to make {menu_item}")

        return can_make


class CoinOperation:
    def __init__(self):
        self.money = 0

    def accept_money(self, menu, menu_item):
        inserted_money = 0
        item_price = menu.get_menu_item(menu_item).cost
        print(f"The price is {self.format_currency(item_price)}")
        num_quarters = int(input("How many quarters to insert? "))
        num_dimes = int(input("How many dimes to insert? "))
        num_nickels = int(input("How many nickels to insert? "))
        num_pennies = int(input("How many pennies to insert? "))
        inserted_money = inserted_money + (num_quarters * 25)
        inserted_money = inserted_money + (num_dimes * 10)
        inserted_money = inserted_money + (num_nickels * 5)
        inserted_money = inserted_money + num_pennies
        if item_price > inserted_money:
            print("You did not insert enough money. You will be refunded.")
            return False
        elif item_price < inserted_money:
            print(f"Dispensing {self.format_currency(inserted_money - item_price)} in change.")
            self.money += item_price
            return True
        else:
            print("Exact change accepted.")
            self.money += item_price
            return True

    @staticmethod
    def format_currency(money):
        """Converts an integer representing cents to a formatted string representing dollars.

        Returns
        _______
        string : Formatted currency string ie: $1.00"""
        money = str(money)
        cents = money[-2:]
        dollars = money[0:-2]
        return f"${dollars}.{cents}"


class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
        }
        self.cost = cost

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class Menu:
    def __init__(self):
        self.menu = {
            MenuItem("latte", 200, 150, 24, 250),
            MenuItem("cappuccino", 250, 100, 24, 300),
            MenuItem("espresso", 50, 0, 18, 150),
        }

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def get_menu_item(self, query):
        for item in self.menu:
            if item.name == query:
                return item
        return None

    def show(self):
        """Ask user for the menu_item they would like to order.

        There are two 'secret' functions allowed: 'off' and 'report'.  We only return a value if the user enters a valid
        menu item or function. If user does not enter valid input, give a warning and ask for input again.

        Returns
        _______
        menu_item : string
            Contains the menu item to make or the special function requested.
        """
        menu_list = ""
        for item in self.menu:
            if menu_list == "":
                menu_list = item.name
            else:
                menu_list += f"|{item.name}"
        while True:
            menu_item = input(f"What would you like? ({menu_list}): ")
            for item in self.menu:
                if menu_item == item.name:
                    return menu_item

            if menu_item == "off" or menu_item == "report":
                return menu_item
            else:
                print("Invalid option. Try again.")


class CoffeeMachine:
    def __init__(self):
        self.dispenser = Dispenser(300, 200, 100)
        self.coin_op = CoinOperation()
        self.menu = Menu()

    def generate_report(self):
        print(f"""
        Water: {self.dispenser.resources["water"]}
        Milk: {self.dispenser.resources["milk"]}
        Coffee: {self.dispenser.resources["coffee"]}
        Profits: {self.coin_op.format_currency(self.coin_op.money)}
        """)

    @staticmethod
    def power_off():
        """Prints a message to inform user that machine is powering down."""
        print("Powering down...")

    def show_menu(self):
        return self.menu.show()

    def can_make(self, menu_item):
        return self.dispenser.has_resources(self.menu, menu_item)

    def has_paid(self, menu_item):
        return self.coin_op.accept_money(self.menu, menu_item)

    def make(self, menu_item):
        self.dispenser.make_coffee(self.menu, menu_item)


def main():
    coffee_machine = CoffeeMachine()
    # Outer loop so we can break from the inner loop and return to main menu.
    while True:
        # Inner loop
        while True:
            menu_item = coffee_machine.show_menu()
            if menu_item == "off":
                coffee_machine.power_off()
                return
            elif menu_item == "report":
                coffee_machine.generate_report()
            else:
                if not coffee_machine.can_make(menu_item):
                    print("Error. Not enough resources to make drink.")
                    break
                else:
                    if coffee_machine.has_paid(menu_item):
                        coffee_machine.make(menu_item)
                    else:
                        break


if __name__ == "__main__":
    main()
