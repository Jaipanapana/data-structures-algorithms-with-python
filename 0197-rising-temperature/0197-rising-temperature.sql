# Write your MySQL query statement below
select t1.id 
from Weather as t1,Weather as t2
where t1.recordDate=date_add(t2.recordDate,interval 1 day) and
t1.temperature>t2.temperature;