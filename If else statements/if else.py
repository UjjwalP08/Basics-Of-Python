a=7
#b=int(input("Enter the value:-"))
b=9
if(b>a):
    print("b is greater than a")
elif(b==a):
    print("b is equal to a")
else:
    print("a is greater than b")

"""
Here we are use in as keyword to check the element is in the list or not in the list
"""
list=[1,3,5,6]

if(1 in list):
    print("1 is in list")

else:
    print("1 not in the list")

if(30 not in list):
    print("30 not in the list")
else:
    print("3 in the list")

    #Quick Prob
"""
Take input form  user and check the your age is able to driving
condition
1) UR  age is less than to 18 print not able drive
2) UR age is equal to 18 print we think about u
3) UR age is grater than to 18 print able to drive
 """

c=int(input("Enter your age:-"))

if(c<18):
    print("Not able to drive")
elif(c==18):
    print("We think about you")
else:
    print("You are able to drive")
