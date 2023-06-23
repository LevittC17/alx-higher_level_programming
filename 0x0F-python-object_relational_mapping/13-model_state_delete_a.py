#!/usr/bin/python3

"""
script that deletes all State objects with a
name containing the letter a from the
database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Variables to store user, passwd and db
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    # Create engine to connect to MySQLdb
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, password, db),
                           pool_pre_ping=True)

    # Generating a db schema
    Base.metadata.create_all(engine)

    # Createing a session to bind engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # A query to delete states containing `a`
    contain_a = session.query(State).filter(State.name.like('%a%'))
    for state in contain_a:
        session.delete(state)
    # Save the changes to db
    session.commit()

    # Close the session
    session.close()
