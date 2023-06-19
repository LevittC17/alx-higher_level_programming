#!/usr/bin/python3

"""
Script that lists all states from
the database hbtn_0e_0_usa
"""


import MySQLdb
import sys

if __name__ == "__main__":
    # connect to MySQL database
    mydb = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3],
                           charset='utf8mb4')
    mycursor = mydb.cursor()

    mycursor.execute("SELECT cities.id,\
                cities.name, states.name FROM cities\
                INNER JOIN states ON\
                cities.state_id=states.id ORDER BY cities.id ASC")

    mycities = mycursor.fetchall()
    for data in mycities:
        print(data)

    mycursor.close()
    mydb.close()
