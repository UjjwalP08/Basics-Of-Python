"""
Guess the no and you have 9 chance
if your all chances are overs your game is over

"""
n=23
i=9
print("You have total 9 chances")

while(i>=0):
    if i!=0:
        u=int(input("Enter number:-"))
        if u==n:
            print("Congretulation!!! You guess the Number \n")
            print("your remaing chances \n", i-1)
            break
        elif u<n:
            print("Your no is smaller \n")
            print("your remaing chances \n", i-1)
            # i=i-1
            i-=1
            #continue
        elif u>n:
            print("Your no is larger \n ")
            print("your remaing chances \n", i-1)
            # i=i-1
            i-=1
            #continue
    else:
        print("")
        print("Your game is Over You have no more chance")
        break

