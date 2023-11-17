#!/usr/bin/python3
"""
This script takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.

This time the script is safe from
MySQL injections!
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (sys.argv[4],))
    rows = cur.fetchall()
    
    for row in rows:
        print(row)
    
