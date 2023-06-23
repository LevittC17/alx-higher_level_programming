#!/usr/bin/python3

"""
script that lists all State objects from
the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    # create engine that connects to MysQLdb
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    # bind the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # retrieving all state objects from the database
    states = session.query(State).order_by(State.id).all()

    # iterating through the results stored in states variable
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
