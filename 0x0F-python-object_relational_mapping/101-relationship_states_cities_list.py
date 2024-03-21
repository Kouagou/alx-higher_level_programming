#!/usr/bin/python3
""" A script that lists all State objects, and corresponding City objects,
    contained in the database hbtn_0e_101_usa.
"""
from relationship_state import Base, State
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from sqlalchemy.orm import lazyload

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                           argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).outerjoin(City).order_by(State.id, City.id).all()
    if states is not None:
        for state in states:
            print("{}: {}".format(state.id, state.name))
            if state.cities is not None:
                for city in state.cities:
                    print("    {}: {}".format(city.id, city.name))

    session.close()
