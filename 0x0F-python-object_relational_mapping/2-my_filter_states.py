#!/usr/bin/python3
"""takes in an argument and displays all values"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
    id ASC".format(argv[4]))
    r_rows = cur.fetchall()
    for row in r_rows:
        if row[1] == argv[4]:
            print(row)
    cur.close()
    db.close()
