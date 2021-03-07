import random

options = list(range(100))


def play_NGG():
    computer = random.choice(options)
    # print(computer)
    decision_1 = input("Please guess a number between 0 and 100: ")
    if int(decision_1) <= int(100) and int(decision_1) >= int(0):
        print("Your choice was " + decision_1)
        print(
            "Your "
            + str(decision_1)
            + " is "
            + str(int(computer) - int(decision_1))
            + " from the computer's choice away."
        )
        if (
            int(decision_1) - int(computer) <= 20
            and int(decision_1) - int(computer) >= -20
        ):
            print("Oh snap, that was close...")
            play_NGG()
    elif ():
        print("You had one job :D... Try again")
        play_NGG()


play_NGG()


def play_NGG_again():
    decision_2 = input("Do you want to try it again? y or n? ")
    if (
        decision_2 != "y"
        and decision_2 != "Y"
        and decision_2 != "n"
        and decision_2 != "N"
    ):
        print("Sorry, I didn't get you, please try again...")
        play_NGG_again()
    elif decision_2 == "y" or "Y":
        print("Alright, let's give it another try")
        play_NGG()
    elif decision_2 == "n" or "N":
        print("Scared Potter...? K, bye!")


play_NGG_again()