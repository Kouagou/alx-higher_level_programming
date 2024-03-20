#!/usr/bin/python3
""" A script that takes in the name of a state as an argument and
    lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """ Create a connexion and then fetch all the cities
        by state.
    """
    cnx = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3], charset="utf8")
    cur = cnx.cursor()
    cur.execute("SELECT cities.name FROM \
            cities INNER JOIN states ON cities.state_id = states.id \
            WHERE states.name = %s ORDER BY cities.id ASC", (argv[4],))
    rows = cur.fetchall()
    if rows is not None:
        print(", ".join([row[0] for row in rows]))
    cur.close
    cnx.close()
