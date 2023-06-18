#!/usr/bin/python3

""" This module takes an argument and displays all values states
    database hbtn_0e_0_usa WHERE name matches the argument.
"""


import MySQLdb
import sys


if __name__ == "__main__":
    """
        Function containing code to select the state provided
        in the argument.
    """
    # Create a database connection
    mydb = MySQLdb.connect(
                host="localhost", port=3306, user=sys.argv[1],
                passwd=sys.argv[2], db=sys.argv[3], charset="utf8"
            )
    mycur = mydb.cursor()
    stateName = sys.argv[4]
    # Select states
    mycur.execute(
            "SELECT * FROM states WHERE\
                    BINARY name='{}' ORDER BY id ASC".format(stateName))
    query = mycur.fetchall()
    for row in query:
        print(row)
    cur.close()
    conn.close()
