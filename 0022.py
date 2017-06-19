import string
import numpy as np
from data import get_file
from time import *

start = clock()

letters = list(string.ascii_lowercase)
letters = dict(zip(letters, np.array(range(len(letters))) + 1))

data = get_file('p022_names.txt')
data.sort()

scores = 0
for i in range(len(data)):
    d = str.lower(data[i])
    score = sum(map(lambda x: letters[x], d)) * (i + 1)
    scores += score

print(scores)
print("Time taken = %.2f" % (clock()-start) + 's')


# # First load the file and sort it.
#
# x = eval( '[' + open( '.../names.txt' ).readlines()[ 0 ] + ']' )
# x.sort()
#
# # Then calculate what is needed.
#
# reduce( lambda x, y: x + y, [ reduce( lambda x, y: x + y, [ ( j + 1 ) * ( ord( i ) - 64 ) for i in x[ j ] ] ) for j in xrange( len( x ) ) ] )


# def p22():
#     f = open("names.txt")
#     names = sorted([n.strip('"') for n in f.read().split(',')])
#
#     total = 0
#     a = ord('A')
#     for i in range(len(names)):
#         total += sum([ord(c)-a+1  for c in names[i]]) * (i+1)
#     print total
#
# def main():
#     from timeit import Timer
#     print Timer('p22()', 'from __main__ import p22').timeit(1)
#
# if __name__ == '__main__': main()