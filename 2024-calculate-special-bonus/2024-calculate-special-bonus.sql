# Write your MySQL query statement below
SELECT employee_id, if(name like 'M%', 0, if(employee_id%2 = 0, 0, salary)) bonus
FROM Employees
order by employee_id