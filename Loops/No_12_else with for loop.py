"""
        Else statement with for loop

some times we are not using the break statement inside the loop
and we want to check the some condition if we use the else statement
we are able to check that condition
"""


ls = ["roti","Sabji","Chawal","Chicken"]

for items in ls:
    if items=="Bread":
        print(f"Your food item is {items}")
else:
    print("Your food is not available in the list")
    print()
for item in ls:
    print(f"Your food item is {item}")

else:
    print("Your loop working properly!!!")