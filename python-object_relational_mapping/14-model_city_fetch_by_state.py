#!/usr/bin/python3

"""
Fetches and displays all City objects
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

if __name__ == "__main__":
    db_engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )

    Session = sessionmaker(bind=db_engine)
    db_session = Session()

    results = (
        db_session.query(City, State)
        .join(State, City.state_id == State.id)
        .order_by(City.id)
    )

    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")
