
import os

"""_summary_
         importing rock_paper_scissors_helper as helper
"""


import rock_paper_scissors_helper as helper


options = ("s", "p", "r")

computer = None


def game_user1(game_mode, point):

    player1 = ""
    player2 = ""
    computer = ""
    point = 0
    running = True

    if game_mode == "1":

        while running:

            if point == 3:
                print("Game End !!!!!!!!!!3")
                print("Total points ", point)
                helper.play_again("do you wanto play again")
                main()

            helper.discription()

            player1 = input("input s, p, r      >>> ")

            if player1 == "!":
                exit()

            computer = helper.random(options)
            print("Total points ", point)
            player1 = helper.cheak_valid_input(player1)

            if player1 == computer:

                print("Player 1 Input    >>> ", player1)
                print("Computer Input    >>> ", computer)
                print("your and computer input matched")
                print("Total points ", point)
                continue
            elif player1 == "r" and computer == "s":
                print("Player 1 Input    >>> ", player1)
                print("Computer Input    >>> ", computer)
                print("You win!")
                point += 1
                print("Total points ", point)
                continue

            elif player1 == "p" and computer == "r":
                print("Player 1 Input    >>> ", player1)
                print("computer Input >> > ", computer)
                print("player1 win")
                point += 1
                print("Total points ", point)
                continue

            elif player1 == "s" and computer == "p":
                print("Player 1 Input    >>> ", player1)
                print("computer Input    >>> ", computer)
                print("player1 win")
                point += 1
                print("Total points ", point)
                continue

            else:

                print("Player 1 Input    >>> ", player1)
                print("computer Input    >>> ", computer)
                print("you lose!")
                print("Total points ", point)
                continue

    elif game_mode == "2":

        while running:

            if point == 3:
                print("Game End !!!!!!!!!!3")
                print("Total points ", point)
                helper.play_again("do you wanto play again")
                main()

            helper.discription()
            player1 = input("input s, p, r      >>> ")
            if player1 == "!":
                exit()
            computer = helper.random(options)
            print("Total points ", point)
            player1 = helper.cheak_valid_input(player1)

            helper.discription()
            player1 = input("input s, p, r      >>> ")
            player2 = input("input s, p, r      >>> ")
            player1 = helper.cheak_valid_input(player1)
            player2 = helper.cheak_valid_input(player2)

            if player1 == "!" or player2 == "!":
                exit()

            print("Total points ", point)

            if player1 == player2:

                print("Player 1 Input    >>> ", player1)
                print("Player 2 Input    >>> ", player2)
                print("your and Player 2 input matched")
                #point += 1
                print("Total points ", point)
                continue
            elif player1 == "r" and player2 == "s":
                print("Player 1 Input    >>> ", player1)
                print("Player 2 Input    >>> ", player2)
                print("player1 win")
                point += 1
                print("Total points ", point)
                continue

            elif player1 == "s" and player2 == "r":
                print("Player 1 Input    >>> ", player1)
                print("Player 2 Input    >>> ", player2)
                print("player2 win")
                point += 1
                print("Total points ", point)
                continue

            elif player1 == "p" and player2 == "r":
                print("Player 1 Input    >>> ", player1)
                print("Player 2 Input    >>> ", player2)
                print("player1 win")
                point += 1
                print("Total points ", point)
                continue

            elif player1 == "r" and player2 == "p":
                print("Player 1 Input    >>> ", player1)
                print("Player 2 Input    >>> ", player2)
                print("player2 win")
                point += 1
                print("Total points ", point)
                continue

            elif player1 == "s" and player2 == "p":
                print("Player 1 Input    >>> ", player1)
                print("Player 2 Input    >>> ", player2)
                print("player1 win")
                point += 1
                print("Total points ", point)
                continue

            elif player1 == "p" and player2 == "s":
                print("Player 1 Input    >>> ", player1)
                print("Player 2 Input    >>> ", player2)
                print("player2 win")
                point += 1
                print("Total points ", point)
                continue

            else:

                print("Player 1 Input    >>> ", player1)
                print("Player 2 Input    >>> ", player2)
                print("you lose!")
                print("Total points ", point)
                break

        print("Total points    >> ", point)
        return point


def main():

    # Clearing the Screen
    os.system('cls')

    print("[       Wellcome to Rock Paper Scissors Game          ]")

    while True:
        point = 0
        print("Enter game mode 1 for User1 vs computer")
        print("Enter game mode 2 for User1 vs User2")

        game_mode = input()
        if game_mode == "!":
            exit()

        game_palyers = helper.players(game_mode)

        if game_palyers == "1":
            print("User 1 and Computer")
            game_user1(game_palyers, point)
        elif game_palyers == "2":
            print("User 1 and user 2")
            game_user1(game_palyers, point)
        else:
            continue


#last call main
if __name__ == "__main__":
    main()
