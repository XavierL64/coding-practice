# Exercise: Given student names and grades, print the names of students with the second lowest grade.

if __name__ == '__main__':
    # Initialize an empty list to hold student records.
    students = []
    
    # Read the total number of students.
    for _ in range(int(input())):
        # Read the student's name.
        name = input()
        # Read the student's grade as a floating-point number.
        score = float(input())
        # Append the student record as a [name, score] pair.
        students.append([name, score])

    # Create a sorted list of unique grades.
    unique_grades = sorted(set(student[1] for student in students))
    # The second lowest grade will be at index 1.
    second_lowest_score = unique_grades[1]

    # Filter out the names of students whose grade matches the second lowest grade,
    # and sort these names alphabetically.
    second_lowest_students = sorted([student[0] for student in students if student[1] == second_lowest_score])

    # Print each student's name on a new line.
    for student in second_lowest_students:
        print(student)