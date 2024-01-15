#!/usr/bin/python3
"""
The module declaration for a mysql connection that
lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    connection = MySQLdb.connect(host="127.0.0.1", port=3306,
                                 user=argv[1], password=argv[2],
                                 db=argv[3])

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states")
    db = cursor.fetchall()

    for i in db:
        print(i)

    cursor.close
    connection.close
