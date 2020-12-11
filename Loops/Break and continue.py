i=1

while(i<=50):
    if i==45:
        i=i+1
        continue# skip when i=45
    if i==49:
        break# break when i=49 and exit in the loop
    print(i,end=" ")
    i=i+1

"""In python while(1)=while(True)  is same so both are work as same"""



while(True):

    i = int(input("Enter a number:-\n"))
    if i>100:
        print("You found number which is grater than 100\n")
        break

    else:
        print("Try Again!!!\n")
        continue


