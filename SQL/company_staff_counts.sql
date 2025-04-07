/*
Exercise: Company Staff Count Query
-------------------------------------
This query calculates the total number of staff members by role for each company. 
It retrieves the company code and founder from the Company table and uses 
LEFT JOINs on subqueries from the Lead_Manager, Senior_Manager, Manager, and Employee tables 
to count the distinct staff members in each role. The use of COALESCE ensures that if a company 
has no records in any role, a 0 is returned. The final output is ordered by company_code.
*/

SELECT 
    c.company_code,
    c.founder,
    COALESCE(lm.total_lead_managers, 0) AS total_lead_managers,
    COALESCE(sm.total_senior_managers, 0) AS total_senior_managers,
    COALESCE(m.total_managers, 0) AS total_managers,
    COALESCE(e.total_employees, 0) AS total_employees
FROM Company c
LEFT JOIN (
    SELECT company_code, COUNT(DISTINCT lead_manager_code) AS total_lead_managers
    FROM Lead_Manager
    GROUP BY company_code
) lm ON c.company_code = lm.company_code
LEFT JOIN (
    SELECT company_code, COUNT(DISTINCT senior_manager_code) AS total_senior_managers
    FROM Senior_Manager
    GROUP BY company_code
) sm ON c.company_code = sm.company_code
LEFT JOIN (
    SELECT company_code, COUNT(DISTINCT manager_code) AS total_managers
    FROM Manager
    GROUP BY company_code
) m ON c.company_code = m.company_code
LEFT JOIN (
    SELECT company_code, COUNT(DISTINCT employee_code) AS total_employees
    FROM Employee
    GROUP BY company_code
) e ON c.company_code = e.company_code
ORDER BY c.company_code;
