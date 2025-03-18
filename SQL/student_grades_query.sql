-- Exercise: The query computes student grades by joining the "students" and "grades" tables,
-- then conditionally selects the student's name based on the grade,
-- and orders the results by grade (in descending order) and by student name or marks (in ascending order).

WITH student_grades AS (
    -- Create a common table expression (CTE) that joins the students and grades tables.
    -- Each student's marks are matched to a grade by checking if they fall between the grade's min_mark and max_mark.
    SELECT st.name, gr.grade, st.marks
    FROM students AS st
    CROSS JOIN grades AS gr
    WHERE st.marks BETWEEN gr.min_mark AND gr.max_mark
)

SELECT 
    -- Conditionally include the student's name if the grade is at least 8; otherwise, return NULL.
    CASE WHEN grade >= 8 THEN name ELSE NULL END AS student_name,
    grade, 
    marks
FROM student_grades
ORDER BY 
    grade DESC,  -- Order the results by grade in descending order.
    -- For tie-breaking, if student_name is not NULL, order by student_name; otherwise, order by marks.
    CASE WHEN student_name IS NOT NULL THEN student_name ELSE marks END ASC;
