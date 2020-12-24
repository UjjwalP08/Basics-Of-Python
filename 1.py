n=input("Enter the value of n")
n=int(n)
# for value in range(n,0,-1):
#     for itm in range(1,value+1):
#         print("*",end=" ")
#     print()
#

# for values in range(1,n+1):
    # print(values)

for value in range(0,n+1):
    for itm in range(1,value+1,1):
        print("*",end=" ")
    print()

