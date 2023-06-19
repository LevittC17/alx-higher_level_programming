#!/usr/bin/python3

"""
A MySQL script that is safe from SQl
Injections, based on code in 2-filter_states.py file
"""


import MysQLdb
import sys

if __nama__ == "__main__":
    # connect to MySQLdb
     mydb = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        password=argv[2], database=argv[3])
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
        (argv[4],)
        )
    row = mycursor.fetchall()
    for i in row:
        print(i)
