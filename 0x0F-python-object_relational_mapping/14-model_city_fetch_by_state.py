#!/usr/bin/python3

"""
write a script 14-model_city_fetch_by_state.py
that prints all City objects from the
database hbtn_0e_14_usa
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Variables to store sys arguments
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    # Create engine to connect to MySQLdb
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, password, db),
                           pool_pre_ping=True)

    # Generating a db schema
    Base.metadata.create_all(engine)

    # Creating a session to bind engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all city objects
    myobjects = session.query(
        State,
        City).filter(
        State.id == City.state_id).order_by(
            City.id).all()
    for state, city in myobjects:
        print(f"{state.name}: {city.id} {city.name}")

    session.close()
