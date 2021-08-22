def getdate():
    import datetime
    return datetime.datetime.now()


f = open("new.txt", "a")

# a = f.write("Entre what you want to enter")  # this statement add text in fie
c=1
while c!=0:
    a=input( "Enter what you wnat to enter 1:-")
    f.write(str(getdate()))
    f.write(" ")

    f.write(a)
    f.write("\n")
    c=int(input("For 1 to continue or for 0 to exit"))
# print(a)  # Show the total no of character we write in line
f.close()
