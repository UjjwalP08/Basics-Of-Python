# n1=input("Enter n1:-")
# n2=input("Enter n2:-")
#
# print("The sum is", int(n1)+int(n2))
# if out n1 and n2 is take input as string so
# above print stament cause of error
# print("The IMP part of program is begain now")

n1 = input("Enter n1:-")
n2 = input("Enter n2:-")

try:  # using try except print the error as msg if it will generate we print it so user can get it is an error
    print("The sum is", int(n1) + int(n2))

except Exception as e:
    print(e)

print("The IMP part of program is begain now")
