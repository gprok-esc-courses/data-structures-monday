
simple_list = []
simple_list.append(45)
simple_list.append(12)
simple_list.append(34)
simple_list.append(15)
simple_list.append(3)

print(simple_list)
simple_list.sort()
print(simple_list)


class Demo:
    def __init__(self, v, d) -> None:
        self.value = v 
        self.distance = d

    def __str__(self) -> str:
        return "[" + self.value + " " + str(self.distance) + "]"
    

demo_list = []
demo_list.append(Demo('A', 10))
demo_list.append(Demo('B', 6))
demo_list.append(Demo('C', 12))
demo_list.append(Demo('D', 8))
demo_list.append(Demo('E', 2))

for item in demo_list:
    print(item, end=' ')
print()
demo_list.sort(key=lambda x : x.distance)
for item in demo_list:
    print(item, end=' ')
print()