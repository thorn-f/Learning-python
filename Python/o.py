import time


x = [34, 343, 4, 35, 34, 53, 35]

i = 0
while True:
    time.sleep(1)
    print("Count", i)
    i += 1
    if i == 10:
        break
    