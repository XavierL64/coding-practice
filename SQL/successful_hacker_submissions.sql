-- Exercise: The query retrieves the hacker IDs and names for hackers who have made successful submissions 
-- (where the submission score matches the challenge's difficulty score) on more than one distinct challenge.
-- The results are ordered by the number of distinct challenges solved (in descending order) and by hacker ID (in ascending order).

SELECT 
    ha.hacker_id,      -- Select the hacker's unique identifier
    ha.name            -- Select the hacker's name
FROM submissions AS su
    -- Join the challenges table to link each submission to its corresponding challenge
    JOIN challenges AS ch ON su.challenge_id = ch.challenge_id
    -- Join the difficulty table to get the expected score for each challenge based on its difficulty level
    JOIN difficulty AS di ON ch.difficulty_level = di.difficulty_level
    -- Join the hackers table to get hacker details
    JOIN hackers AS ha ON su.hacker_id = ha.hacker_id
WHERE 
    su.score = di.score  -- Filter to include only those submissions where the score matches the expected difficulty score
GROUP BY 
    ha.hacker_id,       -- Group results by hacker ID
    ha.name             -- and hacker name
HAVING 
    COUNT(DISTINCT su.challenge_id) > 1  -- Include only hackers who have solved more than one distinct challenge
ORDER BY 
    COUNT(DISTINCT su.challenge_id) DESC,  -- Order by the number of distinct challenges solved in descending order
    ha.hacker_id ASC;                       -- In case of ties, order by hacker ID in ascending order
