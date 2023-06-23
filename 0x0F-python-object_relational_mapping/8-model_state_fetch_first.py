#!/usr/bin/python3

"""
script that prints the first State
object from the database hbtn_0e_6_usa
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
    first_state = session.query(State).first()
    if first_state is None:
        print('Nothing')
    else:
        print("{}: {}".format(first_state.id,
                       first_state.name))

    session.close()
