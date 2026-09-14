
"""
list (a mutable kind of sequence)
    
    
"""

# Creation:

data=[] # an empty list

data=[6,7,True,5.6,"abc", [7,8]]
print(data, len(data))

data=list() # <=> [] an empty list

data=list("abcdef")
print(data)

# To update a list:
data=[6,4,7]
print(data)
data[0]=100
print(data)
data.append(45) # objectname.methodsname(param1, param2, ...)
print(data)
data.extend([5,55,75,89])
print(data)
data.insert(1,99)
print(data)
data.pop() # remove the last element
print(data)
data.pop(0) # remove the element at position
print(data)
if 77 in data:
    data.remove(77)
print(data)
data.clear()
print(data)
data=[6,4,7,8,33,20]
print(data)
print(data[1:4])
data[1:4]=[31,32,33,33,35]
print(data)

# Various methods

print(data.count(33)) # print the number of time 33 appears in the list data
print("the position of 35 is data is", data.index(35))

print(data)
data.reverse()
print(data)

data.sort()
print(data)
