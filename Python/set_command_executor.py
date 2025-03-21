# Exercise: The program first reads a set of integers, then processes a series of commands (such as pop, remove, and discard) to modify the set accordingly. Finally, it prints the sum of the remaining elements in the set.

# Read the number of elements in the set
n = int(input())

# Create a set of integers from the input
s = set(map(int, input().split()))

# Read the number of commands to process
N = int(input())

# Process each command
for _ in range(N):
    # Split the input into the command and an optional argument
    user_input = input().split()
    command = user_input[0]
    
    # If an argument is provided, convert it to an integer and execute the command with the argument
    if len(user_input) > 1:
        value = int(user_input[1])
        getattr(s, command)(value)
    else:
        # If no argument is provided, execute the command without any arguments
        getattr(s, command)()

# Output the sum of the elements remaining in the set
print(sum(s))
