-- Exercise: Query a list of distinct city names from the STATION table
-- for cities that have an even ID number.

SELECT DISTINCT(CITY)
FROM STATION
WHERE ID % 2 = 0;
