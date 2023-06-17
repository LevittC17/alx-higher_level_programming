#!/usr/bin/python3

"""
Script that lists all state with a name starting with N
(upper N) from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    mydb = MySQLdb.connect(host="localhost", port="3306"
                           user=sys.argv[1], passwd=sys.argv[2]
                           db=sys.argv[3], charset="utf8")
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'
                     ORDER BY id ASC")
    for row in mycursor.fetchall():
        print(row)

    mycursor.close()
    mydb.close()
