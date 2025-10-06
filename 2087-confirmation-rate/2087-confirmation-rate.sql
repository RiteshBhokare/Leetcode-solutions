# Write your MySQL query statement below
select s.user_id, round(avg(if(c.action = "confirmed",1,0)),2)  "confirmation_rate"
from Confirmations c right join Signups s 
on c.user_id = s.user_id
group by s.user_id
 