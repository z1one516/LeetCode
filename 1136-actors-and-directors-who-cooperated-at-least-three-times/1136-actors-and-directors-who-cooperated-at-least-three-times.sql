# Write your MySQL query statement below
wITH combination AS 
    (SELECT actor_id, director_id, count(*) AS comb
    FROM ActorDirector
    GROUP BY actor_id, director_id)
SELECT actor_id, director_id
FROM combination
WHERE comb >= 3
