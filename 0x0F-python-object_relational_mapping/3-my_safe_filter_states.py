#!/usr/bin/python3

"""
A MySQL script that is safe from SQl
Injections, based on code in 2-filter_states.py file
"""


import MysQLdb
import sys

if __nama__ == "__main__":
    # connect to MySQLdb
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        charset='utf8mb4'
    )

    mycur = db.cursor()
    mycur.execute(
        "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
        (argv[4],)
        )
    code = mycur.fetchall()
    for data in code:
        print(data)
