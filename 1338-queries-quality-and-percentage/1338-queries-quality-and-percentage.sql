# Write your MySQL query statement below
WITH tmp AS (
SELECT 
query_name, 
round(avg(rating/position),2) AS quality, 
SUM(CASE WHEN rating < 3 THEN 1 
ELSE 0
END) AS poor_query_num, 
count(rating) as total_rating
FROM Queries
GROUP BY query_name )

SELECT 
query_name, 
quality, 
round(poor_query_num/total_rating*100, 2)  AS poor_query_percentage
FROM tmp


-- SELECT
--   query_name,
--   ROUND(AVG(rating / position), 2) AS quality,
--   ROUND(SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) / COUNT(*) * 100, 2) AS poor_query_percentage
-- FROM Queries
-- GROUP BY query_name;

