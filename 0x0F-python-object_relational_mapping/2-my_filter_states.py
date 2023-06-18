#!/usr/bin/python3

"""
script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa 
where name matches the argument.
"""


import sys
import MySQLdb

if __name__ == "__main__":
    # Retrieve command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host='localhost', 
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )
    cur = db.cursor()

    # Create and execute the SQL query
    cur.execute(
        "SELECT *
        FROM states WHERE BINARY
        name='{}' ORDER BY states.id ASC".format(state_name)
    )

    # Fetch and display the results
    selected = cur.fetchall()
    for row in selected:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
