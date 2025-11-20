# Write your MySQL query statement below
SELECT p.product_name, sum(o.unit) unit
FROM Products p JOIN Orders o
ON p.product_id = o.product_id
where o.order_date like "2020-02%"
group by o.product_id
having sum(o.unit) >= 100