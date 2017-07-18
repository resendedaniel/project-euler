import numpy as np

def digits_powered(n, power=4):
    n = str(n)
    return [int(d) ** power for d in n]

sum = 0
for x in range(2, 100000000):
    y = np.sum(digits_powered(x, 5))
    if y == x:
        sum += x

print(sum)

# 100000000 =