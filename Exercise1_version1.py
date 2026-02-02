"""
Write a Python script that prompts the user for a number(an integer) and displays a message that indicates if the number is odd, even or zero.
You can use the modulo operator (%) to determine if a number is even or not: 
    value % 2 returns the remainder of the division of value by 2
    If this remainder is 0 value is even
    
After having tested a first number, the script should prompt the user for other numbers, and continue to run as long as the user does not enter the string "stop".
"""


nb=input("Please enter a numeric value: ")

nb=int(nb)  # to convert the provided string into an int

if nb == 0:
    print(nb, "is Zero")
elif nb % 2 == 0:
    print(nb, "is even")
else:
    print(nb, "is odd")
