# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import numpy as np
from api import is_palindrome

x = 99


palindromes = []
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        if is_palindrome(i * j):
            palindromes = palindromes + [(i, j, i*j)]

print(palindromes)
np.max([p[2] for p in palindromes])

# Found this solution clap, clap:
# max([x*y for x in range(900,1000) for y in range(900,1000) if str(x*y) == str(x*y)[::-1]])