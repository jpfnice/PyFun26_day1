

data=input("Please enter a value: ")
print(data, type(data))

data=45
print(data, type(data))

data= 12 > 0
print(data, type(data))

data=78

if isinstance(data, int):
    print(data/3)

data=input("Please enter a value: ")
print(data, type(data)) # here data is a str
data=int(data)
print(data, type(data)) # here data is an int


