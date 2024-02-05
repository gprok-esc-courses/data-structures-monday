
a = 5
b = 5
a = 10

print(hex(id(a)))
print(hex(id(b)))

print("LIST")
data = [10, 20, 40, 50]
for i in range(len(data)):
    print(hex(id(data[i])))