# Expression that return boolean result

nb=45

print(nb > 0) # True
print(nb < 0) # False

print(nb > 10 and nb < 50) # True

nb=55
print(nb > 10 and nb < 50) # False

message="stop"

print(message == "stop") # True
print(message == "Stop") # False

print(message != "start") # True

nb=10

print(nb==10 or nb<5) # True
nb=4
print(nb==10 or nb<5) # True
print( not(nb==10 or nb<5)) # False
