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
    statename = sys.argv[4]
    # Select states
    mycur.execute(
            "SELECT * FROM states WHERE\
                    BINARY name='{}' ORDER BY id ASC".format(statename))

    for row in mycur.fetchall():
        print(row)
    cur.close()
    conn.close()
