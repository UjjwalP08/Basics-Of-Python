l = ["ujjwal", "harry", "good", "ritik", "Ayushman", "Hermin"]

i = 1

for item in l:
    if i % 2 != 0:
        print(f"{item} is great leader ")
    i += 1
print()
"""
enumerate function provide key as well as index
"""
for j, item in enumerate(l):  # here j value initially is 0
    if j % 2 == 0:
        print(f"{item} is great caption")
