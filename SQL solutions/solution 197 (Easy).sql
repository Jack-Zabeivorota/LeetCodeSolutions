--------------------- SOLUTION 197 -----------------------------------
-- Table: Weather
-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | id            | int pk  |
-- | recordDate    | date    |
-- | temperature   | int     |
-- +---------------+---------+

-- Повертає ідентифікатори записів, температура яких була більше ніж у попередній день
SELECT id AS "Id" FROM (
    SELECT
        id, recordDate, temperature,
        LAG(temperature) OVER (ORDER BY recordDate) AS prev_temperature,
        LAG(recordDate) OVER (ORDER BY recordDate) AS prev_recordDate
    FROM Weather
)
WHERE
    prev_temperature IS NOT NULL AND
    recordDate - prev_recordDate = 1 AND
    temperature > prev_temperature

-- RESULT: id