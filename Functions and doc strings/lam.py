"""
lambda function
"""# Lambda functions or anonymous functions
# def add(a, b):
#     return a+b
#
# # minus = lambda x, y: x-y
#
# def minus(x, y):
#     return x-y
#
# print(minus(9, 4))


a =[[6, 14], [5, 6], [8,23]]
a.sort(key=lambda x:x[0]) #here 0 and 1 is index value
print(a)

