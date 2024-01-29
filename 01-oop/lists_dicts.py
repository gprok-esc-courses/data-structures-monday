
data = [23, 45, 12, 15, 54, 27, 26, 45, 87, 34, 36]

print(len(data))
print(data[-1])

print(data[4:])

list2d = [
    ['X', 'O', '-'],
    ['-', 'X', '-'],
    ['O', '-', 'X']
]

print(list2d[0][0])

for i in range(3):
    for j in range(3):
        print(list2d[i][j], end=' ')
    print()

