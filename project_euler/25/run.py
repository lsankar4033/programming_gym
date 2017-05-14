import math

prev_2 = 1
prev_1 = 1
i = 3
while True:
    cur = prev_1 + prev_2

    if len(str(cur)) >= 1000:
        print(i)
        break

    prev_2 = prev_1
    prev_1 = cur
    i += 1
