# EXERCISE: Make bubble sort a function,
# then run with large lists of random values,
# and empirically calculate the order of growth (Big O)

data = [87, 91, 44, 67, 11, 45, 22, 1]

stop = len(data) - 1
for iter in range(len(data)-1):
    for i in range(stop):
        if data[i] > data[i+1]:
            data[i], data[i+1] = data[i+1], data[i]
    stop -= 1

    print(data)