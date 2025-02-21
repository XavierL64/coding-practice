# Exercise: Merge the Tools
# Given a string and an integer k, split the string into substrings of length k.
# For each substring, remove duplicate characters (preserving order) and print the result.

def merge_the_tools(string, k):
    # Iterate over the string in steps of k to get each substring.
    for i in range(0, len(string), k):
        # Extract a substring of length k.
        substring = string[i:i+k]
        
        # Remove duplicates while preserving the order using dict.fromkeys().
        result = ''.join(dict.fromkeys(substring))
        
        # Print the result for the current substring.
        print(result)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
