#!/usr/bin/python3
""" A script that prints all City objects from the database hbtn_0e_14_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                           argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    res = session.query(City, State).filter(
            State.id == City.state_id
            ).order_by(City.id).all()
    for c, s in res:
        print("{}:({}) {}".format(s.name, c.id, c.name))
