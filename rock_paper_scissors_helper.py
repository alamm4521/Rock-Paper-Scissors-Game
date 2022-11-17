import random
import sys

_rand = random.Random()
options = ("s", "p", "r")


def cheak_valid_input(input_letter):

    if input_letter not in options:
        print("Invalid input")

    return input_letter


def msg(text):

    return text


def discription():

    print("input from the user")
    print("s for Scissors")
    print("p for Paper")
    print("r for Rock")

    return


def random(arr):

    return _rand.choice(arr)


#Player control

def players(user):

    while True:
        if user == "1":

            return user

        elif user == "2":

            return user

        else:
            print("invalid input")
            exit()


def play_again(msg):

    print(msg)
    print("Enter 'Y' or 'y' for YES, 'N' or 'n' for NO:")
    counter = 0
    while True:
        choice = input()

        if choice and choice[0] in 'yY':
            return True
        elif choice and choice[0] in 'nN':
            exit()  # test
            #return False
        else:
            print("Input Is not valid")
            break
