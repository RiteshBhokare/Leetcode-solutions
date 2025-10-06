# Write your MySQL query statement below
select s.student_id, s.student_name , su.subject_name, ifNull(count(e.student_id),0) "attended_exams"
from Students s cross join Subjects su
left join Examinations e
on e.subject_name = su.subject_name and
e.student_id = s.student_id  
group by s.student_id, su.subject_name 
order by s.student_id, su.subject_name