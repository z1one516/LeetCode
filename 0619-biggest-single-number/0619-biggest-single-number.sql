# Write your MySQL query statement below
WITH single AS (
SELECT 
num
FROM MyNumbers
GROUP BY num 
HAVING count(num)  = 1
)

SELECT 
max(num) as num
FROM single