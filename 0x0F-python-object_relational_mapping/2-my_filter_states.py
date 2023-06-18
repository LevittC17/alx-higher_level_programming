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
    db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)
    cur = db.cursor()

    # Create and execute the SQL query
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY states.id ASC".format(state_name)
    cur.execute(query)

    # Fetch and display the results
    results = cur.fetchall()
    for row in results:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()

