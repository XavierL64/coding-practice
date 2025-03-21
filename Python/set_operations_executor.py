
# Exercise: Reads a set A, applies a series of set operations with another set B, and prints the sum of A.

# Read the number of elements in set A.
n = int(input())

# Create set A from input.
A = set(map(int, input().split()))

# Read the number of operations to perform.
N = int(input())

# Process each set operation.
for _ in range(N):
    # Read the operation and the number of elements for set B.
    user_input = input().split()
    operation = user_input[0]
    length = int(user_input[1])
    
    # Create set B from input.
    B = set(map(int, input().split()))
    
    # Execute the specified operation on set A using set B.
    getattr(A, operation)(B)

# Print the sum of the elements in set A.
print(sum(A))
