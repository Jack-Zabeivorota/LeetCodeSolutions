---------------------- SOLUTION 176 ----------------------------------
-- Table: Employee
-- +-------------+---------+
-- | Column Name |   Type  |
-- +-------------+---------+
-- | id          | int pk  |
-- | salary      | int     |
-- +-------------+---------+

-- Повертає другу по величені зарплату робітника, або якщо такої не має NULL
SELECT COALESCE(MAX(salary), NULL) AS SecondHighestSalary
FROM Employee
WHERE salary <> (SELECT MAX(salary) FROM Employee)

-- RESULT: SecondHighestSalary