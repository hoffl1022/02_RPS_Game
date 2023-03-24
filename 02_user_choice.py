# functions go here
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


# list for checking responses
rps_list = ["rock", "paper", "scissors", "xxx"]

# loop for testing purposes
user_choice = ""
while user_choice != "xxx":
    # ask for user choice and check if it is valid
    user_choice = choice_checker("Choose Rock / Paper / Scissors (r/p/s):", rps_list, "Please choose from Rock / "
                                                                                      "Paper / Scissors (r/p/s)")

    # print user choice for comparison purposes
    print(f"You chose {user_choice}")
# ask user for choice and check if its valid


# print user choice for comparison purposes
