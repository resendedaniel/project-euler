import math

# # Recursion explodes
# def get_diagonals(i):
#     if i == 0:
#         return(i + 1)
#     x = get_diagonals(i - 1)
#     return x + (i*2+1)**2*4-6*(i*2)

def get_diagonals(n):
    sum = 1
    current = 1
    for i in range((n - 1) * 4):
        increment = int((math.floor(i / 4) + 1) * 2)
        current += increment
        sum += current
    return sum

print(get_diagonals(501))


print(get_diagonals(1) == 1)
print(get_diagonals(2) == 25)
print(get_diagonals(3) == 101)
print(get_diagonals(4) == 261)
print(get_diagonals(5) == 537)
print(get_diagonals(101) == 5434201)
print(get_diagonals(1000) == 5327337997)

