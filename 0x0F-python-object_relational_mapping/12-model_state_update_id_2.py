#!/usr/bin/python3

"""
script that changes the name of a
State object from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Variables to store user, passwd, db
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    # Create engine to connect to MySQLdb
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, password, db),
                           pool_pre_ping=True)

    # Generating db schema
    Base.metadata.create_all(engine)

    # Create session to bind engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # Get state whose id == 2
    change_state = session.query(State).filter(State.id == 2).first()
    change_state.name = 'New Mexico'
    session.commit()

    session.close()
