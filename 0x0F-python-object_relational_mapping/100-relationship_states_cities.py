#!/usr/bin/python3
""" A script that creates the State “California” with the City
    “San Francisco” from the database hbtn_0e_100_usa.
"""
from relationship_state import Base, State
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                           argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name="California")
    city = City(name="San Francisco")
    state.cities = [city]
    session.add(state)

    session.commit()
    session.close()
