--------------------- SOLUTION 262 -----------------------------------
-- Table: Trips
-- +-------------+--------+
-- | Column Name | Type   |
-- +-------------+--------+
-- | id          | int pk |
-- | client_id   | int    |
-- | driver_id   | int    |
-- | city_id     | int    |
-- | status      | enum   | ('completed', 'cancelled_by_driver', 'cancelled_by_client')
-- | request_at  | date   |
-- +-------------+--------+

-- Table: Users
-- +-------------+--------+
-- | Column Name | Type   |
-- +-------------+--------+
-- | users_id    | int pk |
-- | banned      | enum   | ('Yes', 'No')
-- | role        | enum   | ('client', 'driver', 'partner')
-- +-------------+--------+

-- Повертає співвідношення скасованих поїздок від не заблокованих користувачів
-- (клієнтів або водіїв) за день, протягом періоду з 2013-10-01 до 2013-10-03

-- [SLOW (OLD) VERSION]
WITH Valid_T AS (
    SELECT id, status, request_at FROM Trips
    WHERE id NOT IN (
        SELECT T.id FROM Trips T JOIN Users U
        ON (U.users_id = T.client_id OR U.users_id = T.driver_id) AND U.banned = 'Yes'
    ) AND DATE(request_at) BETWEEN '2013-10-01' AND '2013-10-03'
)
SELECT
    Valid_T.request_at AS "Day",
    ROUND(
        SUM(CASE WHEN Canceled_T.id IS NULL THEN 0.0 ELSE 1.0 END) / COUNT(*),
    2) AS "Cancellation Rate"
FROM Valid_T
LEFT JOIN (SELECT id FROM Valid_T WHERE status <> 'completed') Canceled_T
ON Valid_T.id = Canceled_T.id
GROUP BY Valid_T.request_at
ORDER BY Valid_T.request_at


-- [FAST (NEW) VERSION]
SELECT
    request_at AS "Day",
    ROUND(
        SUM(CASE WHEN status <> 'completed' THEN 1.0 ELSE 0.0 END) / COUNT(*),
    2) AS "Cancellation Rate"
FROM Trips
WHERE
    DATE(request_at) BETWEEN '2013-10-01' AND '2013-10-03' AND
    client_id IN (SELECT users_id FROM Users WHERE banned = 'No') AND
    driver_id IN (SELECT users_id FROM Users WHERE banned = 'No')
GROUP BY request_at
ORDER BY request_at

-- RESULT: Day, Cancellation Rate