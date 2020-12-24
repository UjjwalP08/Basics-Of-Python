"""
some times we want to import file or modules in python using "import" keyword

"""
import sys

print(sys.path)  # Show the path of System module
#


# from sklearn.ensemble import RandomForestClassifier
# print(RandomForestClassifier())




import file1

print(file1.a)
file1.printjoke("This is me")

import file2
print(file2.a)

