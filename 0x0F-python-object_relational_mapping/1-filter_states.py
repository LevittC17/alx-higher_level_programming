#!/usr/bin/python3

"""
Script that lists all state with a name starting with N
(upper N) from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port="3306"
                           user=sys.argv[1], passwd=sys.argv[2]
                           db=sys.argv[3], charset="utf8")
    mycursor = db.cursor()

    mycursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'
                     ORDER BY id ASC")
    for row in mycursor.fetchall():
        if row[1][0] == 'N':
            print(row)

    mycursor.close()
    db.close()
