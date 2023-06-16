#!/usr/bin/python3

"""
A script that lists all states from the database hbtn_0e_0_usa
Arguments: mysql username, mysql password database name
"""


from MySQLdb import _mysql
import sys

if __name__ == "__main__":
    """lists all
    states from the database hbtn_0e_0_usa"""

    db = -_mysql.connect(host="localhost", port=3306,
                        user=sys.argv[1], passwd=sys.argv[2],
                        db=sys.argv[3], charset="utf8")
    cur = db.cursor()
