# Exercise: Modify a string by replacing the character at a specified index.
# This code demonstrates how to mutate an immutable string by converting it to a list,
# updating the desired index, and then joining the list back into a string.

def mutate_string(string, position, character):
    # Convert the immutable string into a list of characters to allow modification.
    list_string = list(string)
    # Replace the character at the specified position.
    list_string[position] = character
    # Convert the list back into a string.
    string = ''.join(list_string)
    return string

if __name__ == '__main__':
    # Read the input string.
    s = input()
    # Read the position and new character, splitting the input into two parts.
    i, c = input().split()
    # Convert the position from string to integer and call the mutate_string function.
    s_new = mutate_string(s, int(i), c)
    # Print the updated string.
    print(s_new)