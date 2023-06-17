#!/usr/bin/python3

"""
A script that lists all states from the database hbtn_0e_0_usa
Arguments: mysql username, mysql password database name
"""


import MySQLdb
import mysql.connector
from sys import argv

if __name__ == "__main__":
    db = mysql.connector.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2],
                         db=argv[3], charset="utf8")
    mycur = db.cursor()
    mycur.execute("SELECT * FROM states ORDERED BY id ASC")
    rows = mycur.fetchall()
    for row in rows:
        print(row)
    mycur.close()
    db.close()
