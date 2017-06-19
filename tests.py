from api import *

print('Testing get_primes')
print(get_primes(0) == [])
print(get_primes(1) == [])
print(get_primes(2) == [2])
print(get_primes(3) == [2, 3])
print(get_primes(10) == [2, 3, 5, 7])
print(get_primes(100) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

print('Testing factorise')
print(factorise(12) == [2, 2, 3])
print(factorise(7) == [7])
print(factorise(402351) == [3, 43, 3119])

print('Find divisors')
print(find_divisors([2]) == [1, 2])
print(find_divisors([2, 3]) == [1, 2, 3, 6])
print(find_divisors([2, 2]) == [1, 2, 4])
print('NEEDS TO FIX THIS', find_divisors(factorise(30)) == [1, 2, 3, 5, 6, 10, 15, 30])

print('Testing calc_fibonacci')
print(calc_fibonacci(100) == [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144])

print('Testing is_palindrome')
print(is_palindrome(5433) == False)
print(is_palindrome(3333) == True)
print(is_palindrome(5) == True)
print(is_palindrome(123321) == True)
print(is_palindrome(12321) == True)
print(is_palindrome(123) == False)
