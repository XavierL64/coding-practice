# Exercise: Word Group Indexing
# Given two groups of words, Group A and Group B, print the 1-indexed positions of each occurrence of every word in Group B as it appears in Group A.
# If a word from Group B does not appear in Group A, print -1.

from collections import defaultdict

# Read the number of words in Group A (n) and Group B (m)
n, m = map(int, input().split())

# Build a dictionary mapping each word in Group A to its list of 1-indexed positions.
occurrences = defaultdict(list)
for i in range(n):
    word = input().strip()
    occurrences[word].append(i + 1)

# Read Group B words.
groupB = [input().strip() for _ in range(m)]

# For each word in Group B, print its occurrence positions or -1 if it doesn't appear.
for word in groupB:
    if word in occurrences:
        print(" ".join(map(str, occurrences[word])))
    else:
        print(-1)
