#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
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
        cities = getCities(self.id)

    def getCities(self, id): # +T6
        """Returns a list of City instances with state_id = id"""
        cities = {}
        for key, val in FileStorage.all('City').items():
            if val.state_id == id:
                cities[key] = val
        return cities
