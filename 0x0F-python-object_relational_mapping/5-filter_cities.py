#!/usr/bin/python3

"""
script that takes in the name of a state
as an argument and lists all cities of
that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # connect to MySQL database
    mydb = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    mycursor = db.cursor()

    mycursor.execute("SELECT cities.id, cities.name, states.name \
    FROM cities JOIN states ON cities.state_id = states.id \
    WHERE states.name = '{}';".format(sys.argv[4]))

    data = mycursor.fetchall()
    print(', '.join([x[0] for x in data]))

    mycursor.close()
    mydb.close()
