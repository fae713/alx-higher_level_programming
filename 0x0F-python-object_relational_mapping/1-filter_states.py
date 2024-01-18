#!/usr/bin/python3
"""
A Python script that lists all states with a name starting with N (uppercase N)
from the database hbtn_0e_0_usa.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Extract command-line arguments
    mysql_username, mysql_password, database_name = argv[1], argv[2], argv[3]

    # Connect to MySQL server
    connection = MySQLdb.connect(host="localhost", port=3306,
                                 user=mysql_username, passwd=mysql_password,
                                 db=database_name, charset="utf8")

    # Create a cursor
    cursor = connection.cursor()

    # Execute the query to select states starting with 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    unique_values = set()

    # Fetch and display the results
    for state in cursor.fetchall():
        if state[1] not in unique_values:
            print(state)
            unique_values.add(state[1])

    # Close the cursor and connection
    cursor.close()
    connection.close()
