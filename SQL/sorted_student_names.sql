-- Exercise: Retrieve student names with Marks > 75,
-- ordered by the last three letters of Name and then by ascending ID.
SELECT Name
FROM STUDENTS
WHERE Marks > 75
ORDER BY RIGHT(Name, 3), ID;