#!/usr/bin/python3

"""
A script that lists all states from the database hbtn_0e_0_usa
Arguments: mysql username, mysql password database name
"""


if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC;")
    for row in cur.fetchall():
        print(row)
