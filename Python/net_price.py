# Exercise: Given a list of N purchased items (each with an item name and price),
# compute and print the net price for each item.
# The net price is defined as: price × quantity sold.
# The output should display each item in order of its first occurrence.

from collections import OrderedDict

# Read the total number of items.
N = int(input())

# Use OrderedDict to preserve the order of first occurrence of each item.
purchases = OrderedDict()

for _ in range(N):
    # Read the input line and split it into item name and price.
    # rsplit is used to correctly capture item names that may contain spaces.
    item, price = input().rsplit(maxsplit=1)
    
    # Convert the price from string to integer.
    price = int(price)
    
    # If the item is already in purchases, increment its quantity by 1.
    if item in purchases:
        purchases[item]['quantity'] += 1
    else:
        # Otherwise, add the item with its price and an initial quantity of 1.
        purchases[item] = {'price': price, 'quantity': 1}

# For each item, calculate the net price (price multiplied by the quantity sold)
# and print the item name and the net price.
for item, data in purchases.items():
    net_price = data['price'] * data['quantity']
    print(f"{item} {net_price}")
