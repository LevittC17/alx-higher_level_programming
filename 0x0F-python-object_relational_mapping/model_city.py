#!/usr/bin/python3

"""
Python file similar to model_state.py named
model_city.py that contains the
class definition of a City.
"""

from model_state import Base, State
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class City(Base):
    """ City class:inherits from Base (imported from model_state)"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True,
                unique=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
