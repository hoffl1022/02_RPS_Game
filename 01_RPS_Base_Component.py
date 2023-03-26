import random

# functions go here


# checks a list of valid answers and compares it to the users input
def choice_checker(question, valid_list, error):
    while True:

        # ask user for choice
        response = input(question).lower()

        # checks through the list of valid items to see if the user choice is a valid item
        # if it is the full name of the item is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item is not in the list
        print(error)
        print()

# main routine goes here


# list of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]
