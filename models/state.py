#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
# from models.__init__ import storage
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os
import models


class State(BaseModel, Base): # +T6: Base
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False) # +T6 vvv
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state",
                               cascade="all, delete, delete-orphan")
    # else:
    #     name = "" # -T6

    @property
    def cities(self): # +T6
        """Returns a list of City instances with state_id = id"""
        cities = []
        for thing in models.storage.all(City).values():
            if thing.state_id == self.id:
                cities.append(thing)
        return cities
