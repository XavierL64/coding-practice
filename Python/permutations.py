# Exercise: Given a string 's' and an integer 'k', generate all permutations of length k from the string.
# Output the permutations in lexicographic (alphabetical) order, one per line.

from itertools import permutations

# Read the input and split into string s and integer k (as a string)
s, k = input().split()

# Generate k-length permutations from s, join each permutation tuple into a string,
# sort them in lexicographic order, and print each permutation on a new line.
for p in sorted(''.join(p) for p in permutations(s, int(k))):
    print(p)