#!/usr/bin/env python3
"""
Creating a User class for authentication
"""

from sqlalchemy.ext.declarative import declarative base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    """
    User authentication class
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    sessiom_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)
