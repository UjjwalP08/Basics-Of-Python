"""Find gratest number in four numbers and input take from user"""

a=int(input("Enter 1st no:-"))
b=int(input("Enter 2nd no:-"))
c=int(input("Enter 3rd no:-"))
d=int(input("Enter 4th no:-"))

if(a>=b and a>=c and a>=d):
    print("a is gratest number")
elif(b>=a and b>=c and b>=d):
    print("b is gratest number")
elif(c>=a and c>=b and c>=d):
    print("c is gratest number")
else:
    print("d is greates number")

