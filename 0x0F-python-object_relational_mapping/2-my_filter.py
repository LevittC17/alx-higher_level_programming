#!/usr/bin/python3

"""
Script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where `name` matches the argument
"""

import MySQLdb
import sys

# Script executed only in this file
if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    statename = sys.argv[4]

    # connect to MySQL DB
    db = MySQL.connect(host='localhost', port=3306
                       user=username, passwd=password, db=database)
    mycursor = cursor()

    # Sorting results in ascending order by state.id
    mycursor.execute("""SELECT * FROM states WHERE
                     name='{}' ORDER BY id ASC""".format(statename))
    # Fething and printing values with a For Loop
    for values in mycursor.fetchall():
        print(values)

    # Closing the cursor and database in that order
    mycursor.close()
    db.close()
