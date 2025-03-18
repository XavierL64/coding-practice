# Exercise: Cubed Fibonacci Sequence
# This program calculates the first n Fibonacci numbers, cubes each number,
# and prints the resulting list. The Fibonacci sequence starts with 0 and 1.

# Lambda function to cube a number.
cube = lambda x: x ** 3

def fibonacci(n):
    """
    Generate a list of the first n Fibonacci numbers.
    For the first two elements, use the index value (0 and 1).
    For subsequent elements, sum the two preceding numbers.
    """
    nums = []  # Initialize the list to hold Fibonacci numbers.
    for i in range(n):
        if len(nums) > 1:
            # For n >= 3, the next number is the sum of the last two numbers.
            new_num = nums[-1] + nums[-2]
            nums.append(new_num)
        else:
            # For the first two numbers, use the index values: 0 and 1.
            new_num = i
            nums.append(new_num)
    return nums

if __name__ == '__main__':
    # Read an integer from input that represents how many Fibonacci numbers to generate.
    n = int(input())
    # Map the cube function to each Fibonacci number, convert to a list, and print the result.
    print(list(map(cube, fibonacci(n))))
