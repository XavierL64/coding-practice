-- Exercise:
-- Query 1: Retrieve an alphabetically ordered list of all names in OCCUPATIONS,
-- each immediately followed by the first letter of their occupation in parentheses.
-- Query 2: For each occupation, output a statement of the form:
-- "There are a total of [occupation_count] [occupation]s."
-- The occupation name should be in lowercase and results should be sorted by count (ascending)
-- and alphabetically for ties.

-- MySQL Version
SELECT CONCAT(Name, '(', LEFT(Occupation, 1), ')')
FROM OCCUPATIONS
ORDER BY Name;

SELECT CONCAT('There are a total of ', COUNT(Name), ' ', LOWER(Occupation), 's.')
FROM OCCUPATIONS
GROUP BY Occupation
ORDER BY COUNT(Name) ASC, LOWER(Occupation) ASC;

-- DB2 Version
SELECT NAME || '(' || SUBSTR(OCCUPATION, 1, 1) || ')' 
FROM OCCUPATIONS
ORDER BY NAME;

SELECT 'There are a total of ' || COUNT(NAME) || ' ' || LOWER(OCCUPATION) || 's.'
FROM OCCUPATIONS
GROUP BY OCCUPATION
ORDER BY COUNT(NAME) ASC, LOWER(OCCUPATION) ASC;
