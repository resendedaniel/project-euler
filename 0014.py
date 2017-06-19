# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

def next_n(n):
    if n % 2 == 0:
        return n/2
    else:
        return n*3 + 1

def get_chain(n):
    chain = [n]
    while n > 1:
        n = next_n(n)
        chain += [n]
    return chain

print(get_chain(13) == [13,40,20,10,5,16,8,4,2,1])

chains = [(n, len(get_chain(n))) for n in range(1000001)]

largest = 0
largest_n = 0

for n, size in chains:
    if size >= largest:
        largest = size
        largest_n = n

print(chains[largest_n])
