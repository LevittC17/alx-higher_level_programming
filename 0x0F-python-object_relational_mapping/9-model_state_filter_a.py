#!/usr/bin/python3

"""
script that lists all State objects that
contain the letter a from the database
hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # create engine to connect to MySQLdb
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]),
                           pool_pre_ping=True)
    # Generating a db schema
    Base.metadata.create_all(engine)

    # Configuring a session to bind the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    contain_a = session.query(State).filter(
        State.name.like('%a%')).order_by(
        State.id)
    # Iterate through the query
    for state in contain_a:
        print(f"{state.id}: {state.name}")

    session.close()
