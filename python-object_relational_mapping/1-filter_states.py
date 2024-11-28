#!/usr/bin/python3
"""
Lists all the states with a name starting with 'N' from the database hbtn_0e_0_usa.
"""


import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL username, password, and database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
