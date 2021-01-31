"""
------------------ Regular Expressions------------

Regular expressions are used to perform search-related tasks in Python

To work with regular expressions, we have to import a built-in module in python called ‘re’.

"""

import re

my_str = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiina'''

# findall, search, split, sub, finditer
# function of re modules

# obj = re.compile(r"fass") # r-string
#   raw-strings use to  also print escape sequence character
#   span =(448,452) means your world count in the string
# obj = re.compile(r".adm")
"""In .adm the (.)means any character and after any character that contain adm"""
# obj = re.compile(r"^Tata")
"""In ^ means our string is start with Tata world if it is true so print the value otherwise not"""
# obj = re.compile(r"ina$")
""" $ means our string is end with given world an if it is true so print the value otherwise not print it"""
# obj = re.compile(r"ai*")
"""*ai means in this string after character a it contain 0 or any no of i character"""
# obj = re.compile(r"a*i*")
"""and here a*i* means this obj 0 or any no of a and i character is contain string """
# obj = re.compile(r"ai+")
"""here ai+ means after character a it contain 1 or any no of i character in the string and if it is true so print it"""
# obj = re.compile(r"a+i+")
"""here a+i+ means 1 or any no of character a and i contain string and if it is true so print it"""
# obj = re.compile(r"ai{2}")
"""here ai{2} means after a character exact contain 2 i character and if it is write so print it"""
# obj = re.compile(r"a{2}i{2}")
"""String must contain exact  2 a and i character """

# obj = re.compile(r"(ai){2}")
"""It means  here using this () parentheses we are make group 
and here it return group of ai and if it is true so print otherwise not
here is group like  'aiai'  like that   """
# obj = re.compile(r"(ai){1}")
"""here contain ai in only group like 'ai'
"""
# obj = re.compile(r"ai{1}|t")
"""Here this code means we are get ai word or t character | this use to either or"""
# obj = re.compile(r"ai{1}|Fax")

#   Special Sequences

# obj = re.compile(r"\ATata")
"""\A use to return a match if given word is begaing of the string"""

# obj = re.compile(r"\bFax")
"""print the detail if given word is start with that word"""

# obj = re.compile(r"Fax\b")
"""print the detail if given word is end with that word"""

obj = re.compile(r"\d{5}-\d{4}")
"""\d is return digit and {} this type paranthesess use to get exact value
so this string return 5 digit no after - this sign and after again return 4 digit no
"""

match = obj.finditer(my_str)  # match object

for items in match:
    print(items)
