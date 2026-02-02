"""
Step 1:
Write a Python script that prompts the user for several numbers (when the user 
enter the string "stop", the script will stop prompting for numbers).
The numbers entered will be stored into a list one after the other.

statements, functions and methods you could use:
while loop + input() function + int() or float() function + list append() or
insert() method

Step 2:
After having retrieved all the numbers, print the list.

statements, functions and methods you could use:
print() function

Step 3:
The script will then compute and print the minimum, the maximum and the mean 
of the different numbers present in the list.

statements, functions and methods you could use:
for or while loop + arithmetic operators
OR
predefine functions

Step 4:
Compute the "truncated mean" of the elements: 
the mean of all elements except the smallest and largest ones.

Example:
    if the list is:
    [3,4,3,6,77,3,77,55,45,45]
    
    the truncated mean will only take into account the elements:
    [4,6,55,45,45] (3 and 77 are ignored)

statements, functions and methods you could use:
    sort(), count(), slices, sum(), ...
    
"""

import statistics # to use the mean() function

numbers=[]   # Creation of an empty list <=> numbers=list()

# Step 1: we construct a list of int with the help of the user input
while True:
    answer=input("Enter an int or 'stop': ")
    if answer=='stop':
        break
    answer=int(answer)
    numbers.append(answer)
        
# Step 2: the list is being printed (and it's size)
print("The list numbers is:",numbers) 
print("The size of numbers is:", len(numbers))

# Step 3:

print("Maximum", max(numbers))
print("Minimum", min(numbers))
print("Mean", sum(numbers)/len(numbers))
print("Mean", statistics.mean(numbers))

# Another strategy to get the min and max 
numbers.sort()
print("Maximum", numbers[-1])
print("Minimum", numbers[0])

# If I want to compute the minimum, the maximum and the sum with my own code:

currentmin=numbers[0] 
currentmax=numbers[0] 
currentsum=numbers[0] 

# or :
# currentmin=currentmax=currentsum=numbers[0]

index=1 
while index < len(numbers):
    if numbers[index] > currentmax:
        currentmax = numbers[index]
    if numbers[index] < currentmin:
        currentmin = numbers[index]  
    currentsum = currentsum + numbers[index]
    index = index + 1
    
print("Maximum", currentmax)
print("Minimum", currentmin)
print("Mean", currentsum/len(numbers))

# Step 4:
    
#Version 1:
# numbers= [3,1,4,1,5,5,1]
minimum=min(numbers) # 1
maximum=max(numbers) # 5

while minimum in numbers: 
    numbers.remove(minimum)
    
while maximum in numbers:
    numbers.remove(maximum)

print("Truncated mean: ", sum(numbers)/len(numbers))

# Version 2:

# numbers= [3,1,4,1,5,5,1]
numbers.sort()
# numbers= [1,1,1,3,4,5,5]

maxocc=numbers.count(numbers[-1]) # 2
minocc=numbers.count(numbers[0]) # 3

#numbers[3:-2]
print("Truncated mean: ", sum(numbers[minocc:-maxocc])/len(numbers[minocc:-maxocc]))
