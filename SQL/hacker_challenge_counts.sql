-- Exercise: The query computes the number of distinct challenges associated with each hacker,
-- then retrieves hackers who have either the maximum challenge count or a unique challenge count,
-- and orders the results by challenge count (in descending order) and hacker ID (in ascending order).

WITH challenge_counts AS (
    SELECT 
        ha.hacker_id,                    -- Select the hacker's unique identifier
        ha.name,                         -- Select the hacker's name
        COUNT(DISTINCT ch.challenge_id) AS challenge_number  -- Count the distinct challenges per hacker
    FROM hackers AS ha
    JOIN challenges AS ch ON ha.hacker_id = ch.hacker_id  -- Join hackers with challenges based on hacker_id
    GROUP BY ha.hacker_id, ha.name      -- Group by hacker to calculate each hacker's challenge count
)

SELECT 
    hacker_id, 
    name, 
    challenge_number
FROM challenge_counts
WHERE 
    -- Select hackers with the maximum challenge count...
    challenge_number = (SELECT MAX(challenge_number) FROM challenge_counts)
    -- ...or hackers whose challenge count is unique (appearing only once in the dataset)
    OR challenge_number NOT IN (
        SELECT challenge_number 
        FROM challenge_counts 
        GROUP BY challenge_number 
        HAVING COUNT(*) > 1
    )
ORDER BY 
    challenge_number DESC,  -- Order by challenge count in descending order
    hacker_id;              -- Then order by hacker ID in ascending order
