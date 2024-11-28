#!/usr/bin/python3
"""Displays all values where name matches argument"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Retrieve arguments passed to the script
    mysql_user = sys.argv[1]
    mysql_passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_passwd,
        db=db_name
    )
    cur = conn.cursor()

    query = ("SELECT * FROM states WHERE BINARY name = '{}' "
             "ORDER BY id ASC".format(state_name))
    cur.execute(query)

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
