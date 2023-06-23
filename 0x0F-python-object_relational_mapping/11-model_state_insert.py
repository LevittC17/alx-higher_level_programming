#!/usr/bin/python3

"""
script that adds the State object
“Louisiana” to the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Variables to stor user, passwd and db
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    # Create engine to connect to MySQLdb
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, password, db),
                           pool_pre_ping=True)

    # Generating db schema
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new state
    new_state = State(name='Louisiana')
    session.add(new_state)

    # Commit the new state to the db schema
    session.commit()
    print(new_state.id)

    session.close()
