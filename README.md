# Logs Analysis

This logs analysis project uses SQL queries in Python code to answer three questions from a database of news articles and their views.  A Linux-based VM is used for the database and to run the code.

## Installation

1.	Use [these](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0) instructions to download and set up the virtual machine.
2.	Using the terminal, '''cd''' into the created `vagrant` directory.
3.	While in the vagrant directory, bring the VM online with `vagrant up` and `vagrant ssh`.
4.	Download the news SQL database [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).  When unzipped, put this file in the `vagrant` directory.
5.	While in your `vagrant` directory, use the command `psql -d news -f newsdata.sql` to complete installation.

## Usage

Before running the logs.py file, you must create two views(most_popular and errors) in PSQL.  While in your `vagrant` directory, run `psql news` to enter the news database.  From there:

To set up most_popular:
```
create view most_popular as
select authors.name, count(*) as views, articles.title
from authors join articles on authors.id = articles.author
join log on articles.slug = substring(log.path from 10)
group by log.path, authors.name, articles.title
order by views desc;
```

To set up errors:
```
create view errors as
select date(time), sum(case when status = '404 NOT FOUND' then 1 else 0 end) as count_error, count(*) as total_requests
from log
group by date(time);
```

After this, you are ready to run the code!  Enter `\q` to exit psql.  While still in the VM `vagrant` directory, run `python logs.py`