# Write your MySQL query statement below
select query_name, round(sum(rating/position)/count(query_name),2) quality, round(sum(if(rating<3,1,0))*100/count(*),2) poor_query_percentage 
from  Queries 
group by query_name 