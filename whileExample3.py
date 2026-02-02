# while loop and break statement
# syntax:
    
# while condition:
#    bloc

nb=50
# + - * / %
# > < >= <= == != and or not
while nb >= 0:
    print("nb is", nb)
    nb=nb-1
    if nb == 21:
        break # leave the loop (irrespective of the loop condition value)
    
print("The end")
