# Exercise: Swap the case of each letter in a given string.
# This code converts all uppercase letters to lowercase and vice versa.

def swap_case(s):
    # Create a list by iterating through each character in the string.
    # For each character, if it's uppercase, convert it to lowercase;
    # otherwise, convert it to uppercase.
    swapped = [char.lower() if char.isupper() else char.upper() for char in s]
    # Join the list back into a single string and return it.
    return ''.join(swapped)

if __name__ == '__main__':
    # Read the input string from the user.
    s = input()
    # Get the string with swapped cases.
    result = swap_case(s)
    # Print the resulting string.
    print(result)