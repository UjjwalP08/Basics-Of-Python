"""
---------------------Json Module -------------------

json full form is JavaScript Object Notation
"""

import json

# in json the all the data in string form and make it string use single quot('')
data = '{"va1":"its value is 8","var 2 ":"its value is 88"}'

print(data)

new = json.loads(data)
print(new['va1'])
# using json module we are access any item with its key but using dictionary we
# can't use it
# print(json.load(data))


data2 = {  # this code now is python compatible
    "channel_name": "CodeWithHarry",
    "cars": ['bmw', 'audi a8', 'ferrari'],
    "fridge": ('roti', 540),
    "isbad": False
}

jscomp = json.dumps(data2)
"""
dumps() function use to make the code java-script compatible  
"""
print(jscomp)

"""
json.load() take file object as an argument when json.loads() take string as
an argument
"""