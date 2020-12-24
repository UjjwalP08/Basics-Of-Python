lis = ("Elon", "Musk", "Jeff", "Bezzoz", "Bill", "Gates"
    , "Steve", "jobs")
"""
suppose we want to print the element of list and after each element "and"
is nedded so we can print using for loop
"""

# for item in lis:
#     print(item, "and ", end="")
#
# print("Those all are Billionaires ")

# We can also print this type statement using "Join function"

a = " and ".join(lis)

print(a)

print("Those all are Billionaires")

b = ",".join(lis)

print(b)
# this is use of join function
