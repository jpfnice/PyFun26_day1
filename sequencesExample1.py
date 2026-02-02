
"""
   
Sequences (a specific kind of collection):
    list tuple str array
"""

# [] operator

name="Hello World"
print("First element", name[0])
print("Second element", name[1])
print("Last element", name[-1])

data=[4,5,6,10,56]
print("First element", data[0])
print("Second element", data[1])
print("Last element", data[-1])

# slices:

print(name[1:3])
print(data[1:3])
print(name[3:])
print(name[-2:])
print(data[0:5:2])
print(name[6:0:-1])

# concatenation: +

result=name + " Final"
print(result)
result=data + [6,8,99]
print(result)

# repeat *

result="*-" * 30
print(result)

result=[0] * 30
print(result)
