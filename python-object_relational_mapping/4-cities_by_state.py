"""Lists all cities of the database hbtn_0e_4_usa, ordered by city id.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to the MySQL database using the provided arguments
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Create a cursor object to execute SQL queries
    c = db.cursor()
    
    # Execute the SQL query to fetch city and state information
    c.execute("SELECT c.id, c.name, s.name \
                FROM cities as c \
                INNER JOIN states as s \
                ON c.state_id = s.id \
                ORDER BY c.id")
    [print(city) for city in c.fetchall()]
