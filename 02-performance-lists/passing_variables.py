
# Passing by VALUE
def change_int(n):
    n = n * 2

# Passing by REFERENCE
def change_list(data):
    data = [1,2,3,4]
    for i in range(len(data)):
        data[i] = data[i] * 2


a = 5
change_int(a)
print(a)

d = [1, 2, 3, 4]
change_list(d)
print(d)