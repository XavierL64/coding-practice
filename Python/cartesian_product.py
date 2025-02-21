# Exercise: Compute the cartesian product of two sorted lists A and B.

from itertools import product

# Read the input lists as tuples of integers.
A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))

# Compute the cartesian product of A and B.
cartesian_products = list(product(A, B))

# Print all tuples from the cartesian product on one line, separated by spaces.
print(*cartesian_products)
