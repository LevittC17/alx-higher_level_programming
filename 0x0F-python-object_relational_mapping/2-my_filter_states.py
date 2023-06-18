#!/usr/bin/python3

"""
script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa 
where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Open database connection
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query using execute() method.
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
    ORDER BY id ASC".format(sys.argv[4]))

    # Fetch a single row using fetchone() method.
    data = cursor.fetchall()

    # disconnect from server
    cursor.close()
    db.close()

    for row in data:
        if row[1] == sys.argv[4]:
            print(row)
