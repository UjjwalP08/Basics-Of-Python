""" 
        ---------> Program of printing star pattern <--------- 
 """

n=input("Enter the value of n:-")
n=int(n)
# for value in range(n,0,-1):
#     for itm in range(1,value+1):
#         print("*",end=" ")
#     print()
#

# for values in range(1,n+1):
    # print(values)

for i in range(1,n+1):
    for j in range(1,i+1):
        print(" * ",end=" ")
    print()

for i in range(n,0,-1):
    for j in range(1,i+1):
        print(" * ",end=" ")
    print()

for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(" * ",end=" ")
    print()
for i in range(n,0,-1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(" * ",end=" ")
    print()


