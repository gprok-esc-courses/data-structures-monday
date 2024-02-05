import random

data = [random.randint(1, 1000) for i in range(20)]
print(data)

n = int(input("Give a number: "))

found = False 
for value in data:
    if value == n:
        print("Found")
        found = True
        break
if not found:
    print("Not found")

data = sorted(data)
print(data)