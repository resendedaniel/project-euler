# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

for a in range(1, 1001):
    for b in range(1, 1001 - a) :
        c = 1000 - a - b
        if (a**2 + b**2 - c**2 == 0):
            print(a, b, c, ' = ', a*b*c)

# neat
[(x,y,1000-x-y) for x in range(1,1000) for y in range(1,x) if x**2+y**2==(1000-x-y)**2]