a=7
b=9
c=sum( (a,b))#In build function 
print("The sum of a and b is", c)


def avg(a,b):#User define function
    """This function use to find 2 number avrage"""#this is doc string
    avgr=(a+b)/2
    return avgr

# print(avg(a,b))
print("The avrages is",avg(a,b))
print(avg.__doc__)