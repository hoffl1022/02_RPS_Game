def check_rounds():
    while True:
        response = input("how many rounds?: ")

        round_error = "please press <enter> or type an integer more than zero"

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

# main routine goes here

rounds_played = 0
choose_instruction = "Please choose rock(r), paper(p), or scissors(s)"

# ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":
    print()
    if rounds == "":
        heading = f"Continuous mode: Round {rounds_played + 1}"
