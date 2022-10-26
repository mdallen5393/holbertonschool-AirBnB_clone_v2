#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os
# from models.user import User
# from models.state import State
# from models.amenity import Amenity
# from models.review import Review


class City(BaseModel, Base):  # +T6: Base
    """ The city class, contains state ID and name """
    # if os.getenv('HBNB_TYPE_STORAGE') == "db":
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'),
                      nullable=False)  # +T6
    name = Column(String(128), nullable=False)  # +T6

    places = relationship('Place', backref='cities',
                          cascade='all, delete, delete-orphan')
    # else:
    #     state_id = ""  # -T6
    #     name = ""  # -T6
