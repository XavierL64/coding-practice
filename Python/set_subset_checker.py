# Exercise: Determine if set A is a subset of set B using the .intersection() method.

# Read the number of test cases.
T = int(input())

for _ in range(T):
    # Read and create set A.
    length_A = int(input())
    A = set(map(int, input().split()))
    
    # Read and create set B.
    length_B = int(input())
    B = set(map(int, input().split()))
    
    # Calculate the intersection of A and B.
    intersection = A.intersection(B)
    
    # If the intersection equals A, then every element of A is in B.
    if intersection == A:
        print(True)
    else:
        print(False)

# Alternative solution using issubset
 print(A.issubset(B))