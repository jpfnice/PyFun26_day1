
"""
Collections:
    list tuple set dict str array ....
    
Sequences (a specific kind of collection):
    list tuple str array
"""

# length of a collection: len()

name="Hello World"
print("Size of", name, "is", len(name))

data=[4,5,6,10,56]
print("Size of", data, "is", len(data))

# you can the presence of an element with "in", "not in":
    
if "W" in name:
    print("W is present")
    
if 6 in data:
    print("6 is present")
    
# you can iterate through their elements with a for loop:
    
for element in name:
    print(element)
    
for element in data:
    print(element)

    
    