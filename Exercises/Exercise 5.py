"""
Snake,Water and Gun game
"""

import random


def game():
    """This is Program of snake water and gun game"""  # doc string
    comp = 0
    me = 0
    k = 1
    print("\n\t\tWelcome into Snake,Water And Gun Game!!!!!\n")

    while k <= 10:
        print("Enter Your choice\n")
        i = input("s for Snake\nw for water\ng for Gun\n")

        list1 = ["s", "w", "g"]
        j = random.choice(list1)
        print("Computer choose", j)
        print()

        if i == "s" and j == "w":
            print("\t\tYou Win\n")
            me += 1
            k += 1
            # print(k)
        elif i == "w" and j == "s":
            print("\t\tComputer Win\n")
            comp += 1
            k += 1
            # print(k)

        elif i == "w" and j == "g":
            print("\t\tYou win\n")
            me += 1
            k += 1
            # print(k)

        elif i == "g" and j == "w":
            print("\t\tComputer Win\n")
            comp += 1
            k += 1
            # print(k)

        elif i == "g" and j == "s":
            print("\t\tYou win\n")
            me += 1
            k += 1
            # print(k)

        elif i == "s" and j == "g":
            print("\t\tComputer Win\n")
            comp += 1
            k += 1
            # print(k)

        elif i == j:
            print("\t\tIt's Draw\n")
            k += 1
            me += 1
            comp += 1
            # print(k)

        else:
            print("\t\tEnter right choice!!!!!!\n")
            print("\t\tTry Again!!!!!")
            game()

    print("Your Score is", me)
    print("Computer Score is", comp)

    if me > comp:
        print()
        print("\t\tCongratulation!!!!!!")
        print("\t\tYou are Winner\n")
    elif me == comp:
        print()
        print("\t\tIt's Draw\n")
    else:
        print()
        print("\t\tComputer is Winner\n")


game()
