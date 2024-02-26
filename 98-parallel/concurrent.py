from time import sleep
import random
import threading

def count(id):
    for i in range(5):
        print("id", id, " Value", i)
        sleep(random.randint(1, 5))


threads = []
for id in range(4):
    th = threading.Thread(target=count, args=(id,))
    threads.append(th)
    th.start()
for th in threads:
    th.join()
print("COMPLETED")