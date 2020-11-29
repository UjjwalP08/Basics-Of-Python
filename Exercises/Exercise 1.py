"""In This exercise we can take input from user and compiler return according to its out put
Eg:- Key now we can provide some details about it."""
a = {"key": "Use to open lock", "greet": "Means to Call about Good mornig", "IT": "Study of Website and Computer"}
""
print(a.keys())

print("Enter Key which details you want to show")
b=input()
print(a[b])