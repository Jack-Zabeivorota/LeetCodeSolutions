--------------------- SOLUTION 184 -----------------------------------
-- Table: Employee
-- +--------------+---------+
-- | Column Name  | Type    |
-- +--------------+---------+
-- | id           | int pk  |
-- | name         | varchar |
-- | salary       | int     |
-- | departmentId | int     |
-- +--------------+---------+

-- Table: Department
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int pk  |
-- | name        | varchar |
-- +-------------+---------+

-- Повертає робітників, які мають найбільшу зарплату в кожному департаменті
SELECT D.name AS "Department", E.name AS "Employee", E.salary AS "Salary"
FROM (
    SELECT name, salary, departmentId FROM Employee
    WHERE (salary, departmentId) IN (
        SELECT MAX(salary), departmentId FROM Employee
        GROUP BY departmentId
    )
) E
JOIN Department D ON D.id = E.departmentId

-- RESULT: Department, Employee, Salary