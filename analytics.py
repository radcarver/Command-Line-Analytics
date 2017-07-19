#!/usr/bin/env python
import psycopg2


def get_results(query, dbname='news'):
    conn = psycopg2.connect('dbname={}'.format(dbname))
    cursor = conn.cursor()
    cursor.execute('{}'.format(query))
    return cursor.fetchall()
    conn.close()


def step_one():
    print ("\nHere are the three most popular articles of all time:\n" +
           "-------------------------------------------------------")
    foo = get_results("SELECT title, count(*)FROM log "
                      "LEFT JOIN articles ON log.path "
                      "LIKE CONCAT('%',articles.slug) "
                      "WHERE title IS NOT NULL GROUP BY title "
                      "ORDER BY count(*) desc LIMIT 3")
    for i in range(len(foo)):
        print("\"" + str(foo[i][0]) + "\" --- " + str(foo[i][1]) + " views")


def step_two():
    print ("\nHere are the most popular authors of all time:\n" +
           "-------------------------------------------------------")
    foo = get_results("SELECT name, count(*) FROM log "
                      "LEFT JOIN articles "
                      "ON log.path LIKE CONCAT('%',articles.slug) "
                      "LEFT JOIN authors on articles.author = authors.id "
                      "WHERE title IS NOT NULL "
                      "GROUP BY name ORDER BY count(*) desc LIMIT 10")
    for i in range(len(foo)):
        print(str(foo[i][0]) + " --- " + str(foo[i][1]) + " views")


def step_three():
    print ("\nOn the following days, over 1% of requests led to errors:\n" +
           "-------------------------------------------------------")
    foo = get_results("select * from (select date(time), cast(((count(*) "
                      "filter (where status like "
                      "concat('4','%')))*100)/count(*)"
                      "::float as numeric(3,2)) as failure_pct "
                      "from log group by date(time) order by failure_pct "
                      "desc limit 10) as foo where failure_pct >=1")
    for i in range(len(foo)):
        print(str(foo[i][0]) + " --- " + str(foo[i][1]) + " failure rate")


if __name__ == "__main__":
    step_one()
    step_two()
    step_three()
    print("\n" + "End of Analytics!\n" +
          "-------------------------------------------------------")
