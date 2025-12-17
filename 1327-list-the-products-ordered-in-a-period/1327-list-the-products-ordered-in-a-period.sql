# Write your MySQL query statement below
-- SELECT P.product_name, O.unit 
-- FROM Products P 
-- LEFT JOIN (SELECT product_id, SUM(unit) OVER (PARTITION BY product_id) as unit From Orders 
-- WHERE order_date >= '20200201' AND order_date < '20200229') O 
-- ON P.product_id = O.product_id 
-- WHERE O.unit >= 100 
-- GROUP BY P.product_name

SELECT P.product_name, SUM(O.unit) AS unit
FROM Products P 
LEFT JOIN  Orders O 
ON P.product_id = O.product_id 
WHERE O.order_date >= '20200201' 
        AND O.order_date < '20200301'
GROUP BY P.product_id, P.product_name
HAVING Sum(O.unit) >= 100