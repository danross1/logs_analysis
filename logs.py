#!/usr/bin/env python

import psycopg2


def database_function(query):
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    return results


def top_articles():
    query = ("SELECT title, views "
             "FROM most_popular "
             "ORDER BY views DESC "
             "LIMIT 3;")
    results = database_function(query)
    print("\nWhat are the top three articles of all time?\n")
    for title, views in results:
        print("    {} -- {} views".format(title, views))


def top_authors():
    query = ("SELECT name, sum(views) as total_views "
             "FROM most_popular "
             "GROUP BY name "
             "ORDER BY total_views DESC;")
    results = database_function(query)
    print("\nWho are the most popular authors of all time?\n")
    for name, total_views in results:
        print("    {} -- {} views".format(name, total_views))


def err_rates():
    query = ("SELECT date, ((count_error::double precision) "
             "/ (total_requests::double precision) * 100) as error_rate "
             "FROM errors "
             "WHERE ((count_error::double precision) "
             "/ (total_requests::double precision) > 0.01);")
    results = database_function(query)
    print("\nOn which date did more than 1% of requests lead to errors?\n")
    for date, error_rate in results:
        print("    {} -- {}%".format(date, error_rate))

if __name__ == "__main__":
    top_articles()
    top_authors()
    err_rates()
