"""
Write program to create function which take input for the user
In function create files which take input from user and when required give its output to user
create 3 persons which name is Harry,Rohan,and Hammad
enter input as data form them diet and workout details with time and save this data in the file
we require total 6 files
3 for diet
3 for workout
"""


def getdate():
    """Genrate Data and time using this function"""
    import datetime
    return datetime.datetime.now()


def Health_Management_System():
    """This is Health Management System Progaram"""
    c = 1
    while c != 0:
        print("\nWelcome to Health Management  System!!!!\n")
        print("Enter Person No. which you want to show his diet and workout")
        name = int(input("1 for Harry \n2 for Rohan \n3 for Hammad \n"))

        if name == 1:
            print("\t\tYou choose Harry\n")
            print("In Harry Enter what you want to show")
            h = int(input("1 for Harry Diet \n2 for Harry's Workout\n"))
            if h == 1:
                print("\t\tThis Harry's Diet")
                print("What do you want to do in Harry diet")
                h = int(
                    input("1 for show Data of Harry Diet\n2 for enter data in Harry's Data\n"))
                if h == 1:
                    with open("hd.txt") as hd:
                        print("Harry Food and its timing \n")
                        print(hd.read())

                else:
                    c = 1
                    print("Enter Harry Diet")

                    with open("hd.txt", "a") as hd:
                        while c != 0:
                            ha = input("Enter what Harry want eat:-")
                            hd.write(str(getdate())+" "+ha+"\n")
                            # hd.write(" ")
                            # hd.write(ha)
                            # hd.write("\n")
                            c = int(
                                input("For continue press 1 and for exit press 0:-"))

            elif h == 2:
                print("\t\tThis Harry's Workout")
                print("What do you want to do in Harry's Workout")
                h = int(
                    input("1 for show Data of Harry Workout\n2 for enter data in Harry's Workout\n"))
                if h == 1:
                    with open("hw.txt") as hd:
                        print("Harry Exercise and its timing \n")
                        print(hd.read())

                else:
                    c = 1
                    print("Enter harry Workout")
                    with open("hw.txt", "a") as hd:
                        while c != 0:
                            ha = input(
                                "Enter which exercise harry want to do:-")
                            hd.write(str(getdate())+" "+ha+"\n")
                            # hd.write(" ")
                            # hd.write(ha)
                            # hd.write("\n")
                            c = int(
                                input("For continue press 1 and for exit press 0:-"))

            else:
                print("Enter correct choice!!!!!")
                print("Try again!!!!!")

        elif name == 2:
            print("\t\tYou choose Rohan\n")
            print("In Rohan Enter what you want to show ")
            r = int(input("1 for Rohan Diet \n2 for Rohan's Workout\n"))

            if r == 1:
                print("\t\tThis is Rohan Diet\n")
                print("What do you want to do in Rohan diet")
                h = int(
                    input("1 for show Data of Rohan Diet\n2 for enter data in Rohan's Data\n"))
                if h == 1:
                    with open("rd.txt") as hd:
                        print("Rohan Food and its timing \n")
                        print(hd.read())

                else:
                    c = 1
                    print("Enter Rohan Diet")

                    with open("rd.txt", "a") as hd:
                        while c != 0:
                            ha = input("Enter what Rohan want eat:-")
                            hd.write(str(getdate())+" "+ha+"\n")
                            # hd.write(" ")
                            # hd.write(ha)
                            # hd.write("\n")
                            c = int(
                                input("For continue press 1 and for exit press 0:-"))
            elif r == 2:
                print("\t\tThis is Rohan's Workout\n")
                print("What do you want to do in Rohan's Workout")
                h = int(
                    input("1 for show Data of Rohan Workout\n2 for enter data in Rohan's Workout\n"))
                if h == 1:
                    with open("rw.txt") as hd:
                        print("Rohan Exercise and its timing \n")
                        print(hd.read())

                else:
                    c = 1
                    print("Enter Rohan Workout")
                    with open("rw.txt", "a") as hd:
                        while c != 0:
                            ha = input(
                                "Enter which exercise Rohan want to do:-")
                            hd.write(str(getdate())+" "+ha+"\n")
                            # hd.write(" ")
                            # hd.write(ha)
                            # hd.write("\n")
                            c = int(
                                input("For continue press 1 and for exit press 0:-"))

            else:
                print("Enter correct choice!!!!!")
                print("Try again!!!!!")

        elif name == 3:
            print("\t\tYou choose Hammad\n")
            print("In Hammad Enter what you want to show ")
            ha = int(input("1 for Hammad Diet \n2 for Hammad's Workout\n"))
            if ha == 1:
                print("\t\tThis is Hammad Diet\n")
                print("What do you want to do in Hammad diet")
                h = int(
                    input("1 for show Data of Hammad Diet\n2 for enter data in Hammad's Data\n"))
                if h == 1:
                    with open("had.txt") as hd:
                        print("Hammad Food and its timing \n")
                        print(hd.read())

                else:
                    c = 1
                    print("Enter Hammad Diet")

                    with open("had.txt", "a") as hd:
                        while c != 0:
                            ha = input("Enter what Hammad want eat:-")
                            hd.write(str(getdate())+" "+ha+"\n")
                            # hd.write(" ")
                            # hd.write(ha)
                            # hd.write("\n")
                            c = int(
                                input("For continue press 1 and for exit press 0:-"))

            elif ha == 2:
                print("\t\tThis is Hammad's Workout\n")
                print("What do you want to do in Hammad's Workout")
                h = int(input(
                    "1 for show Data of Hammad Workout\n2 for enter data in Hammad's Workout\n"))
                if h == 1:
                    with open("haw.txt") as hd:
                        print("Hammad Exercise and its timing \n")
                        print(hd.read())

                else:
                    c = 1
                    print("Enter Hammad Workout")
                    with open("haw.txt", "a") as hd:
                        while c != 0:
                            ha = input(
                                "Enter which exercise Hammad want to do:-")
                            hd.write(str(getdate())+" "+ha+"\n")
                            # hd.write(" ")
                            # hd.write(ha)
                            # hd.write("\n")
                            c = int(
                                input("For continue press 1 and for exit press 0:-"))

            else:
                print("Enter correct choice!!!!!")
                print("Try again!!!!!")

        else:
            print("Enter correct choice!!!!\n")
            print("Try again!!!!\n\n\n")

        c = int(input("\n\t\t1 for continue and 0 for exit:-"))


print(Health_Management_System.__doc__)
Health_Management_System()
print("\t \tThanks to visit our Health Management System!!!!!! ")
