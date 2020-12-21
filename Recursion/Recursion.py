def fact(n):
    """This is Recursive method to find factorial of given no """
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

"""
Recursion:-It means a function call itself is known as....
"""

def fact1(n):
    """This is Iterative method to find factorial of given no"""
    fac=1
    for i in range(n):
       fac=fac * (i+1)
    return fac

num = int(input("Enter the no which you want to find factorial:-"))

print(fact.__doc__)
print("The factorial of  no is ", num, "Its answer is", fact(num))
print(fact1.__doc__)
print("The factorial of  no is ", num, "Its answer is", fact1(num))
