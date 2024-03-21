#!/usr/bin/python3
""" A  Python file similar to model_state.py named model_city.py
    that contains the class definition of a City.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State
from sqlalchemy.orm import relationship


class City(Base):
    """ Defines City class """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    state = relationship("State", back_populates="cities")
