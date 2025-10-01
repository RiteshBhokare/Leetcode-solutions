# Write your MySQL query statement below
select e1.name "Employee" 
from Employee e1 inner join Employee e2
on e2.id = e1.managerId
where e1.salary > e2.salary