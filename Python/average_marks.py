# Exercise: Compute the average marks from student records using namedtuple.
# The records include the columns ID, MARKS, CLASS, and NAME in any order.

from collections import namedtuple

# Read the total number of student records.
N = int(input())

# Create a Student namedtuple using the header (columns are provided in any order).
Student = namedtuple('Student', input().split())

# Sum the MARKS field from each student record.
total_marks = sum(int(Student(*input().split()).MARKS) for _ in range(N))

# Calculate the average marks.
average_marks = total_marks / N

# Print the average marks formatted to 2 decimal places.
print(f"{average_marks:.2f}")
