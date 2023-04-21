#!/usr/bin/python3
"""
returns all the table values of the table states
the parameter are: username, password, database
"""

import MySQLdb
from sys import argv

if __name__=="__main__":

    # connecting to the database
    db = MySQLdb.connect(host="localhost",
            port=3306,
            user=argv[1],
            paswd=argv[2],
            db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
