def day_009_1():
    """
    Day 9 - Practice 1
    Convert a table of scores to the descriptive grades below:
    91 - 100: Grade = "Outstanding"
    81 - 90: Grade = "Exceeds Expectations"
    71 - 80: Grade = "Acceptable"
    70 or lower: Grade = "Fail"
    """
    student_scores = {
        "Harry": 81,
        "Ron": 78,
        "Hermione": 99,
        "Draco": 74,
        "Neville": 62,
    }

    student_grades = {}

    for student in student_scores:
        if student_scores[student] <= 70:
            student_grades[student] = "Fail"
        elif student_scores[student] <= 80:
            student_grades[student] = "Acceptable"
        elif student_scores[student] <= 90:
            student_grades[student] = "Exceeds Expectations"
        else:
            student_grades[student] = "Outstanding"

    print(student_grades)


def day_009_2():
    """
    Instructions

    You are going to write a program that adds to a travel_log.
    You can see a travel_log which is a List that contains 2
    Dictionaries.
    Write a function that will work with the following line of
    code on line 21 to add the entry for Russia to the
    travel_log.
        > add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

        > You've visited Russia 2 times.
        > You've been to Moscow and Saint Petersburg.
    """
    travel_log = [
        {
            "country": "France",
            "visits": 12,
            "cities": ["Paris", "Lille", "Dijon"]
        },
        {
            "country": "Germany",
            "visits": 5,
            "cities": ["Berlin", "Hamburg", "Stuttgart"]
        },
    ]

    def add_new_country(country, visits, cities):
        # Add new information to the travel log
        travel_log.append({"country": country, "visits": visits, "cities": cities})

        # Print the new information in readable syntax.
        print(f"You've visited {country} {visits} times.")

        # Assemble readable output for the list using commas, 'and', and a period.
        output_string = ""
        num_cities = len(cities)
        for city in cities:
            if num_cities == len(cities):
                # If this is our first city, just add it to the output string.
                output_string = city
            elif num_cities > 1:
                # If this is not the first city OR the last city, add it with a comma.
                output_string = output_string + f", {city}"
            else:
                # If this is our last city, use the word 'and' and end with a period.
                output_string = output_string + f" and {city}."
            num_cities = num_cities - 1
        # Print the cities added to the travel log
        print(f"You've been to {output_string}")

    add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
    print(travel_log)


def day_009_final():
    from os import system
    print("Blind Auction")
    # Enter your name
    # Enter your bid
    # Type yes or no
    # If yes, clear screen, then repeat
    # If no, clear screen and show winning bidder

    # Make an empty dict for storing bids.
    bid_list = {}
    # Set our loop flag to yes to add the first bidder
    add_another_bid = "yes"
    # Loop until our flag is changed to no
    while add_another_bid == "yes":
        # I had to set a flag inside PyCharm's run configuration for this file.
        # By default it does not run the terminal as a terminal. You have to set
        # it to emulate the terminal, and then the following works inside the IDE.
        system('cls')
        # Get input
        bidder_name = input("Enter your name: ")
        bidder_bid = int(input("Enter your bid as a whole number: $"))
        # Add to bid list
        bid_list[bidder_name] = bidder_bid

        add_another_bid = input("Add another bidder? [yes/no]: ").lower()

    highest_bid = 0
    highest_bidder = ""
    for bidder in bid_list:
        if bid_list[bidder] > highest_bid:
            highest_bid = bid_list[bidder]
            highest_bidder = bidder

    print(f"{highest_bidder} wins with a bid of ${highest_bid}")


# day_009_1()
# day_009_2()
day_009_final()
