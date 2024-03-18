#!/usr/bin/python3
""" A script that lists all states with a name starting with N
    (upper N) from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys

if __name__ == '__main__':
    """ Create a connexion and then fetch all the states starting
        with N present in the database.
    """
    cnx = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                          passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = cnx.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close
    cnx.close()
