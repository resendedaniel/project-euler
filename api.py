import numpy as np
from collections import Counter

def get_primes(n=100):
    '''
    Generate primes using the sieve algorithm
    '''
    if n == 2:
        return [2]
    elif n < 2:
        return []
    s = range (3, n+1, 2)
    mroot = n ** 0.5
    half = ((n + 1) / 2) - 1
    i = 0
    m = 3
    while m <= mroot:
        if s[i]:
            j = (m * m - 3) / 2
            s[j] = 0
            while j < half:
                s[j] = 0
                j += m
        i = i+1
        m = 2 * i + 3
    return [2] + [x for x in s if x]


def calc_fibonacci(n=100):
    '''
    Generates a Fibonacci sequence up to n

    :param n: Sequence's upper limit
    :return: list of fibonacci's sequence
    '''
    a1 = 0
    a2 = 1

    output = []

    while a2 < n:
        a1, a2 = a2, a1 + a2
        output.append(a2)

    return output


def factorise(x):
    '''
    Factorise a number

    :param x: Integer to be factored
    :return: list of factors
    '''
    n = 2
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

def find_divisors(factors = []):
    '''
    Find divisors given factors

    :param factors: list of factors [try factorise(n)]
    :return: list of divisors
    '''
    n = len(factors)
    output = [1]
    for i in range(n):
        for j in range(i, n+1):
            output += [np.prod(factors[i:j])]
    output = np.sort(np.unique(output))

    return output

def is_palindrome(x):
    '''
    Checks if a number is palindrome

    :param x:
    :return:
    '''
    x = str(x)
    n = len(x)
    n = n - (n % 2)
    n = n / 2

    boo = 1
    for i in range(n):
        boo *= x[i] == x[-(i+1)]

    return boo

def is_pandigital(x, up_to=9):
    '''
    Pandigital are numbers that contains all digits like 123456789.

    :param x:
    :param up_to: Not implemented yet
    :return:
    '''
    arr_char = list(str(x))
    if np.sum([int(n) for n in arr_char]) == 45:
        return not any(np.array(Counter(arr_char).values()) > 1)
    return False
