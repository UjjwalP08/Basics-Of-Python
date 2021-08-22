# -----------Map Function -----------

lis = ["45", "43", "98", "455"]

# Here our list is in sting data type and we want to increase the value of its elements\
# So first convert in integer
# After using it we can perform arithmetic process
# for i in range(len(lis)):
#
#     lis[i]=int(lis[i])
#
# lis[3]=lis[3]+5
#
# print(lis)

# Using Map function we can do same thins as above in only one line

# map syntax:-map(function, iterable)

# lis=["45" , "43" , "98", "455"]
#
#
lis = list(map(int, lis))

lis[1] = lis[1] ** 0.5
print(lis)
lis1 = [1, 2, 3, 4, 5]

c = list(map(lambda x: x ** 2, lis1))

print(c)

# def sq(x):
#     return x*x
#
# lis=list(map(sq,lis))
# print(lis)

# we can do same thing using lambda function

# lis=list(map(lambda x: x*x, lis))
#
# print(lis)


# fun = [lambda x:x*x,lambda y:y*y*y]
#
# for items in range(5):
#     val=list(map(lambda j:j(items),fun))
#     print(val)


# ----------------filter function-------------

#   Syntax:-filter(function,iterable)

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def is_greater_5(num):
    return num > 5


gr_than_5 = list(filter(is_greater_5, list_1))
print(gr_than_5)

ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def less(n):
    return n < 7


les = list(filter(less, ls))
print(les)

# -------------reduce function-------------

#   Syntax:-reduce(function,iterable)


# suppose we have list and we want to receive sum of all of his elements

l = [1, 2, 3, 4, 5]

n = 0
for item in l:
    n = n + item

print(n)
# but this process is so lengthy using reduce function we can do this so easily

# reduce function is inside the functool so first we want to import functool than we can use it


from functools import reduce

ans = (reduce(lambda x, y: x + y, l))

print("The sum is", ans)
