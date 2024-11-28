#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa.
Usage: ./7-model_state_fetch_all.py <mysql username>
                                    <mysql password>
                                    <database name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
    f'mysql+mysqldb://{username}:{password}@localhost/{db_name}',
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).order_by(State.id).first()

    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")

    session.close()
