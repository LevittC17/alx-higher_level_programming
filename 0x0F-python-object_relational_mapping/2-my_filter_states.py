#!/usr/bin/python3

"""
Script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where `name` matches the argument
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQL.connect(host="localhost", port=3306,
                       user=sys.argv[1], passwd=sys.argv[2],
                       db=sys.argv[3], charset="utf8")
    mycursor = cursor()
    mycursor.execute("""SELECT * FROM states WHERE name
                     LIKE BINARY '{}'\\ ORDER BY id
                     ASC""".format(sys.argv[4]))
    for row in mycursor.fetchall():
        print(row)

    mycursor.close()
    db.close()
