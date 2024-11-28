#!/usr/bin/python3
"""Displays all values in the states table of the database hbtn_0e_0_usa
whose name matches that supplied as argument.
Safe from SQL injections.
Usage: ./3-my_safe_filter_states.py <mysql username> \
                                    <mysql password> \
                                    <database name> \
                                    <state name searched>"""

import sys
import MySQLdb

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

    query = ("SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
