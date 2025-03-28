-- Exercise:
-- Pivot the OCCUPATIONS table so that each occupation (Doctor, Professor, Singer, Actor)
-- becomes a column. The names are sorted alphabetically and aligned by their row number.
-- If an occupation lacks a name for a given row, NULL is displayed.

WITH OrderedOccupations AS (
    -- Create a Common Table Expression (CTE) to:
    -- 1. Sort names alphabetically within each occupation.
    -- 2. Assign a row number (rn) to each name, restarting for each occupation.
    SELECT
        Name,
        Occupation,
        ROW_NUMBER() OVER (PARTITION BY Occupation ORDER BY Name) AS rn
    FROM OCCUPATIONS
)
SELECT
    -- Pivot the data by grouping on rn and using conditional aggregation:
    -- For each occupation, the CASE expression returns the name when the condition matches;
    -- MAX() then picks the non-null value from each group.
    MAX(CASE WHEN Occupation = 'Doctor' THEN Name END) AS Doctor,
    MAX(CASE WHEN Occupation = 'Professor' THEN Name END) AS Professor,
    MAX(CASE WHEN Occupation = 'Singer' THEN Name END) AS Singer,
    MAX(CASE WHEN Occupation = 'Actor' THEN Name END) AS Actor
FROM OrderedOccupations
GROUP BY rn      -- Group by row number to align names from different occupations
ORDER BY rn;     -- Order the final output by the row number (alphabetical order)
