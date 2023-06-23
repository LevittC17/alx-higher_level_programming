#!/usr/bin/python3
"""takes in the name of a state as an argument and lists all cities of that
 state, using the database hbtn_0e_4_usa"""

import MySQLdb
import sys


if __name__ == "__main__":

    mydb = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])

    mycursor = mydb.cursor()
    mycursor.execute("SELECT cities.name\
                FROM cities LEFT JOIN states\
                ON states.id = cities.state_id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC", (sys.argv[4],))
    mydata = mycursor.fetchall()
    print(", ".join([data[0] for data in mydata]))
    mycursor.close()
    mydb.close()
