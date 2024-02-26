from time import sleep
import random

def count(id):
    for i in range(5):
        print("id", id, " Value", i)
        sleep(random.randint(1, 5))


for id in range(4):
    count(id)
