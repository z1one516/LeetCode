# Write your MySQL query statement below
SELECT
event_day as `day`, emp_id, 
sum(stay_minutes) as total_time
FROM 
(SELECT
emp_id, event_day, out_time - in_time  as stay_minutes
FROM Employees) calculation
GROUP BY `day`, emp_id