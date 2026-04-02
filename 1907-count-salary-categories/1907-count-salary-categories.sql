# Write your MySQL query statement below
-- select category, count(a.account_id) accounts_count 
-- from (select *, case when income<20000 then "Low Salary" when income between 20000 and 50000 then "Average Salary" else "High Salary" end as category
-- from accounts) t
-- group by category

select "Low Salary" as category,
sum(income < 20000) as accounts_count
from accounts
union
select "Average Salary" as category,
sum(income between 20000 and 50000) as accounts_count
from accounts
union
select "High Salary" as category,
sum(income > 50000) as accounts_count
from accounts