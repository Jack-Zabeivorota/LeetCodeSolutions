--------------------- SOLUTION 178 -----------------------------------
-- Table: Scores
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int pk  |
-- | score       | decimal |
-- +-------------+---------+

-- Повертає відсортовані очки з назначеними рангами
SELECT score, DENSE_RANK() OVER (ORDER BY score DESC) as "rank"
FROM Scores

-- RESULT: score, rank