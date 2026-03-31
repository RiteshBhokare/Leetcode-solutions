# Write your MySQL query statement below
with cte as (select * 
from (select *, dense_rank() over(partition by departmentId order by salary        desc) "rk" 
from employee) t
where rk <= 3
)

select d.name as "Department", e.name as "Employee",e.salary as "Salary"
from cte e inner join Department d
on e.departmentId = d.id
