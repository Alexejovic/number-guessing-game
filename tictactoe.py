# warum reicht nicht "import random", wenn randint doch dessen bestandteil ist?
from random import randint

# im nachhinein rausgestellt, das import random doch ausreicht, WVS spinnt
# muss hier, statt vor "if" gesetzt werden weil sonst keine abfrage durch user mehr und ewiger loop bei falscher eingabe
options = ["x", "y", "z"]


def play_SSP():
    computer = options[randint(0, 2)]
    decision = input("Make a decision - x, y or z?!: ")
    if (
        decision == "x" or decision == "y" or decision == "z"
    ):  # davor nur einmal decision geschrieben, überhaupt möglich?
        print("Your decision was: " + decision)
        print("Now let's compare with your opponent, the computer")
        print("The computers decision was " + computer)
        if decision == computer:
            print("Tie! :/ Try again!")
        elif decision == "x" and computer == "y":
            print("x hits y, you win! :)")
        elif decision == "x" and computer == "z":
            print("z hits x, oh no you loose :(")
        elif decision == "y" and computer == "z":
            print("y hits z, you win! :)")
        elif decision == "y" and computer == "x":
            print("x hits y, oh no you loose :(")
        elif decision == "z" and computer == "x":
            print("z hits x, you win! :)")
        elif decision == "z" and computer == "y":
            print("y hits z, oh no you loose :(")
    else:
        print("You had one job... :D Please try again!")
        play_SSP()


play_SSP()


def play_SSP_loop():
    decision_2 = input("Do you want to play again? y/n?: ")
    if decision_2 == "y":
        print("ok, let's go for another round")
        play_SSP()
        play_SSP_loop()
    elif decision_2 == "n":
        print("Ok, thank you for playing and good bye!")
    else:
        print("You had one job... :D Please try again!")
        play_SSP()


play_SSP_loop()