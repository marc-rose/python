"""
Random idea I found from a programming website:

We again use the random function here. You make a move first and then the program makes one.
To indicate the move, you can either use a single alphabet or input an entire string.
A function will have to be set up to check the validity of the move.
Using another function, the winner of that round is decided.
You can then either give an option of playing again or decide a pre-determined number of moves in advance.
A scorekeeping function will also have to be created which will return the winner at the end.

"""
import random

RPS_CHOICES = ("Rock", "Paper", "Scissors")


def checkInput(check_me):
    """
    Function to validate input. First letter of entry must be r, p, or s
    """
    if check_me[0].lower() == 'r' or \
       check_me[0].lower() == 'p' or \
       check_me[0].lower() == 's':
        return  # valid input
    elif len(check_me) == 0:  # empty variable causes issue in game()
        raise IndexError("checkInput(): Please enter at least one character")
    else:  # any other character is invalid
        raise ValueError("checkInput(): Invalid entry")


def game():
    """
    Function to represent game.
    """
    play_game = "Y"  # game ready to run
    user_rps = None  # create variable before logic and reference
    while play_game and play_game[0].lower() == "y":  # game() loops until play_game not starting with "y"
        user_str = input("Choose (R)ock, (P)aper, or (S)cissors: ")  # can reference RPS_CHOICES directly instead
        try:
            checkInput(user_str)  # validate input
        except (IndexError, ValueError):  # when checkInput raises either error, print same message
            print("Invalid input! Please start your response with either R, P, or S")
            continue  # go to start of while loop
        for item in range(len(RPS_CHOICES)):  # iterates RPS list
            if user_str[0].lower() == RPS_CHOICES[item][0].lower():
                user_rps = item  # match if first letter is first of a choice: (r, p, s)
        comp_rps = random.randrange(3)  # randomly generate computer choice
        if user_rps == comp_rps:
            print("Tie!")
            print("You both chose: " + RPS_CHOICES[user_rps])
        elif (user_rps == 0 and comp_rps == 2) or \
             (user_rps == 1 and comp_rps == 0) or \
             (user_rps == 2 and comp_rps == 1):
            print("You win!")
            print(f"Opponent chose: {RPS_CHOICES[comp_rps]}\nYou chose: {RPS_CHOICES[user_rps]}")
        else:
            print("You lose!")
            print(f"Opponent chose: {RPS_CHOICES[comp_rps]}\nYou chose: {RPS_CHOICES[user_rps]}")
        play_game = input("\nPlay again? (Y)es: ")  # game() leaves while loop if "y" is not entered


if __name__ == "__main__":
    game()
