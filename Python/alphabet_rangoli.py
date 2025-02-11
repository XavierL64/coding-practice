# Exercise: Print an alphabet rangoli of a given size.

def print_rangoli(size):
    # Create a reversed list of letters from 'a' to the specified letter.
    letters = [chr(97 + i) for i in range(size)][::-1]
    
    # Calculate the total width of the pattern.
    width = 4 * size - 3
    
    pattern = []
    
    for i in range(size):
        # Build the left part of the row.
        left = letters[:i+1]
        # Build the right part by reversing left (excluding the last element).
        right = left[:-1][::-1]
        # Combine the parts with hyphens and center the row.
        row = '-'.join(left + right)
        pattern.append(row.center(width, '-'))
    
    # Form the full pattern by mirroring the top half.
    full_pattern = pattern + pattern[-2::-1]

    # Print the complete rangoli.
    print('\n'.join(full_pattern))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
