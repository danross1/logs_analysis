import psycopg2

db = psycopg2.connect("dbname=news")

c = db.cursor()

c.execute(
    "select title, views "
    "from most_popular "
    "order by views desc "
    "limit 3;")

q1 = c.fetchall()

print(q1)

c.execute(
    "select name, sum(views) as total_views "
    "from most_popular "
    "group by name "
    "order by total_views desc;")

q2 = c.fetchall()

print(q2)

c.execute(
    "select date "
    "from errors "
    "where ((count_error::double precision) "
    "/ (total_requests::double precision) > 0.01);")

q3 = c.fetchall()

print(q3)

db.close()
