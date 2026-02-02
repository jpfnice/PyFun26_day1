# while loop
# syntax:
    
# while condition:
#    bloc

nb=100
# + - * / %
# > < >= <= == != and or not
while nb >= 0 :
    if nb % 3 == 0:
        print(nb, "can be divided by 3")
    else:
        print("nb is", nb)
    nb=nb-1
    
print("The end")
