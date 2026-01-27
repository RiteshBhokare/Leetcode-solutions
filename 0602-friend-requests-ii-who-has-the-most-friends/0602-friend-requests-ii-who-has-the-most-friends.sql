# Write your MySQL query statement below
select id, count(*) num
from (select requester_id id 
        from RequestAccepted
        union all
        select accepter_id id from RequestAccepted) b
group by 1
order by 2 desc
limit 1 