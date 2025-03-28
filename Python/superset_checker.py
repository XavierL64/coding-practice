# Exercise: check if set A is a strict superset of each of the n given sets.

# Read set A from input (space-separated integers)
A = set(map(int, input().split()))

# Read the number of test sets
n = int(input())

# Iterate over each test set
for _ in range(n):
    # Read the current test set B from input
    B = set(map(int, input().split()))
    
    # If A is not a strict superset of B, print False and exit the loop
    if not (A > B):
        print(False)
        break

# The else block runs if the loop completes without breaking 
else:
    print(True)
