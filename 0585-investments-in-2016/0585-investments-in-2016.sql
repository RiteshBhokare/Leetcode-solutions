# Write your MySQL query statement below
select round(sum(i.tiv_2016),2) as tiv_2016 
from insurance i
join (
    select tiv_2015
    from insurance
    group by tiv_2015
    having count(*) > 1
) t1
on i.tiv_2015 = t1.tiv_2015 
join (
    select lat, lon
    from insurance
    group by lat, lon
    having count(*) = 1
) t2 
on i.lat = t2.lat and i.lon = t2.lon
