#!/usr/bin/python3

"""
A MySQL script that is safe from SQl
Injections, based on code in 2-filter_states.py file
"""


import MySQLdb
import sys

if __name__ == "__main__":
    # connect to MySQLdb
    mydb = MySQLdb.connect(
        host="localhost", port=3306, user=sys.argv[1],
        password=sys.argv[2], database=sys.argv[3])
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
        (sys.argv[4],)
        )
    row = mycursor.fetchall()
    for i in row:
        print(i)
