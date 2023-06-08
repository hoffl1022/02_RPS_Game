import random


# Ask user if they have played the game before.
# If 'no' show instructions
def instructions():
    print("********How to play********")
    print()
    print("choose how many rounds you want to play, or press <enter> for infinite rounds")
    print()
    print("you will be asked to choose Rock, Paper, Scissors")
    print("or you can type 'xxx' to end the game manually")
    print("(You can also just type the first letter of the word instead of typing the whole word)")
    print()
    print("the rules are:")
    print("- Rock beats scissors")
    print("- Scissors beats paper")
    print("- Paper beats rock")
    print()
    print("=====Good Luck=====")
    print()
    return ""


# Ask users for rounds( checks if response is valid )
def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> or an that is more than 0"

        # If infinite mode not choose, check response is an integer that is more than 0
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


# Check users response is valid
def choice_checker(question, valid_list, error):
    while True:
        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item in the list (or the first letter of an item),
        # the full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item not in list
        print(error)
        print()


# List of valid responses

rps_list = ["rock", "paper", "scissors", "xxx"]
yes_no_list = ["yes", "no"]

game_history = []

# Main routine goes here
# Introduction question
played_before = choice_checker("Have you played the game before? ", yes_no_list, "Please enter yes / no")

if played_before == "no":
    instructions()

print()

rounds_played = 0
rounds_lost = 0
rounds_drawn = 0

# Ask user for # of rounds then loop
# Asl user for the # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Start of Game Play Loop

    # Rounds heading
    print()
    if rounds == "":
        heading = f"Continuous mode: [Round {rounds_played + 1}]"
    else:
        heading = f"[Round {rounds_played + 1} of {rounds}]"

    print(heading)

    # Tell the user what their options are
    choose_instruction = "Choose either rock (r), paper(p), scissors(s) or 'xxx' to exit: "

    # Print error message if user choice is not valid
    choose_error = "Please choose from Rock, Paper, Scissors (or xxx to end game)"

    # Ask user for choice and check if it's valid
    user_choice = choice_checker(choose_instruction, rps_list, choose_error)

    print()
    print(f"You chose: {user_choice}")

    # End game if exit code is typed
    if user_choice == "xxx":
        print("Thank you for playing")
        break

    # get computer choice
    comp_choice = random.choice(rps_list[:-1])
    print("Comp Choice: ", comp_choice)

    # Compare computer and user choices
    if comp_choice == user_choice:
        result = "tied"
        rounds_drawn += 1
    elif user_choice == "rock" and comp_choice == "scissors":
        result = "won"
    elif user_choice == "paper" and comp_choice == "rock":
        result = "won"
    elif user_choice == "scissors" and comp_choice == "paper":
        result = "won"
    else:
        result = "lost"
        rounds_lost += 1

    feedback = f"{user_choice} vs {comp_choice} - You {result}"
    print(feedback)

    # add feedback to list and include round number
    outcome = f"Round {rounds_played + 1}: {feedback}"
    game_history.append(outcome)

    # rest of loop / game

    rounds_played += 1

    # end game if requested # of rounds has been played
    if rounds_played == rounds:
        break


# Quick Calculations (stats)
rounds_won = rounds_played - rounds_lost - rounds_drawn

# displays game stats with % values with no decimals

if rounds_played > 1:
    # Calculate Game Stats
    percent_win = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100
    percent_tie = rounds_drawn / rounds_played * 100

    # ask the user if they want to see their game history
    print()
    history_display = choice_checker("do you want to see your game history? ", yes_no_list, "please choose yes / no")
    if history_display == "yes":
        print()
        for item in game_history:
            print(item)

    # End of Game Statements
    print()
    print("******** END GAME SUMMARY ********")
    print(f"Won: {rounds_won} \t|\t Lost: {rounds_lost} \t|\t Draw: {rounds_drawn}")
    print()
    print(f"Win: {rounds_won}, ({percent_win:.0f}%)\nLoss: {rounds_lost}, ({ percent_lost:.0f}%)\nDraw: {rounds_drawn}, ({percent_tie:.0f}%)")
    print()
    print("Thanks for playing")

else:
    print("🐔🐔🐔 You chickened out. Squawk Squawk. 🐔🐔🐔")
