# Exercise: Calculate the average of distinct integers from a list.
# The result should be rounded to 3 decimal places.

def average(array):
    # Convert the list to a set to remove duplicate numbers.
    distinct_numbers = set(array)
    # Calculate the average of the distinct numbers and round to 3 decimals.
    return round(sum(distinct_numbers) / len(distinct_numbers), 3)

if __name__ == '__main__':
    # Read the number of elements (unused in this solution but part of input format).
    n = int(input())
    # Read the list of integers from input.
    arr = list(map(int, input().split()))
    # Calculate the average of distinct numbers.
    result = average(arr)
    # Output the result.
    print(result)
