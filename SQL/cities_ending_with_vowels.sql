-- This query selects unique CITY names from the STATION table
-- where both the first and last characters of the city name are vowels.
SELECT DISTINCT CITY
FROM STATION
WHERE 
    -- Extract the first character, convert it to lowercase, and check if it's a vowel.
    LOWER(SUBSTR(CITY, 1, 1)) IN ('a', 'e', 'i', 'o', 'u')
    -- Extract the last character and check if it's a vowel.
    AND SUBSTR(CITY, LENGTH(CITY), 1) IN ('a', 'e', 'i', 'o', 'u');
