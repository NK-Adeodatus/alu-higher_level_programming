#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa.

Usage: ./5-filter_cities.py <mysql username> <mysql password> \
                            <database name> <state name>
This script is SQL injection-free.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to the MySQL database using command-line arguments
    db = MySQLdb.connect(
        user=sys.argv[1],    # MySQL username
        passwd=sys.argv[2],  # MySQL password
        db=sys.argv[3],      # Database name
        host="localhost",    # Host where the database is located
        port=3306            # Default MySQL port
    )

    # Create a cursor object to execute SQL queries
    cur = db.cursor()

    # SQL query to fetch cities for the given state, using parameterized query
    query = (
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC"
    )

    # Execute the query, passing the state name as a parameter
    cur.execute(query, (sys.argv[4],))

    cities = cur.fetchall()

    city_names = ", ".join(city[0] for city in cities)

    print(city_names)

    cur.close()
    db.close()
