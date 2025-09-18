# Write your MySQL query statement below
DELETE p
FROM Person p
JOIN (

SELECT email, MIN(id) as keep_id
FROM Person
GROUP BY email
)
t ON p.email = t.email
WHERE p.id != t.keep_id
