# Exercise: Calculate and print the average marks of a queried student, formatted to 2 decimal places.

if __name__ == '__main__':
    # Read the number of student records.
    n = int(input())
    
    # Initialize a dictionary to store each student's name and list of marks.
    student_marks = {}
    
    # Read each student's data.
    for _ in range(n):
        # Split input: the first value is the student's name and the rest are marks.
        name, *line = input().split()
        # Convert the marks from strings to floats.
        scores = list(map(float, line))
        # Store the student's marks in the dictionary.
        student_marks[name] = scores
    
    # Read the name of the student for whom the average is to be calculated.
    query_name = input()
    
    # Retrieve the marks list for the queried student.
    marks = student_marks[query_name]
    
    # Calculate the average of the marks.
    marks_average = sum(marks) / len(marks)
    
    # Print the average marks formatted to 2 decimal places.
    print(f"{marks_average:.2f}")
