
# if-else statement
# The syntax is:
    
# if condition:
#   bloc
# elif  condition:
#   bloc
# elif  condition:
#   bloc
# ...
# else:
#   bloc

value = input("Enter an integer: ")
value = int(value)

if value > 0:
    print(value, "is positive")
    result=value * 3
elif value < 0:
    print(value, "is negative")
    result=value / 3
else:
    print(value, "is zero")
    result=0

print("result is", result)
print("The end")





