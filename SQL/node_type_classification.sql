-- Exercise: Given a Binary Tree table (BST) with columns N (node value) and P (parent node),
-- classify each node as 'Root' if P is NULL, 'Inner' if the node appears as a parent for any other node,
-- or 'Leaf' otherwise. Results are ordered by node value (N).

SELECT
    N,  
    CASE 
        WHEN P IS NULL THEN 'Root'       
        WHEN N IN (SELECT P FROM BST) THEN 'Inner'  
        ELSE 'Leaf'                     
    END
FROM BST
ORDER BY N ASC;  -
