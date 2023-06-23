#!/usr/bin/python3

"""
script that prints the State object with the
name passed as argument from the
database hbtn_0e_6_usa
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
    # Configuring session to bind the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    passed_name = session.query(State).filter(
        State.name == sys.argv[4]).first()

    if passed_name is None:
        print('Not found')
    else:
        print(passed_name.id)

    session.close()
