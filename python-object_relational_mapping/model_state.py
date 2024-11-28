#!/usr/bin/python3
"""
This module contains the definition of the State class,
which maps to the 'states' table in the MySQL database.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for our model classes
Base = declarative_base()

class State(Base):
    """
    Represents the 'states' table in the database.
    """
    __tablename__ = 'states'  # Name of the table in the database

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
