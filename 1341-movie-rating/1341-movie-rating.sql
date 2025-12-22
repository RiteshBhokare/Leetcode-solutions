# Write your MySQL query statement below
-- select name 
-- from Users 
-- where user_id in (select count(user_id) from MovieRating )

(select u.name as results
from Users u, MovieRating m
where u.user_id = m.user_id
group by m.user_id
order by count(*) desc, u.name
limit 1)

union all

(select m.title
from Movies m, MovieRating mr
where m.movie_id = mr.movie_id and mr.created_at like "2020-02%"
group by mr.movie_id
order by avg(mr.rating) desc, m.title
limit 1)