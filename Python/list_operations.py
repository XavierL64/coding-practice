# Exercise: Process a series of list commands (insert, print, remove, append, sort, pop, reverse) to modify a list.

if __name__ == '__main__':
    # Read the number of commands.
    N = int(input())
    
    # Initialize an empty list to perform operations.
    my_list = []
    
    # Process each command.
    for _ in range(N):
        # Split the input command into its components.
        command = input().split()
        # The first component determines the operation.
        operation = command[0]
        
        if operation == 'insert':
            # Convert parameters to integers: index and element.
            i, e = int(command[1]), int(command[2])
            my_list.insert(i, e)
        elif operation == 'print':
            # Print the current state of the list.
            print(my_list)
        elif operation == 'remove':
            # Convert the element to remove to an integer.
            e = int(command[1])
            my_list.remove(e)
        elif operation == 'append':
            # Convert the element to append to an integer.
            e = int(command[1])
            my_list.append(e)
        elif operation == 'sort':
            # Sort the list in ascending order.
            my_list.sort()
        elif operation == 'pop':
            # Remove the last element from the list.
            my_list.pop()
        elif operation == 'reverse':
            # Reverse the order of the list.
            my_list.reverse()
