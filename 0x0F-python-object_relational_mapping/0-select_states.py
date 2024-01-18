#!/usr/bin/python3
"""
The module declaration for a MySQL connection that
lists all unique states from the database hbtn_0e_0_usa.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", port=3306,
                                 user=argv[1], passwd=argv[2],
                                 db=argv[3], charset="utf8")

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Use a set to store unique states
    unique_states = set()

    for state in cursor.fetchall():
        # Check if the state is not in the set before printing
        if state[1] not in unique_states:
            print(state)
            unique_states.add(state[1])

    cursor.close()
    connection.close()
