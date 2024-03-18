#!/usr/bin/python3
""" A script that lists all states from the database hbtn_0e_0_usa. """
import MySQLdb
import sys

cnx = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2],
                      database=sys.argv[3])
cur = cnx.cursor()
cur.execute("SELECT * FROM states")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close
cnx.close()
