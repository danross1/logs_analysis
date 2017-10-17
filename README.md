# Views

This logs analysis uses two SQL views, most_popular and errors.  Before running the python code, make sure you enter the VM psql news database. 

To set up most_popular:
'''
create view most_popular as
select authors.name, count(*) as views, articles.title
from authors join articles on authors.id = articles.author
join log on articles.slug = substring(log.path from 10)
group by log.path, authors.name, articles.title
order by views desc;
'''

To set up errors:
'''
create view errors as
select date(time), sum(case when status = '404 NOT FOUND' then 1 else 0 end) as count_error, count(*) as total_requests
from log
group by date(time);
'''

