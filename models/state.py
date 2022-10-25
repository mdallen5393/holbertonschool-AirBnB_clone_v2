#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base): # +T6: Base
    """ State class """
    __tablename__ = 'states'
    # name = "" # -T6
    name = Column(String(128), nullable=False) # +T6 vvv
    storage = os.getenv('HBNB_TYPE_STORAGE')
    if storage == 'db':
        cities = relationship("")
    if storage == 'file':
        cities = cities()

    @property
    def cities(self): # +T6
        """Returns a list of City instances with state_id = id"""
        cities = {}
        for key, val in storage.all('City').items():
            if val.state_id == id:
                cities[key] = val
        return cities
