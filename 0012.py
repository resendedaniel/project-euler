import numpy as np
import math

def find_factors(x, n=2):
    out = []
    while x >= n:
        if x % n == 0:
            out = out + [n]
            x = x / n
        else:
            if x > n:
                n = n - (not (n % 2)) + 2
            else:
                break

    return out

def find_n_divisors(factors):
    # to do: Need to find combination possibilities considering repeated factors
    n = len(factors)
    r = n - len(np.unique(factors))
    return math.factorial(n) / (math.factorial(r) * math.factorial(n-r))


n_divisors = [find_n_divisors(find_factors(x)) for x in [1,3,6,10,15,21,28]]
print(n_divisors)
print(n_divisors == [1,2,4,4,4,4,6])



