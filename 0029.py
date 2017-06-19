import numpy as np

out = []
for i in range(2, 101):
    for j in range(2, 101):
        out.append(i**j)
print(len(np.unique(out)))

# len(set(a**b for a in range(2, 101) for b in range(2, 101)))