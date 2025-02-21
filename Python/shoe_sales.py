# Exercise: Shoe Sales
# Compute total earnings from customer orders by selling available shoes.
# Only sell a shoe if its size is in stock.

from collections import Counter

# Read the number of shoes and their sizes.
num_shoes = int(input())
shoe_sizes = list(map(int, input().split()))
inventory = Counter(shoe_sizes)

# Read the number of customers.
num_customers = int(input())
total_sales = 0

# Process each customer order (desired size and offered price).
for _ in range(num_customers):
    size, price = map(int, input().split())
    if inventory[size] > 0:
        total_sales += price
        inventory[size] -= 1

# Print the total earnings.
print(total_sales)
