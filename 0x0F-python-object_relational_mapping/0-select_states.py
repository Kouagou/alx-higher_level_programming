#!/usr/bin/python3
""" A script that lists all states from the database hbtn_0e_0_usa. """
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """ Create a connexion and then fetch all the states
        present in the database.
    """
    cnx = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3], charset="utf8")
    cur = cnx.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close
    cnx.close()