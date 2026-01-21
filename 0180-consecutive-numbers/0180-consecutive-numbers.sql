# Write your MySQL query statement below
select distinct num as ConsecutiveNums
from (select num,
        LAG(num,1) over(order by id) prev1, 
        LAG(num,2) over(order by id) prev2
        from Logs) Logs1
    where (num = prev1) and (num = prev2) ;
