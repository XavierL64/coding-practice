-- Query for the city with the shortest name.
-- This query selects the CITY and its length from the STATION table where the length matches
-- the minimum length found in the table. It orders the results alphabetically and returns one row.
SELECT CITY, LENGTH(CITY)
FROM STATION
WHERE LENGTH(CITY) = (SELECT MIN(LENGTH(CITY)) FROM STATION)
ORDER BY CITY LIMIT 1;

-- Query for the city with the longest name.
-- This query selects the CITY and its length from the STATION table where the length matches
-- the maximum length found in the table. It orders the results alphabetically and returns one row.
SELECT CITY, LENGTH(CITY)
FROM STATION
WHERE LENGTH(CITY) = (SELECT MAX(LENGTH(CITY)) FROM STATION)
ORDER BY CITY LIMIT 1;
