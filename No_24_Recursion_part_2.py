"""
write function which generate Fibonacci series using function
0 1 1 2 3 5 8 13.....
"""

def fibo1(n):
    """Using iterative approach"""
    a=0
    b=1
    c=0
    print("Using iteration")

    for i in range(0,n):
        print(a, end=" ")
        c=a+b
        a=b
        b=c



def fibo(n):
    """Using recursive approach"""
    if n<=1:
        return n
    # elif n == 2:
    #     return 1

    else:
        return fibo(n - 1) + fibo(n - 2)



num = int(input("Enter no :-"))

# print(fibo1(num))
fibo1(num)

if num<0:
    print("Enter positive no")
else:
    print("\nUsing Recursion")
    for i in range(num):
       print(fibo(i),end=" ")

