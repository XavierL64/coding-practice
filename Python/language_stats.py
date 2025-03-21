# Exercise: Reads sets of integers representing ids of people who speak English and French,
# then calculates and prints the number of people who speak at least one language,
# only English, and exactly one language (i.e., either English or French but not both).

# Read the number of people who speak English
n = int(input())

# Create a set of integers representing people who speak English
english = set(map(int, input().split()))

# Read the number of people who speak French
b = int(input())

# Create a set of integers representing people who speak French
french = set(map(int, input().split()))

# Print the number of people who speak at least one language (English or French)
print(len(english.union(french)))

# Print the number of people who speak only English (those in English but not in French)
print(len(english.difference(french)))

# Print the number of people who speak exactly one language (either English or French but not both)
print(len(english.symmetric_difference(french)))
