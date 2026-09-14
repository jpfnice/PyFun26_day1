# How to increment all elements of a list of number by 5 ?

# Here is the original list:
    
data1=[5,6,7,10,20,4,3]

# data2=data1+5 does not work: I cannot add an int to a list
# I need to add 5 to each element of data1 in turn :
    
data2=[]
for elt in data1:
    data2.append(elt+5)

print(data2)
    
# What if I use the sequence ndarray provided by the module numpy?

import numpy
array1=numpy.array(data1) # array() is a ndarray constructor
array2=array1+5 # This works ! No need of using a loop
print(array2)
# If I want to obtain a list I can convert an ndarray into a list this way:
data3=list(array2)
print(data3) # data3 is a list

