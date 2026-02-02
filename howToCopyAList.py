
data=[5,6,7]

#bis=data
bis=data.copy()

data.pop()
print(bis)

bis.extend([8,8,8])
print(data)

print(id(bis), id(data))

