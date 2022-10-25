#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
# from models.user import User
# from models.state import State
# from models.amenity import Amenity
# from models.place import Place
# from models.review import Review
import os


class City(BaseModel, Base):  # +T6: Base
    """ The city class, contains state ID and name """
    if os.getenv('HBNB_TYPE_STORAGE' == 'db'):
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'),
                          nullable=False)  # +T6
        name = Column(String(128), nullable=False)  # +T6
    else:
        state_id = ""  # -T6
        name = ""  # -T6

    places = relationship("Place", backref="cities",
                          cascade="all, delete-orphan")
