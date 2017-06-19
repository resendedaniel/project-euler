from api import calc_fibonacci
from time import *

start = clock()

fib = [1] + calc_fibonacci(10**1000)
print(sum([len(str(f)) < 1000 for f in fib]) + 1)

print("Time taken = %.2f" % (clock()-start) + 's')

# from math import ceil
# print(ceil((1000 - 1 + math.log10(math.sqrt(5))) / math.log10((1+math.sqrt(5))/2)))
