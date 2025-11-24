# Write your MySQL query statement below
SELECT S.employee_id
FROM Employees e
RIGHT JOIN Salaries s
ON e.employee_id = s.employee_id
WHERE e.name is null
UNION
SELECT e.employee_id
FROM Employees e
LEFT JOIN Salaries s
ON e.employee_id = s.employee_id
WHERE s.salary is null
ORDER BY employee_id

