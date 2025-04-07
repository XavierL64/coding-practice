# Exercise: For each test case, read two values and attempt to perform integer division.
# If division by zero or an invalid literal error occurs, print the error message prefixed by "Error Code:".
# Otherwise, print the result of the integer division.

T = int(input())

for _ in range(T):
    a, b = input().split()
    
    try:
        print(int(a) // int(b))
        
    except ZeroDivisionError as e:
        print(f"Error Code: {e}")
    
    except ValueError as e: 
        print(f"Error Code: {e}")
