# Exercise: For a given integer n, print the decimal, octal, hexadecimal, and binary representations
# of each integer from 1 to n, right-aligned to the width of the binary representation of n.

def print_formatted(number):
    # Calculate the padding width based on the length of the binary representation of n (without the '0b' prefix)
    padding = len(bin(number)[2:])
    for i in range(1, number + 1):
        # Format each representation:
        # - Decimal: convert to string and right-align using rjust
        # - Octal: remove the '0o' prefix and right-align
        # - Hexadecimal: remove the '0x' prefix, convert to upper case and right-align
        # - Binary: remove the '0b' prefix and right-align
        dec_str = str(i).rjust(padding)
        oct_str = oct(i)[2:].rjust(padding)
        hex_str = hex(i)[2:].upper().rjust(padding)
        bin_str = bin(i)[2:].rjust(padding)
        # Concatenate the formatted strings with a single space between them and print the result.
        print(dec_str + " " + oct_str + " " + hex_str + " " + bin_str)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
