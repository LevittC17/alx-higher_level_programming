#!/usr/bin/python3

"""
script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""


import MySQLdb
import sys


if __name__ == "__main__":
    # Create a database connection
    mydb = MySQLdb.connect(
                host="localhost", port=3306, user=sys.argv[1],
                passwd=sys.argv[2], db=sys.argv[3], charset="utf8mb4"
            )
    mycur = mydb.cursor()
    state_name = sys.argv[4]
    # Select states
    mycur.execute(
            "SELECT * FROM states WHERE\
                    BINARY name='{}' ORDER BY id ASC".format(state_name))
    query = mycur.fetchall()
    for row in query:
        print(row)

    mycur.close()
    mydb.close()
