# Types of operators in Python
# Arithmetic Operators
# Assignment Operators
# Comparison Operators
# Logical Operators
# Identity Operators
# Membership Operators
# Bitwise Operators


a = int(input("Enter any no:-"))
b = int(input("Enter any no:-"))

# Airthmatic Operators
# +,-,*,/,%,**,//
print("The sum is ", a + b)  # for +
print("The diffrence is ", a - b)  # for -
print("The multiplication is ", a * b)  # for *
print("The divison is ", a / b)  # for /
print("The answer of a power b is ", a ** b)  # for power
print("The reminder is ", a % b)  # for reminder
print("The answer is ", a // b)  # Return int no for divison answer not return decimal points

# Assignment Operators
# =,+=,-=,*=,/=,%=
a += a  # or a=a+a
print("the answer is ", a)
a *= a  # or a=a-a a+=1 means a=a+1
print("the answer is ", a)
a /= a  # or a=a*a
print("the answer is ", a)
a -= a  # or a=a/a
print("the answer is ", a)

# Comparison Operators
# ==,<=,<,>,>=,!=
print(a == b)  # check both no is equal
print(a < b)  # check less than
print(a > b)  # check grater than
print(a != b)  # not equal to

# logical operators
# or & and
# Work like boolean gates or boolean algebra
a = True
b = False
print(a and a)
print(a and b)
print(b and a)
print(b and b)

print(a or b)
print(b or b)
print(b or a)
print(a or a)

# Bitwise Operator
# &(Bitwise and) ,|(Bitwise or)
# decimal to binary in bit form
# 0 - 00
# 1 - 01
# 2 - 10
# 3 - 11

print(0 & 2)
# that answer come like 0 in binary 00
# and 2 in binary 10
# now  we can perfom binay bitwise
# like 0 & 1=0 and 0 & 0=0 so our answer is 00 and its reprsent 0 in decimal

print(0 | 3)
# 0 in binary 00
# 3 in binary 11
# 0|1=1 and 0|1=1 so our answer is 11 and its reprsent 3 in decimal

# Identity operators
# is , is not
c = 5
print(c is 5)
print(5 is not 0)

# Membership Operators
# in , not in
list = [3, 3, 2, 2, 39, 33, 35, 32]
print(32 not in list)
print(32 in list)
print(352 not in list)
print(3 in list)


