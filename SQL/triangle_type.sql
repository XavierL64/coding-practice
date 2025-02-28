-- This query outputs the type of triangle based on side lengths in the TRIANGLES table.
SELECT 
  CASE 
    -- Check if the three sides satisfy the triangle inequality.
    WHEN A + B > C AND A + C > B AND B + C > A THEN
      CASE 
        -- All sides equal: Equilateral.
        WHEN A = B AND B = C THEN 'Equilateral'
        -- Two sides equal: Isosceles.
        WHEN A = B OR A = C OR B = C THEN 'Isosceles'
        -- Otherwise: Scalene.
        ELSE 'Scalene'
      END
    -- If the triangle inequality fails, it's not a valid triangle.
    ELSE 'Not A Triangle'
  END AS Triangle_Type
FROM TRIANGLES;
