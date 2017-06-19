from __future__ import division

def f(k):
    if k == 0:
        return 1
    return k
def f_sum(k, n):
    return sum([math.floor(i/k) for i in range(n+1)])

print(f_sum(5, 10)) # 18
print(f_sum(7, 100)) # 1003
print(f_sum(2, 10**3)) # 2648308895643

5*f(0) + 5*f(1) + f(2)
7*f(0) + 7*f(1) + 7*(2) + 7*f(3) + 7*f(4) + 7*f(5) + 7*f(6) + 7*f(8) + 7*f(9) + 7*f(10) + 7*f(11) + 7*f(12) + 7*f(13) + 3*f(14)
