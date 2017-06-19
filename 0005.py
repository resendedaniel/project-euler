# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import numpy as np
from api import factorise

cumulative_factors = []
for x in range(21):
    # cumulative_factors += factorise(3)
    comparison = cumulative_factors[:]
    to_be_add = []
    for f in factorise(x):
        if f in comparison:
            comparison.pop(comparison.index(f))
        else:
            to_be_add = to_be_add + [f]

    cumulative_factors = cumulative_factors + to_be_add

print(np.prod(cumulative_factors))

# Neat solution
# i = 1
# for k in (range(1, 21)):
#     if i % k > 0:
#         for j in range(1, 21):
#             if (i*j) % k == 0:
#                 i *= j
#                 break
# print i