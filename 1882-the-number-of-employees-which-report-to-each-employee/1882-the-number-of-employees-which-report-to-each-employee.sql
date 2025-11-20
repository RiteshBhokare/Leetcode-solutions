# Write your MySQL query statement below
SELECT n.employee_id, n.name, count(m.employee_id) reports_count, round(AVG(m.age)) average_age 
FROM Employees n JOIN Employees m
ON n.employee_id = m.reports_to
group by employee_id
order by employee_id