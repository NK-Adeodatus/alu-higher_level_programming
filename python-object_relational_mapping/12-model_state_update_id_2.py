#!/usr/bin/python3
"""
Changes the name of the State object with id = 2 to "New Mexico"
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine and session
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{db_name}',
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the state with id = 2
    state = session.query(State).filter(State.id == 2).first()

    if state:
        # Change the name of the state
        state.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
