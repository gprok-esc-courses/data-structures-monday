from time import time
import random 

def even_numbers_in_list(data):
    counter = 0
    for value in data:
        if value % 2 == 0:
            counter += 1
    return counter 


values = [10000, 100000, 1000000, 10000000, 100000000]

for n in values:
    data = [random.randint(1, 1000) for i in range(n)]
    start_time = time()
    even_numbers_in_list(data)
    end_time = time()
    print(n, " elapsed:", end_time-start_time)