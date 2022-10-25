#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class User(BaseModel, Base):
    """
    Database vs File Storage Method for User
    """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':  # db storage
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        places = relationship("Place", backref="user",
                            cascade="all, delete-orphan")
    else:  # All other storage (file)
        email = ''
        password = ''
        first_name = ''
        last_name = ''

