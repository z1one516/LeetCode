# Write your MySQL query statement below
SELECT 
U.name, 
IFNULL(SUM(R.distance),0) as travelled_distance
FROM Users U
LEFT JOIN Rides R
ON U.id = R.user_id
GROUP BY U.id
ORDER BY travelled_distance DESC, name ASC