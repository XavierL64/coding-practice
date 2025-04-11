# Exercise: Given two timestamps in the format "Day dd Mon yyyy hh:mm:ss +xxxx", compute and print the absolute difference (in seconds) between the two timestamps. The first input line contains T, the number of test cases, and each test case consists of two timestamps.

from datetime import datetime

def time_delta(t1, t2):

    # Convert timestamp strings to a datetime object.
    dt1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    dt2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    
    # Calculate the absolute difference between the two datetime objects.
    diff = abs(dt2 - dt1)
    
    # Return the total difference in seconds.
    return str(int(diff.total_seconds()))

# Read the number of test cases.
T = int(input())

# Process each test case.
for _ in range(T):
    t1 = input()  
    t2 = input()
    print(time_delta(t1, t2))
