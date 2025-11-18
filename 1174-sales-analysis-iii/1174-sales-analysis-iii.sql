# Write your MySQL query statement below
SELECT p.product_id , p.product_name    
FROM Sales s left join Product p
ON p.product_id = s.product_id
group by p.product_id, p.product_name
HAVING MIN(s.sale_date) >= '2019-01-01'
   AND MAX(s.sale_date) <= '2019-03-31';



