# Write your MySQL query statement below
select u.name, ifnull(sum(r.distance),0) travelled_distance
from Users u left join Rides r
on r.user_id = u.id  
group by user_id
order by travelled_distance  desc, name 