#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def fetch_cities():
    if len(sys.argv) != 4:
        print("Usage: ./14-model_city_fetch_by_state.py " +
              "<mysql username> <mysql password> <database name>")
        return

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{mysql_username}:{mysql_password}'
        f'@localhost/{database_name}'
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = (
        session.query(City, State)
        .join(State)
        .order_by(City.id)
        .all()
    )

    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()


if __name__ == '__main__':
    fetch_cities()
